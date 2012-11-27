'''
Created on 16.07.2012

@author: olfronar
'''
from bot.sn_api import TwitterApi


class SimpleBot(object):

    def __init__(self):
        self.api = TwitterApi()

    def do_daily_things(self):
        """
        Posting message from top.
        Follow our followers.
        Follow random people who posts trend messages
        """
        top = self.api.top
        self.api.send_message(top[1])
        self.api.follow_followers()
        who_to_follow = self.api.who_to_follow
        for user_id in who_to_follow:
            self.api.follow(user_id)