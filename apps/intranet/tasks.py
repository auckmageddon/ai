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


def get_steam_profile(id):
    r = requests.get(PLAYER_INFO_URL.format(KEY, id))
    if r.ok:
        return r.json()['response']['players'][0]


def get_useful_steam_data(profile):
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

    profile_data = get_steam_profile(steam_id)

    if profile_data is None:
        return None

    profile = get_useful_steam_data(profile_data)
    return profile


def get_steam_account_for_id(steam_id):
    profile_data = get_steam_profile(steam_id)

    if profile_data is None:
        return None

    profile = get_useful_steam_data(profile_data)
    return profile

def update_profiles():
    profiles = Profile.objects.all()
    length = len(profiles)
    num_requests = (length / 99) + 1
    

    for profile in profiles:
        p = get_steam_account_for_id(profile.steam_id)
        profile.__dict__.update(p.__dict__)
        profile.save()
