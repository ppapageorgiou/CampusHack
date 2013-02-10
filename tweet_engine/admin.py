from django.contrib import admin
from tweet_engine.models import HashTag, Tweet, Achievement

admin.site.register(HashTag)
admin.site.register(Tweet)
admin.site.register(Achievement)