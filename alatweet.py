# -*- coding: utf-8 -*-
# ALA Talk generator

# from several data files of programs from ALA Annual Conference
# 2016-18, which have been split into potential beginnings and endings,
# creates a new talk maship

import random, string
import tweepy
from alacredentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():

    infile = open('ala_beginners.txt','r')
    bdata = infile.readlines()
    infile.close()

    infile = open('ala_enders.txt','r')
    edata = infile.readlines()
    infile.close()

    beginners = [line[:-1] for line in bdata]
    enders = [line[:-1] for line in edata]

    lenb = len(beginners)
    lene = len(enders)

    first= beginners[random.randrange(1, lenb)]
    second = enders[random.randrange(1, lene)]

    line = first + ' ' + second
    print line
        
    api.update_status(line)

main()
