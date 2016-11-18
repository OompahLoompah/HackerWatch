from urllib2 import Request, urlopen, URLError
import json

print("Test")

class api():

    def __init__(self):
        print("test1")

    def PullTopStories(self):
        try:
            stories = self.GetURL('https://hacker-news.firebaseio.com/v0/topstories.json')
            return stories
        except URLError, e:
            return int(1)

    def PullItem(self, story_id):
        try:
            item = self.GetURL('https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json')
            return item
        except URLError, e:
            return int(1)

    def GetUser(self, user_id):
        try:
            user = self.GetURL('https://hacker-news.firebaseio.com/v0/user/' + user_id + '.json')
            return user
        except URLError, e:
            return int(1)

    def GetURL(self, url):
        get = Request(url)

        try:
            response = urlopen(get)
            data = json.loads(response.read())
            return data
        except URLError, e:
            print 'Connection failed: ', e
            return int(1) 
