import requests
import json


DEBUG = True


class Api(object):
    def __init__(self, url_):
        self.URL = url_
        # self.auth_header = (username, password)
        # print(url_)

    def get_response(self):

        r = requests.get(self.URL)
        # print(r.status_code)
        if r.status_code == requests.codes.ok:
            response = r.json()
            print(json.dumps(response, sort_keys=True, indent=4))
        else:
            print('Error: {0}'.format(r))


if __name__ == '__main__':
    # facebook
    # url = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cfriends%7Beducation%2Clikes%7Babout%2Ccategory%2Cname%2Cdisplay_subtext%2Cgeneral_info%2Cgenre%2Ccompany_overview%7D%7D&access_token=EAACEdEose0cBANVKu4kuhHu9xkvE0DfThGU4YZCwpEBQ3LlgZCxDBxyJ2VbUzYRqOhpGZCxO1rJtR5JKiyQp0MkdFzMTVvV4IPEWS41ZCbv6WGsPcaBz0fjjv5t93VYl8wPsZALxe8dNriT3sX58J3nNXcsKjodStZCyNhZAcxbR7VHwJeNi7ZC8ZCqgnGZCZCWweAZD'
    # ebay
    url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=RobinLi-HackBU-SBX-16c385072-25a053d6&GLOBAL-ID=EBAY-US&RESPONSE-DATA-FORMAT=JSON&callback=_cb_findItemsByKeywords&REST-PAYLOAD&keywords={0}&paginationInput.entriesPerPage=3'.format('cleveland%20cavaliers')
    t = Api(url)
    t.get_response()
