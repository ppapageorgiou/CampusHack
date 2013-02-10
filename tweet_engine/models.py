from django.db import models
from datetime import datetime
from django.db.models.signals import post_save

class HashTag(models.Model):
	'''
	This is the base class for a Hash Tag. This table will
	hold all hash tags that will be monitored and its tweeets
	counted
	'''

	tag     = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return self.tag

class Tweet(models.Model):
	'''
	This is the model for a tweet.  We save tweets so that we 
	can count them and use their sender to offer rewards.
	'''

	hash_tag  				= models.ForeignKey(HashTag, related_name="tweets")
	sender    				= models.CharField(max_length=50)
	tweet     				= models.CharField(max_length=200)
	created_at 				= models.DateTimeField(default=datetime.now())
	entities 				= models.TextField()
	tweet_id_str 			= models.CharField(max_length=100)
	in_reply_to_screen_name = models.CharField(max_length=100)
	retweet_count 			= models.IntegerField(default=0)
	coordinates 			= models.CharField(max_length=50)

	def __unicode__(self):
		return self.tweet

class Achievement(models.Model):
	'''
	This is the model for an Achievement.  We queue rewards to be given out to the winners.
	'''

	hash_tag  			= models.ForeignKey(HashTag, related_name="achievements")
	winner    			= models.CharField(max_length=50)
	reason 				= models.CharField(max_length=300)
	url 				= models.CharField(max_length=200)
	img 				= models.CharField(max_length=200)
	discount_string 	= models.CharField(max_length=50)
	reward_name			= models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.url

def find_achievements(**kwargs):
	"""
	Analyse tweets and decide whether to give new achievements.
	"""
	if kwargs['created']:
		all_tweets = Tweet.objects.all()
		counter = Tweet.objects.all().count()
		if counter == 5:
			# create an achievement
			a = Achievement()
			a.hash_tag = kwargs['instance'].hash_tag
			a.winner = kwargs['instance'].sender
			a.reason = "Hashtag reached 5 tweets"
			a.save()
			pass

models.signals.post_save.connect(find_achievements, sender=Tweet)