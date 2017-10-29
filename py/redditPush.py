from time import sleep
import requests
import praw
import json
import re

def postWebhook(msg):

    discord_url = "https://discordapp.com/api/webhooks/374301350961348619/Tls23TCT2y115XnCJ0ciSFC90LJoevQXYzsrQLEWUX_Ot80MvsQLcYIZRLTBP9EVta-l"

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


