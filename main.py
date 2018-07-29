import configparser

config = configparser.ConfigParser()

config.read("secrets.cfg")

print(config.sections())

print(config["DEFAULT"]["Username"])

userAgent = config["DEFAULT"]["UserAgent"]
clientID = config["DEFAULT"]["ClientID"]
clientSecret = config["DEFAULT"]["ClientSecret"]
username = config["DEFAULT"]["Username"]
password = config["DEFAULT"]["Password"]

print(userAgent, clientID, clientSecret, username, password)

