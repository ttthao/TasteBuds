from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def token(client_id='', client_secret='', callback_url='', request_url=''):
    # client = BackendApplicationClient(client_id=client_id)
    # yelp = OAuth2Session(client=client)
    # access_token = yelp.fetch_token(token_url='https://api.yelp.com/oauth2/token', 
    #                                 client_id=client_id, 
    #                                 client_secret=client_secret)
    # tokenstring = str(token)
    # accesstok = re.findall(r"'access_token': u'(.*?)', ",tokenstring)
    # authhead = "Bearer " + accesstok[0]
    # head = {'Authorization': authhead}

    path = 'https://api.yelp.com/oauth2/token'
    yelp_session = OAuth2Session(client_id)
    access_token = yelp_session.fetch_token(path,
                                client_secret=client_secret,
                                code=path,
                                authorization_response=path)
    return access_token

client_id = 'yncucN0peQa4V7SheHiC5Q'
client_secret = 'hdLmWEMfOTcG6VMtIeuZJ7cXOAtgEYRQH2YnHFmiibtye6GkU7nFfoESzxI0MHYk'

tokenObj = token(client_id=client_id, client_secret=client_secret)

# print str(tokenObj)

# token = json.loads(str(tokenObj))

print tokenObj