
import os
import pickle
from requests_oauthlib import OAuth1Session

request_token_url = 'https://{}/api/oauth/request_token.php'
access_token_url = 'https://{}/api/oauth/access_token.php'
authorization_base_url = 'https://{}/oauth/authorize.php'


def authorize(auth_type, host, client_key, client_secret):
    if auth_type == 'direct_access':
        return DirectAccessAuth(host, client_key, client_secret)
    elif auth_type == 'user_token':
        return UserTokenAuth(host, client_key, client_secret),
    else:
        raise Exception('auth_type {} not understood. Should be [direct_access, user_token]'.format(auth_type))


class DirectAccessAuth:
    def __init__(self, host, client_key, client_secret):
        self.host = host
        self.client_key = client_key
        self.client_secret = client_secret
        self.auth = OAuth1Session(client_key, client_secret)


class UserTokenAuth:
    def __init__(self, host, client_key, client_secret, save_auth=True, auth_file='auth.pkl'):
        self.host = host
        self.client_key = client_key
        self.client_secret = client_secret
        if os.path.exists(auth_file):
            self.auth = self.load_pickle_auth(auth_file)
        elif save_auth:
            self.auth = self.get_user_token_auth()
            self.save_auth(auth_file)
        else:
            self.auth = self.get_user_token_auth()

    def get_user_token_auth(self):
        oauth = OAuth1Session(self.client_key, self.client_secret, callback_uri='http://localhost:8080/accesstoken.html')
        oauth.fetch_request_token(request_token_url.format(self.host))

        authorization_url = oauth.authorization_url(authorization_base_url.format(self.host))
        print('Please go here and authorize,', authorization_url)

        oauth.parse_authorization_response(input("Enter the url: "))
        oauth.fetch_access_token(access_token_url.format(self.host))
        return oauth

    def load_pickle_auth(self, filename):
        oauth = OAuth1Session(self.client_key, self.client_secret, callback_uri='http://localhost:8080/accesstoken.html')
        oauth.auth = pickle.load(open(filename, 'rb'))
        return oauth

    def save_auth(self, filename):
        pickle.dump(self.auth.auth, open(filename, 'wb'))
