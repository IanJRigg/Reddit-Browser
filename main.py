import configparser
import praw

import sqlite3
from sqlite3 import Error



def parse_config_file():
    config = configparser.ConfigParser()
    config.read("secrets.cfg")
    return config


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as error:
        print(error)

    # If the database can't be made, exit
    exit()


def search_reddit():
    config = parse_config_file()

    bot = praw.Reddit(user_agent    = config["DEFAULT"]["UserAgent"],
                      client_id     = config["DEFAULT"]["ClientID"],
                      client_secret = config["DEFAULT"]["ClientSecret"],
                      username      = config["DEFAULT"]["Username"],
                      password      = config["DEFAULT"]["Password"])

    subreddit = bot.subreddit(config["PARAMETERS"]["Subreddit"]);

    term = config["PARAMETERS"]["SearchTerm"].lower()

    conn = create_connection(config["PARAMETERS"]["SQLiteFile"])

    for submission in subreddit.hot(limit=10):

        submission.comments.replace_more(limit=0)

        for comment in submission.comments:
            text = comment.body.lower()

            if term in text:
                print(text)

    print(count)

if __name__ == '__main__':
    search_reddit()