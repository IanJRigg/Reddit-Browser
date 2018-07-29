import configparser
import praw

import sqlite3
from sqlite3 import Error

config = configparser.ConfigParser()

config.read("secrets.cfg")

userAgent = config["DEFAULT"]["UserAgent"]
clientID = config["DEFAULT"]["ClientID"]
clientSecret = config["DEFAULT"]["ClientSecret"]
username = config["DEFAULT"]["Username"]
password = config["DEFAULT"]["Password"]

bot = praw.Reddit(user_agent = userAgent,
                  client_id  = clientID,
                  client_secret = clientSecret,
                  username = username,
                  password = password)

subreddit = config["PARAMETERS"]["Subreddit"]
term = config["PARAMETERS"]["SearchTerm"]


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as error:
        print(error)

    return None