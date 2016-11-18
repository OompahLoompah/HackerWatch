from api import api
import json

hn = api()

story_ids = hn.PullTopStories()

for story_id in story_ids:
    story = hn.PullStoryEntry(story_id)
    if story == int(1):
        exit(1)
    else:
        try:
            print story['title'].encode('ascii', 'ignore')
        except UnicodeEncodeError, e:
            print("\n\n\n\nWe choked on the following story:\n")
            print story
