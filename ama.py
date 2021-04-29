import praw
from discord import Webhook, RequestsWebhookAdapter

WEBHOOK_URL = "" # Discord Webhook URL

CLIENT_ID = "" # Reddit client_id
CLIENT_SECRET = "" # Reddit client_secret
USER_AGENT = "/u/porter_robinson comment stream bot for AMA on 4/29. v1.0" # Reddit user agent

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

print('Reddit client is watching and listening for new submissions!')

webhook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())

for comment in reddit.redditor("porter_robinson").stream.comments(skip_existing=True):
    webhook.send("/u/{}: {}\n\n/u/{}: {}".format(comment.parent().author, comment.parent().body, comment.author, comment.body))
