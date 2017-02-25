import requests
import json
import sys


DEBUG = True


class Api(object):
    def __init__(self, url_):
        self.URL = url_
        # self.auth_header = (username, password)
        # print(url_)

    def get_response(self):
        r = requests.get(self.URL)#auth=self.auth_header)
        # print(r.status_code)
        if r.status_code == requests.codes.ok:
            response = r.json()
            print(json.dumps(response, sort_keys=True, indent=4))
        else:
            print('Error: {0}'.format(r))


if __name__ == '__main__':
    url = ''

    t = Api(url)
    t.get_response()
