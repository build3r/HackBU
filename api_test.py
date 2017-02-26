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
            #for person in response['friends']['data']:
            #    print(person['name'])
            print(json.dumps(response, sort_keys=True, indent=4))

            # extract the name and current selling price from Json for the top item
        else:
            print('Error: {0}'.format(r))


if __name__ == '__main__':
    # ebay
    url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=RobinLi-HackBU-SBX-16c385072-25a053d6&GLOBAL-ID=EBAY-US&RESPONSE-DATA-FORMAT=JSON&callback=_cb_findItemsByKeywords&REST-PAYLOAD&keywords=Dell%20Laptops&itemFilter.paramName=Currency&itemFilter.paramValue=USD&itemFilter.value=true&paginationInput.entriesPerPage=3'
    # facebook
    #url = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cfriends%7Bname%2Ceducation%2Clikes%7Babout%2Ccategory%2Cname%2Cdisplay_subtext%2Cgeneral_info%2Cgenre%2Ccompany_overview%7D%2Cbirthday%7D&access_token=EAACEdEose0cBAN7gkHYqNO3BnEXoKk2nZCFOHNZC7crvAUWzmU6zZA7DdSZABm2nvz8ZAZAMPPo3ZC42ESGyQxhq2QFzGiYLA1smfSar2golM7bZAUHuABY3t80MQjSqC20xdexoJBAjOW3NswkfoVzFOe2EokDXI1Fh48T9F90AnZCZB9adaB3d0UxJSjD1CZCI6cZD'
    t = Api(url)
    t.get_response()
