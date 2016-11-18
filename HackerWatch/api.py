from urllib2 import Request, urlopen, URLError
import json, time

print("Test")

class api():

    def __init__(self):
        print("test1")

    def PullTopStories(self):
        get = Request('https://hacker-news.firebaseio.com/v0/topstories.json')

        time.sleep(1)
        try:
            response = urlopen(get)
            top_stories = json.loads(response.read())
            return top_stories
        except URLError, e:
            print 'Connection failed: ', e
            return int(1)

    def PullStoryEntry(self, story_id):
        get = Request('https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json')

        time.sleep(1)
        try:
            response = urlopen(get)
            story = json.loads(response.read())
            return story
        except URLError, e:
            print 'Story connection failed: ', e
            return int(1)
