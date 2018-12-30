from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Comment

# It is a good practice to use HyperlinkedModelSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'username', 'email', 'content', 'created')

'''
from datetime import datetime

class Comment(object):
    def __init__(self, username,email, content, created=None):
        self.username = username
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(username="leila7", email='leila@example.com', content='foo bar')

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer = CommentSerializer(comment)
print(serializer.data)

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print(json)
'''