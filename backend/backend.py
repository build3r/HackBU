import logging
import requests
import json

from flask import Flask
from flask_ask import Ask, statement, question, session


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent("GetGiftSuggestion")
def get_gifts(FriendName):

    ret_string = 'You should get {0} nothing'.format(FriendName)
    return statement(ret_string).simple_card('Gift Suggestion', ret_string)

if __name__ == '__main__':
    app.run()
