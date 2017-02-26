import requests
import json


DEBUG = True


class Api(object):
    def __init__(self, url_):
        self.URL = url_
        # self.auth_header = (username, password)
        # print(url_)

    def get_response(self):
        h = {'X-EBAY-SOA-SECURITY-APPNAME':'RobinLi-HackBU-SBX-16c385072-25a053d6', 'X-EBAY-SOA-OPERATION-NAME':'findItemsByKeywords'}
        d = {"mimeType": "application/x-www-form-urlencoded; charset=UTF-8", "text": "path=http%3A%2F%2Fsvcs.sandbox.ebay.com%2Fservices%2Fsearch%2FFindingService%2Fv1&headers=X-EBAY-SOA-SECURITY-APPNAME%3ARobinLi-HackBU-SBX-16c385072-25a053d6%0D%0AX-EBAY-SOA-OPERATION-NAME%3AfindItemsByKeywords&body=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E%0D%0A%3CfindItemsByKeywordsRequest+xmlns%3D%22http%3A%2F%2Fwww.ebay.com%2Fmarketplace%2Fsearch%2Fv1%2Fservices%22%3E%0D%0A++%3Caffiliate%3E%0D%0A++++%3CnetworkId%3E9%3C%2FnetworkId%3E%0D%0A++++%3CtrackingId%3E1234567890%3C%2FtrackingId%3E%0D%0A++++%3CcustomId%3Ek-man%3C%2FcustomId%3E%0D%0A++%3C%2Faffiliate%3E%0D%0A++%3CsortOrder%3EEndTime%3C%2FsortOrder%3E%0D%0A++%3CpaginationInput%3E%0D%0A++++%3CentriesPerPage%3E4%3C%2FentriesPerPage%3E%0D%0A++%3C%2FpaginationInput%3E%0D%0A++%3Ckeywords%3EDell+Laptops%3C%2Fkeywords%3E%0D%0A%3C%2FfindItemsByKeywordsRequest%3E%0D%0A&method=POST&api=finding&call=findItemsByKeywords&variation=xml", "params": [{"name": "path","value": "http%3A%2F%2Fsvcs.sandbox.ebay.com%2Fservices%2Fsearch%2FFindingService%2Fv1"},{"name": "headers","value": "X-EBAY-SOA-SECURITY-APPNAME%3ARobinLi-HackBU-SBX-16c385072-25a053d6%0D%0AX-EBAY-SOA-OPERATION-NAME%3AfindItemsByKeywords"},"name": "body","value": "%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E%0D%0A%3CfindItemsByKeywordsRequest+xmlns%3D%22http%3A%2F%2Fwww.ebay.com%2Fmarketplace%2Fsearch%2Fv1%2Fservices%22%3E%0D%0A++%3Caffiliate%3E%0D%0A++++%3CnetworkId%3E9%3C%2FnetworkId%3E%0D%0A++++%3CtrackingId%3E1234567890%3C%2FtrackingId%3E%0D%0A++++%3CcustomId%3Ek-man%3C%2FcustomId%3E%0D%0A++%3C%2Faffiliate%3E%0D%0A++%3CsortOrder%3EEndTime%3C%2FsortOrder%3E%0D%0A++%3CpaginationInput%3E%0D%0A++++%3CentriesPerPage%3E4%3C%2FentriesPerPage%3E%0D%0A++%3C%2FpaginationInput%3E%0D%0A++%3Ckeywords%3EDell+Laptops%3C%2Fkeywords%3E%0D%0A%3C%2FfindItemsByKeywordsRequest%3E%0D%0A"},{"name": "method","value": "POST"},{"name": "api","value": "finding"},{"name": "call","value": "findItemsByKeywords"},{"name": "variation","value": "xml"}]}
        r = requests.post(self.URL, data = d)
        # print(r.status_code)
        if r.status_code == requests.codes.ok:
            response = r.json()
            print(json.dumps(response, sort_keys=True, indent=4))
        else:
            print('Error: {0}'.format(r))


if __name__ == '__main__':
    #url = 'https://graph.facebook.com/v2.8/me?access_token=EAACEdEose0cBAAqRnJugzWPKFI3ZBcdIuADvZCPSZBc4OFiBCFen5ZC9wlnwVRjtMvyMwo5R6EAwF4tLL45oRITVKibDbUpoKrU04g318YESWhkFZCayv5ZCbcZAkDZAJLXCFnWhWIa3eXZCaZBpT3cHaJaEmv1hbAW8mAyCMv46z1xZBHmKcO83dBGb5nuY5btRfUZD&debug=all&fields=id%2Cname%2Clikes&format=json&method=get&pretty=0&suppress_http_code=1'
    # url = 'https://graph.facebook.com/v2.8/me?access_token=EAACEdEose0cBAB0PlN0TUIZBVPsg1MENWG6B7CkHx96UFZBd2zCJVlkr6CypEG7OJbfpIiU4tgWaMnIF2PEyWxwgZBpIJbCGIF3kzLOZB67NnPhh806Q9Cyp3YcqCFpmgJ2JgCIEiFxnhvE1mMI5seCZCfxL695xLu3NCTXPH8jLmYBuKaTUHDpcK5bjOhBkZD&debug=all&fields=id%2Cname%2Clikes%2Cfriends%7Blikes%7D&format=json&method=get&pretty=0&suppress_http_code=1'
    url = 'http://developer.ebay.com/invoke_api'

    t = Api(url)
    t.get_response()
