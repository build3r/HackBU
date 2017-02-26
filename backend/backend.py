import logging
import requests
import json

from flask import Flask
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

facebook_url = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cfriends%7Bname%2Ceducation%2Clikes%7Bcategory%2Cname%7D%2Cbirthday%7D&access_token=EAACEdEose0cBAAZAlCuCcgKxIovBglwcZCB2VCJkB10mMAaHXTraOeE4Y2NQFIEDnmKAmEEF3TfzijZB1zVZCFvypmwd7gk1JZCpsi9OguZB8gBZAPTICVSBwGb4vmFEN74yr7pfpG9HhNlGZBodkS2Va7bZAffp4hzYJfDALv8K2bqGt5OH8KZA7HjiN3Q0oG1R8ZD'
ebay_url = 'http://svcs.sandbox.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=RobinLi-HackBU-SBX-16c385072-25a053d6&GLOBAL-ID=EBAY-US&RESPONSE-DATA-FORMAT=JSON&callback=_cb_findItemsByKeywords&REST-PAYLOAD&keywords={0}&itemFilter.paramName=Currency&itemFilter.paramValue=USD&itemFilter.value=true&paginationInput.entriesPerPage=1'

not_enough_info_string = "I don't have enough info to suggest anything for {0}. Perhaps you should ask {0} yourself."


@ask.intent("GetGiftSuggestion")
def get_gifts(friend_name):
    #try:
    print('Name: {0}'.format(friend_name))
    # get info from facebook
    items_list = get_facebook_info(friend_name)

    # use facebook info to find ebay listings
    gifts_list = get_ebay_info(items_list)

    ret_string = get_nice_message(gifts_list).format(friend_name)
    return statement(ret_string).simple_card('Gift Suggester', ret_string)
    #except:
    #    conn_err_message = 'There seems to have been a connection error. Please try again later.'
    #    return statement(conn_err_message).simple_card('Gift Suggester', conn_err_message)


def get_college_info(person):
    try:
        edu = person['education']
        for school in edu:
            if school['type'] == 'College':
                school_name = school['school']['name']
                print(school_name)
                return ['college', str(school_name)]
    except KeyError:
        pass
    return []


def get_facebook_info(friend_name):
    if not friend_name:
        return None
    info = requests.get(facebook_url).json()
    people = info['friends']['data']  # list of people
    for person in people:
        if (person['name'])[:person['name'].find(' ')].lower() == friend_name.lower():
            print('Found {0}'.format(friend_name))
            likes_list = person['likes']['data']
            top_3_likes = parse_likes(likes_list)#.append(get_college_info(person))
            if not top_3_likes:
                top_3_likes = get_college_info(person)
            else:
                top_3_likes = top_3_likes.append(get_college_info(person))
            return top_3_likes
    return None


def parse_likes(likes_list):
    if not likes_list:
        return None
    sports_team = []
    book = []
    musician = []
    clothing = []
    computers = []
    for like in likes_list:
        category = like['category'].lower()
        if category == 'sports team':
            sports_team.append(['sports team', like['name']])
        elif category == 'book':
            book.append(['book', like['name']])
        elif category.find('musician') != -1:
            musician.append(['musician', like['name']])
        elif category.find('computers') != -1:
            computers.append(['computers', like['name']])
        elif category.find('clothing') != -1:
            clothing.append(['clothing', like['name']])

    likes = sports_team + book + musician + clothing + computers
    print(likes)

    i = 0
    retVal = []
    for element in likes:
        if i < 3:
            retVal.append(element)
        else:
            break
        i += 1
    print('retVal: ' + str(retVal))
    return retVal


def get_ebay_info(items_list):
    if not items_list:
        return None
    else:
        gifts_list = []
        for item in items_list:
            print("ITEM: " + str(item))
            if item[0] != 'college':
                ebay_string = ebay_url.format(get_ebay_string(item))
                ebay_info = requests.get(ebay_string).json()
                try:
                    item_price = ebay_info['findItemsByKeywordsResponse'][0]['searchResult'][0]['item'][0]['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']
                    gifts_list.append([item, str(item_price)])
                except KeyError:
                    print("Couldn't find an item matching {0} {1}".format(item[0], item[1]))
    print(gifts_list)
    return gifts_list


def get_ebay_string(item):
    category = item[0]
    name = item[1]
    retval = ''
    if category == 'sports team':
        retval = name
    else:
        retval = category + ' ' + name
    retval = retval.replace(' ', '%20')
    print(retval)
    return retval



def get_nice_message(gifts_list):
    if not gifts_list:
        return not_enough_info_string
    else:
        final_message = ''
        curr_spot = 0
        for gift in gifts_list:
            if gift[0][0] == 'sports team':
                if curr_spot == 0:
                    final_message += '{0} might like an item from the ' + gift[0][1] + '. I found one for ' + gift[1] + ' dollars on ebay.'
                else:
                    final_message += ' {0} might also like an item from the ' + gift[0][1] + '. I found one for ' + gift[1] + ' dollars on ebay.'
            elif gift[0][0] == 'book':
                if curr_spot == 0:
                    final_message += '{0} might like the book ' + gift[0][1] + '. I found a copy for ' + gift[1] + ' dollars on ebay.'
                else:
                    final_message += ' {0} might also like the book ' + gift[0][1] + '. I found a copy for ' + gift[1] + ' dollars on ebay.'
            elif gift[0][0] == 'musician':
                if curr_spot == 0:
                    final_message += '{0} might like something by ' + gift[0][1] + '. I found some merchandise for ' + gift[1] + ' dollars on ebay.'
                else:
                    final_message += ' {0} might also like something by ' + gift[0][1] + '. I found some merchandise for ' + gift[1] + ' dollars on ebay.'
            elif gift[0][0] == 'computers':
                if curr_spot != 0:
                    final_message += ' '
                final_message += 'It might be time for {0} to get some new tech. I found a ' + gift[0][1] + ' for ' + gift[1] + ' dollars on ebay.'
            elif gift[0][0] == 'clothing':
                if curr_spot != 0:
                    final_message += ' '
                final_message += 'It might be time for {0} to refresh his wardrobe. I found some apparel from ' + gift[0][1] + ' for ' + gift[1] + ' dollars on ebay.'
            elif gift[0] == 'college':
                if curr_spot != 0:
                    final_message += ' You could also get {0} some swag from their alma matter, ' + gift[1] + '.'
                else:
                    final_message += 'You might want to get {0} some swag from their alma matter, ' + gift[1] + '.'
            curr_spot += 1
        return final_message


if __name__ == '__main__':
    app.run()
