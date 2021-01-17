import hashlib
from db import put_db, get_db

from googlesearch import search


class Bot:
    __instance = None

    @staticmethod
    def getObject(name):
        if Bot.__instance is None:
            Bot()
        return Bot.__instance

    def __init__(self, name):
        if Bot.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.name = name
            Bot.__instance = self

    # fetch google link based on the data as google search key
    # using google lib for fetching data
    # return the list of links
    def get_google_link(self, data):
        query = data
        links = [] #tld="co.in"
        for j in search(query, num=5, stop=5, pause=2):
            links.append(j+'\n')

        return "TOP Five Links are :\n" + "".join(links)

    # set google history in db
    # We split the sentence into words and store the value as sentence in it
    # for example $google game thrones
    # key = game, thrones, game of throne
    # value = game of throne
    # we create hash of key for fast retrieval
    def set_history(self, data):
        orginal = data
        data = data.lower()
        data = data.split()
        for d in data:
            result = hashlib.sha1(d.encode())
            key = result.hexdigest()
            put_db(key, orginal)

        result = hashlib.sha1(orginal.lower().encode()).hexdigest()
        put_db(result, orginal)
    # get the response from the incoming message
    # income message have $google,$recent or basic conversation message

    def get_response(self, message):
        if message.startswith('$google'):
            message = message.replace('$google', '')
            res = self.get_google_link(message)
            # set the history for the search google term
            self.set_history(message)
            return res

        # get history of recent searches
        if message.startswith('$recent'):
            message = message.replace('$recent', '')
            # cleaning of incoming message
            message = message.lower()
            message = message.replace(' ', '')
            # convert the incoming message to sha digest for fetching value from redis cache
            message_hex = hashlib.sha1(message.encode()).hexdigest()
            resp = get_db(message_hex)
            return resp

        # basic hi conversation
        message = message.lower().replace('$','')
        if message in ['hello', 'hi', 'How are you', 'hi' ]:
            return "Hi" 

        if message in ["what is your name",'name']:
        	return "my name is".format(self.name)

        return "Please ask again, Thanks for understanding"


