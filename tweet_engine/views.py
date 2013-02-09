# Dependencies: pip install tweepy
from django.http import HttpResponse
import tweepy
from models import *

consumer_key = 'anCzDqH0g9Qxv46h8ecRhQ'
consumer_secret = 'LtlgzBbOMmC4BOJNnTov8o10mruPu585cPiALLOmM'

access_token = '1163067522-DjTrcFBvf9RgomZN1swvUREA6FFgJQU20ufBxis'
access_token_secret = 'J6aVMuztkOzZsMYFXZEyBBkrkBq4xXYvpVLtNlsjScY'

# OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Get HashTag from database
hash_tag = HashTag.objects.get(pk=1)

# # Get the User object for twitter...
# user = api.get_user('avocarrot')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
    	# print status.text
     	#print status.user.screen_name
		t = Tweet()
		t.hash_tag = hash_tag
		t.sender = status.user.screen_name
		t.tweet = status.text
		t.save()
		print "Another tweet into DB"

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream


# Create your views here.
def listener(request):
	sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
	sapi.filter(track=[hash_tag])

	html = "<html><body>This should never be displayed</body></html>"
	return HttpResponse(html) 

def monitor(request):
	html = "<html><body>Hello {} with {} followers.</body></html>".format(2,4)
	return HttpResponse(html) 

