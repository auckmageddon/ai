import requests
from celery import shared_task
from models import Profile

KEY   = 'E016707F7036B759C62ADA91CE937C10'

PLAYER_INFO_URL = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}'
VANITY_URL      = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={}&vanityurl={}'
DATABASE_URL    = 'http://api.steampowered.com/ISteamApps/GetAppList/v2'

class FetchFailedException(Exception):
    pass

def get_steam_id(username):
    r = requests.get(VANITY_URL.format(KEY, username))
    if r.ok and r.json()['response']['success'] == 1:
        return r.json()['response']['steamid']


def get_steam_profiles(ids):
    r = requests.get(PLAYER_INFO_URL.format(KEY, ','.join(ids)))
    if r.ok:
        return r.json()['response']['players']


def build_profile(profile):
    return Profile(steam_id=profile['steamid'],
                   username=profile['personaname'],
                   avatar_url=profile['avatar'],
                   profile_url=profile['profileurl'],
                   game_id=profile.get('gameid', None),
                   game_name=profile.get('gameextrainfo', None),
                   game_ip=profile.get('gameserverip', None))


def get_steam_account_for_name(name):
    steam_id = get_steam_id(name)

    if steam_id is None:
        return None

    return get_steam_account_for_id(steam_id)


def get_steam_account_for_id(identifier):
    profiles = get_steam_accounts_for_ids([identifier])
    return profiles[0]


def get_steam_accounts_for_ids(steam_ids):
    potential_profiles = get_steam_profiles(steam_ids)

    if potential_profiles == []:
        return []

    profiles = [build_profile(p) for p in potential_profiles]
    return profiles


@shared_task
def update_profiles():
    profiles = Profile.objects.all()
    length = len(profiles)
    num_requests = (length / 99) + 1

    for i in range(0, num_requests):
        lower_limit = i * 100
        upper_limit = lower_limit + 99

        ids = [p.steam_id for p in profiles[lower_limit:upper_limit]]

        updated_profiles = get_steam_accounts_for_ids(ids)

        for updated in updated_profiles:
            profile = profiles.get(steam_id=updated.steam_id)
            profile.game_id = updated.game_id
            profile.game_ip = updated.game_ip
            profile.game_name = updated.game_name
            profile.save()
