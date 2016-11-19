from urllib2 import Request, urlopen, URLError
import json

print("Test")

class api():

    def __init__(self):
        print("test1")

    def GetTopStories(self):
        try:
            stories = self.GetURL('https://hacker-news.firebaseio.com/v0/topstories.json')
            return stories
        except URLError, e:
            return int(1)

    def GetItem(self, story_id):
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

    def GetJobStories(self):
        try:
            jobs = self.GetURL('https://hacker-news.firebaseio.com/v0/jobstories.json')
            return jobs
        except URLError, e:
            return int(1)

    def GetShowStories(self):
        try:
            show_stories = self.GetURL('https://hacker-news.firebaseio.com/v0/showstories.json')
            return show_stories
        except URLError, e:
            return int(1)

    def GetAskStories(self):
        try:
            ask_stories = self.GetURL('https://hacker-news.firebaseio.com/v0/askstories')
            return ask_stories
        except:
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
