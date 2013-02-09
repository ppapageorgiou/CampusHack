from django.db import models

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

	hash_tag  = models.ForeignKey(HashTag, related_name="tags")
	sender    = models.CharField(max_length=50)
	tweet     = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.tweet