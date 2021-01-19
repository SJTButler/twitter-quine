import twitter as t
from conf import *
a=t.Api(consumer_key=ck,consumer_secret=cs,access_token_key=atk,access_token_secret=ats)
with open(__file__) as f:
    a.PostUpdate(f.read())
#quine #twitterbot #python