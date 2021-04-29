# Porter-AMA

This is a webhook bot which uses [PRAW](https://praw.readthedocs.io/en/latest/) to monitor a user's comments (in this case, Porter) and sends them to a channel on Discord via a webhook.

# Getting started

- Make sure you have Python installed. In this case, I am using 3.8.3.

- `pip install discord` - Installs the Discord package to give us an easy way to send data through webhooks.
- `pip install praw` - Installs the PRAW library for communicating with reddit.

- Create a new app on [Reddit](https://old.reddit.com/prefs/apps/). In this case it's just a script.
- Edit the values in `ama.py` so that they contain the app's ID as well as its `client_secret`!
- Run `python ama.py` from the command line!
