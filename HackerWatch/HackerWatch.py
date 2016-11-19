#!/usr/bin/python

from api import api
import optparse, time, json

parser = optparse.OptionParser()
parser.add_option('-t', '--top', help='Get the top stories', dest='top', default=False, action='store_true')
parser.add_option('-s', '--show', help='Get show Hacker News stories', dest='show', default=False, action='store_true')
parser.add_option('-j', '--jobs', help='Get job postings', dest='jobs', default=False, action='store_true')
parser.add_option('-i', '--item', help='Get a single item', dest='item')
parser.add_option('-u', '--user', help='Get user information', dest='user')

(opts, args) = parser.parse_args()

hn = api()

if opts.top:
    story_ids = hn.GetTopStories()

    for story_id in story_ids:
        story = hn.GetItem(story_id)
        if story == int(1):
            exit(1)
        else:
            try:
                print story['title'].encode('ascii', 'ignore')
            except UnicodeEncodeError, e:
                print("\n\n\n\nWe choked on the following story:\n")
                print story
        time.sleep(1)

if opts.show:
    story_ids = hn.GetShowStories()

    for story_id in story_ids:
        story = hn.GetItem(story_id)
        if story == int(1):
            exit(1)
        else:
            try:
                print story['title'].encode('ascii', 'ignore')
            except UnicodeEncodeError, e:
                print("\n\n\n\nWe choked on the following story:\n")
                print story
        time.sleep(1)

if opts.jobs:
    story_ids = hn.GetJobStories()

    for story_id in story_ids:
        story = hn.GetItem(story_id)
        if story == int(1):
            exit(1)
        else:
            try:
                print story['title'].encode('ascii', 'ignore')
            except UnicodeEncodeError, e:
                print("\n\n\n\nWe choked on the following story:\n")
                print story
        time.sleep(1)

if opts.item:
    item = hn.GetItem(opts.item)
    if item == int(1):
        print('Invalid ID')
    else:
        print item

if opts.user:
    user = hn.GetUser(opts.user)
    print user
