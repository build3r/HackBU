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

            # ebay
            #response = response['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][0]['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']
            # for person in response['friends']['data']:
            #     print(person['name'])
            #     try:
            #         edu = person['education']
            #         # print(json.dumps(edu, sort_keys=True, indent=4))
            #         for school in edu:
            #             # print(json.dumps(school, sort_keys=True, indent=4))
            #             if school['type'] == 'College':
            #                 print(school['school']['name'])
            #     except KeyError:
            #         pass
            #         print(json.dumps(response, sort_keys=True, indent=4))
            print(json.dumps(response, sort_keys=True, indent=4))

            # extract the name and current selling price from Json for the top item
        else:
            print('Error: {0}'.format(r))


if __name__ == '__main__':
    # ebay
    #url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=RobinLi-HackBU-SBX-16c385072-25a053d6&GLOBAL-ID=EBAY-US&RESPONSE-DATA-FORMAT=JSON&callback=_cb_findItemsByKeywords&REST-PAYLOAD&keywords=adventure%20club&itemFilter.paramName=Currency&itemFilter.paramValue=USD&itemFilter.value=true&paginationInput.entriesPerPage=1'
    # facebook
    url = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cfriends%7Bname%2Ceducation%2Cbirthday%2Clikes%7Bcategory%2Cname%7D%7D&access_token=EAACEdEose0cBAFo6LQmEcYE9O8aL5l2THSgT0hIyj8NCBwIKYCoIemrSt5G2WtBG0joIv0df5bAjHZBoBtDXr8wZAPEUy9uT7dn5zq9MruW24R2K8gY1UuuBpVylu7CSXCRw6WGkL47vqWBhEWOWfNpGFomWkwV1xeRAKnua1vrUa4Cr7ZCFYsEeOnSFa8ZD'
    #url = 'https://graph.facebook.com/v2.8/1631357656880896/likes?access_token=EAACEdEose0cBABwNqxhpl9kVHembkKfp0yQ42q1zpZCMM8H01muXFh8Yiqf0ENZCTUiZADwsqZC822iw9JfTgPnyjhkHZBAZBqURnlSN6ZChvmKqIw6K6XUnLuqNgtM3p8ueFwtOS0JeNZA8t5egEAnKAgAemTnkrs4uCaTAqIEYkPcImp7H7IubZB3snF1NOXt8ZD&fields=category%2Cname&limit=25&after=ODUyMTEzMjk0ODA4MTM1'
    t = Api(url)
    t.get_response()
