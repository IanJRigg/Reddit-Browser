import configparser
import praw

import sqlite3
from sqlite3 import Error


# SQL Statements
create_table_command = """ CREATE TABLE IF NOT EXISTS posts (
                               ID INTEGER PRIMARY KEY AUTOINCREMENT,
                               post TEXT NOT NULL
                           ); """

insert_post_command = """ INSERT INTO posts(post) VALUES(?);"""



def parse_config_file():
    config = configparser.ConfigParser()
    config.read("../secrets.cfg")
    return config


def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_command)
    except Error as error:
        print(error)

def insert_post(conn, comment):

    try:
        cursor = conn.cursor()
        cursor.execute(insert_post_command, (comment.body, ));
    except Error as error:
        print(error)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        create_tables(conn)
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

    for submission in subreddit.hot(limit=25):

        # Remove the more commments comment (requires another API hit)
        submission.comments.replace_more(limit=0)

        for comment in submission.comments:
            text = comment.body.lower()

            if term in text:
                insert_post(conn, comment)


if __name__ == '__main__':
    search_reddit()