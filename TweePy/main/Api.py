import tweepy


class APITwitterClass():
    def __init__(self):
        API_KEY = 'J7oizhk4hRPxbCfgxbbrwe7FC'
        API_SECRET_KEY = 'S8WJtYPW2jwsAXba5NZOHR4s96VfhppD2F0VpuH6VF9SDuwOrS'
        API_ACCESS_TOKEN = '1511487882145452033-BY2Lf3y4A2EVC40HzFvGstcpbYlRho'
        API_ACCESS_TOKEN_SECRET = 'Eta8v5BsuI7npzd9BRJr1yF1FtvFAqFv4TWDORJmcBEpv'
        self.auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        self.auth.set_access_token(API_ACCESS_TOKEN, API_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(self.auth)

    def GetUserInfo(self, name):
        userInfo = name
        userInfo = self.api.search_users(userInfo)[0]._json
        userInfo = {'screen_name': userInfo['screen_name'], 'description': userInfo['description'], 'followers_count': userInfo['followers_count'], 'friends_count': userInfo['friends_count']}

        return userInfo

    def GetUserTw(self, name):
        userInfo = name
        userInfo = self.api.user_timeline(screen_name=userInfo, count=10, tweet_mode='extended')
        userInfoList = []
        for tweet in userInfo:
            userInfoList.append(tweet.full_text)

        return userInfoList

