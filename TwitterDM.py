#!/usr/bin/env python
import tweepy, time, sys
try:
   import cPickle as pickle
except:
   import pickle
'''
Message to be sent via bot
'''
MESSAGE = "INSERT HERE"

ACCESS_KEY = 0
ACCESS_SECRET = 0
CONSUMER_KEY = ''#Get on your own
CONSUMER_SECRET = ''

# RUNNING:
# ---------------------------------------------x        
if __name__=="__main__":
	
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth_url = auth.get_authorization_url()
	print 'Visit this URL with the script still running to authorize application: ' + auth_url
	verifier = raw_input('PIN: ').strip()
	auth.get_access_token(verifier)
	print "ACCESS_KEY = '%s'" % auth.access_token.key
	print "ACCESS_SECRET = '%s'" % auth.access_token.secret
	
	ACCESS_KEY = auth.access_token.key
	ACCESS_SECRET = auth.access_token.secret
	
	f1 = file('auth.pkl', 'wb')
	pickle.dump(ACCESS_KEY,f1,True)
	pickle.dump(ACCESS_SECRET,f1,True)
	f1.close()
	print "Application authenticated. Monitoring followers."
	
	api = tweepy.API(auth)
	
	try:
		f3 = file('followers.pkl', 'rb')
		print "rb"
		oldFollowers = pickle.load(f3)
	except:
		f3 = file('followers.pkl', 'wb')
		print "wb"
		oldFollowers = api.followers_ids()
		
	f3.close()
	
	while True:
		
		f3 = file('followers.pkl', 'wb')
		
		new_followers = []
		
		try:
			api = tweepy.API(auth)
		except:
			print "unauthorized"
			
		newFollowers = api.followers_ids()
	
		for follower in newFollowers:
			if (not follower in oldFollowers):
				api.send_direct_message(user_id = follower, text = MESSAGE)
				print "Sending"
			
		oldFollowers = newFollowers
		
		try:
			pickle.dump(oldFollowers,f3)
		except:
			print "write error"
		f3.close()
		time.sleep(600)
		
	
	
	
    
