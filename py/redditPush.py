#https://github.com/skandix/ListentoThisSite/blob/dca35fcd0d13f65c597fb16f388ce315f7728a42/modules/reddit.py#L62-L76
# Use oysteins method to store post id's in files.. #ggez
import requests
import praw
import json

def postWebhook(msg):

    discord_url = "<Webook>"

    headers = {
        'User-Agent': 'usenetinvite',
        'Content-Type': 'application/json',
    }

    hooker = {
        'content': msg
    }

    msg = json.dumps(hooker)
    res = requests.post(url=discord_url, data=msg, headers=headers)

    return res

def reddit(thread):
    r = praw.Reddit(client_id=""
                    ,client_secret=""
                    ,user_agent="usenetNotif")
    sub = r.subreddit(thread)
    for k in sub.new():
        if "[O]" in  k.title:
            msg = "\nTitle: {0:s}\nURL: {1:s}".format(k.title, k.url)
            postWebhook(msg)

reddit('UsenetInvites')
