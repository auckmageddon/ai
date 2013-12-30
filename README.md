# ai
ai started life as the "Auckmageddon Intranet", a minimal webapp for helping to manage a LAN party.  Since that event
died, it's been exhumed for Ping Zero.  I'll have to think of a clever new name.

It has a very minimal feature set.  Currently, it provides:

 * The ability to post news
 * A schedule of events
 * The ability to embed Challonge tournaments

Shortly, it will also support listing the games attendees are currently playing (thanks to Steam!).  We'll roll in new
features over time, but we're trying to keep the feature set contained (but well implemented) to begin with.

## Setup
ai is built in Python 2.7 and Django.  Assuming you have a basic Python environment setup already (including
virtualenv), you can get ready for development using:

    virtualenv env --no-site-packages --distribute
    source env/bin/activate
    pip install -r requirements.txt

This project is configured along Heroku's design guidelines.  The settings.py file isn't really worth editing; instead,
check `.env` to change anything for your environment.  By default, everything's configured to run straight from your
checkout.

Once the environment is ready, you should be able to get up and running using:

    honcho run python manage.py syncdb # or foreman, forego, etc.
    honcho run python manage.py migrate
    honcho start

The virtualenv includes [honcho] for your convenience, but you can use whatever tool you like here.

We use sqlite in development, rather than postgres, to avoid database setup.  However, it's probably a better idea to
just use postgres.

[honcho]: https://github.com/nickstenning/honcho
