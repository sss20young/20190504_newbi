from django.contrib import admin
from .models import Post, Event, Schedule, Tip, Review, Like

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Schedule)
admin.site.register(Tip)
admin.site.register(Review)
admin.site.register(Like)
# Register your models here.
