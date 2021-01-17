# discord_bot
  Bot have three functionality:
	1. Hi Hello message
	2. $google <querry> --> search querry on google, return top 5 links.
	3. $recent querry --> To check the history of the google search.


Language: Python 3.8
Database : Redis cache [for storing history in Redis]
config : config.json

{
"discord" :
{
  "token" : BOT_TOKE_ID
},
  "redis":{

    "host":HOST_URL,
    "password" : PASSWORD,
    "port" : PORT_NUMBER

  }

}
