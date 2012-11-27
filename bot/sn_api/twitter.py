# -*- coding: utf-8 -*-
'''
Created on 16.07.2012

@author: olfronar
'''
import tweepy

consumer_key = "yrDfCXzYwXEs1Z7ObE4yiw"
consumer_secret = "Am1Nn4Fr3asnksbyNhVlGG08vbCOMocSE9Vf8qLnn0"
access_key="628298860-V4ANGxiMOz46NRLIWkF8rzBA9Wtt0J45xXEzCNdS"
access_secret="HlSlj4ovDfYaUh4oTD7EC0UdHsspgDqrqBs6eu3tqSc"
user = "ventilaptor"


class TwitterApi(object):

    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api=tweepy.API(auth)
        self.following = [friend.id for friend in tweepy.Cursor(self.api.friends, id=user).items(100)]

    def send_message(self, twit):
        self.api.update_status(twit[:140])

    def follow(self, user_id):
        if user_id not in self.following:
            self.api.create_friendship(user_id)
            self.following.append(user_id)

    def follow_followers(self):
        followers = [friend.id for friend in tweepy.Cursor(self.api.followers).items(100)]
        for user_id in followers:
            self.follow(user_id)

    @property
    def who_to_follow(self):
        trends = self.api.trends_location(23424936)[0]['trends']
        first_trend = trends[1]["name"]
        second_trend = trends[2]["name"]
        third_trend = trends[3]["name"]
        raw = self.api.search("{} OR {} OR {}".format(first_trend,second_trend, third_trend), 
                                    lang = "ru", rpp = 5)
        return [message.from_user_id for message in raw]

    @property
    def top(self):
        raw = self.api.search("#", lang = "ru", result_type = "popular")
        return [message.text.decode("utf-8") for message in raw]
