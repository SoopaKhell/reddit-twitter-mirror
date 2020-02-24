import json
def getConfig():
    try:
        with open("config.json", 'r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        with open("config.json", 'w') as f:
            print("You need to fill out the config.json file with your keys.")
            f.write("""{\n\t"subreddit": "SUBREDDIT_HERE",\n\t"twitter_api_key": "TWITTER_API_KEY_HERE",\n\t"twitter_api_secret": "TWITTER_API_SECRET_HERE",\n\t"twitter_access_token": "TWITTER_ACCESS_TOKEN_HERE",\n\t"twitter_access_token_secret": "TWITTER_ACCESS_TOKEN_SECRET_HERE",\n\t"reddit_client_id": "REDDIT_CLIENT_ID_HERE",\n\t"reddit_client_secret": "REDDIT_CLIENT_SECRET_HERE",\n\t"reddit_password": "REDDIT_PASSWORD_HERE",\n\t"reddit_username": "REDDIT_USERNAME_HERE",\n\t"reddit_user_agent": "REDDIT_USER_AGENT_HERE"\n}""")
            exit(1)