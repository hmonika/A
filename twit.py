class twitter_member(object):
    member_name = []
    member_user_id = []
    list_follower = []
    list_following = []
    list_tweets = []
    def __init__(self,name,user_id):
        self.member_name = name
        self.member_user_id = user_id
    
    def add_follower(self,twitter_member):
        self.list_follower.append(twitter_member)
        
    def show_follower(self):
        for user in range(len(self.list_follower)):
            print self.list_follower[user]
            
    def add_tweets(self,tweet):
        self.list_tweets.append(tweet)
     
    def show_tweets(self):
        for tweet in range(len(self.list_tweets)):
            print self.list_tweets[tweet]
