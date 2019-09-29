#!/bin/python
import tweepy
import time
import argparse
from configparser import ConfigParser

def quiet_print(message, silenced):
	if not silenced:
		print(message)

def main(args, conf):

	auth = tweepy.OAuthHandler(conf['consumer']['key'], conf['consumer']['secret'])
	auth.set_access_token(conf['access']['token'], conf['access']['secret'])

	api = tweepy.API(auth)

	while True:
		try:
			finished = 0
			if not args['no_unfollow'] or len(api.friends()) > 0:
				quiet_print('unfollowing...', args['quiet'])
				for friend in api.friends():
					api.destroy_friendship(friend.id, friend.screen_name)
			else:
				finished += 1
			
			if not args['no_block'] or len(api.followers()) > 0:
				quiet_print('blocking...', args['quiet'])
				for follower in api.followers():
					api.create_block(follower.id, follower.screen_name)
			else:
				finished += 1
			
			if not args['no_delete_tweets'] or len(api.user_timeline()) > 0:
				quiet_print('deleting tweets...', args['quiet'])
				for tweet in api.user_timeline():
					api.destroy_status(tweet.id)
			else:
				finished += 1

			if finished >= 3:
				quiet_print('finished', args['quiet'])
				break
		
		except tweepy.error.RateLimitError:
			quiet_print('Sleeping for 10 minutes...', args['quiet'])
			time.sleep(10 * 60)

if __name__ == '__main__':
	# parse arguments for options
	parser = argparse.ArgumentParser(description='Clean up twitter account')
	parser.add_argument('--no-block', action='store_true', default=False, help='disable blocking followers')
	parser.add_argument('--no-unfollow', action='store_true', default=False, help='disable unfollowing accounts you follow')
	parser.add_argument('--no-delete-tweets', action='store_true', default=False, help='disable deleting tweets')
	parser.add_argument('--quiet', '-q', action='store_true', default=False, help='silence output')
	args = vars(parser.parse_args())

	# parse configuration for twitter credentials
	conf = ConfigParser()
	conf.read('credentials.ini')
	
	main(args, conf)
