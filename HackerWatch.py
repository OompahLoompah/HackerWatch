from urllib2 import Request, urlopen, URLError
import json, time

def PullTopStories():
    get = Request('https://hacker-news.firebaseio.com/v0/topstories.json')

    time.sleep(1)
    try:
        response = urlopen(get)
        top_stories = json.loads(response.read())
        return top_stories
    except URLError, e:
        print 'Connection failed: ', e
        return int(1)

def PullStoryEntry(story_id):
    get = Request('https://hacker-news.firebaseio.com/v0/item/' + str(story_id) + '.json')
    
    time.sleep(1)
    try:
        response = urlopen(get)
        story = json.loads(response.read())
        return story
    except URLError, e:
        print 'Story connection failed: ', e
        return int(1)

story_ids = PullTopStories()

for story_id in story_ids:
    story = PullStoryEntry(story_id)
    if story == int(1):
        exit(1)
    else:
        try:
            print story['title'].encode('ascii', 'ignore')
        except UnicodeEncodeError, e:
            print("\n\n\n\nWe choked on the following story:\n")
            print story
