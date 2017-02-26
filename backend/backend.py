import logging
import requests
import json

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

facebook_url = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cfriends%7Bname%2Ceducation%2Clikes%7Babout%2Ccategory%2Cname%2Cdisplay_subtext%2Cgeneral_info%2Cgenre%2Ccompany_overview%7D%2Cbirthday%7D&access_token=EAACEdEose0cBAN7gkHYqNO3BnEXoKk2nZCFOHNZC7crvAUWzmU6zZA7DdSZABm2nvz8ZAZAMPPo3ZC42ESGyQxhq2QFzGiYLA1smfSar2golM7bZAUHuABY3t80MQjSqC20xdexoJBAjOW3NswkfoVzFOe2EokDXI1Fh48T9F90AnZCZB9adaB3d0UxJSjD1CZCI6cZD'

not_enough_info_string = "I don't have enough info to suggest anything for {0}. Perhaps you should ask {0} yourself."


@ask.intent("GetGiftSuggestion")
def get_gifts(friend_name):
    print('Name: {0}'.format(friend_name))
    # get info from facebook
    items_list = get_facebook_info(friend_name)

    # use facebook info to find ebay listings
    gifts_dict = get_ebay_info(items_list)

    ret_string = get_nice_message(gifts_dict).format(friend_name)
    return statement(ret_string).simple_card('Gift Suggestion', ret_string)


def get_facebook_info(friend_name):
    if not friend_name:
        return None
    info = requests.get(facebook_url).json()
    people = info['friends']['data']  # list of people
    for person in people:
        if (person['name'])[:person['name'].find(' ')].lower() == friend_name.lower():
            print('Found {0}'.format(friend_name))
            likes_list = person['likes']['data']
            top_3_likes = parse_likes(likes_list)
            return top_3_likes
    return None


def parse_likes(likes_list):
    if not likes_list:
        return None
    else:
        return None

def get_ebay_info(items_list):
    if not items_list:
        return None
    else:
        return None # [{1: 10}, {2: 20}, {3: 30}]


def get_nice_message(gifts_dict):
    if not gifts_dict:
        return not_enough_info_string
    else:
        return None

if __name__ == '__main__':
    app.run()
