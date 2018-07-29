# Reddit Browser
The following project is a basic search utility for reddit. The end goal is provide a database of links to comments with a specified search term, on a specified subreddit.


## Design:
The system is composed of two parts: a reddit bot written in Python using PRAW, and a Node.js API which utilizes the Express framework. The bot is used to search for a user defined set of keywords. Finding those posts, the data from those posts is then placed into a sqlite database. That database is then exposed via a REST API as paginated JSON.

## Configuration:
The Reddit bot is configured via a file called secrets.cfg, it must be defined in your copy of the project. The file use Python's configparser module and an example is listed below:

``` ini
[DEFAULT]
UserAgent = Unique Name For A Bot That Is Definitely Unique
ClientID = 123456789ABCDEF
ClientSecret = 123456789ABCDEF
Username = test
Password = password

[PARAMETERS]
SearchTerm = Test
Subreddit = all
```

Several parameters are required for the Bot to work correctly with Reddit. Those are the UserAgent, the ClientID, and the ClientSecret. Additionally a username and password are required to register those three parameters with Reddit itself.

Finally, you must specify the term to search for, and the subreddit to find them in.

## TODO:
1. Get the configuration mechanism working
2. Register a Reddit Bot
3. Get read/write access to the database working
4. Start populating the bot
5. Ensure that the database is getting populated
6. Initialize the express project
7. Create the pagination SQL
8. Tie in the routes to the API