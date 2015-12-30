'''
Created on Dec 22, 2015
@author: hanhanwu
Get the data from blog posts
'''
import feedparser
import json

def stripHTML(h):
    p = ''
    s = 0
    for c in h:
        if c == '<':
            s = 1
        elif c == '>':
            p += ' '
            s = 0
        elif s == 0:
            p += c
    return p

def main():
    URL = 'http://feeds.feedburner.com/oreilly/radar/atom'
    fp = feedparser.parse(URL)
    
    print '%d entries from: %s ' % (len(fp.entries[0].title), fp.feed.title)
    
    posts = []
    for e in fp.entries:
        posts.append({'title': e.title, 'content': stripHTML(e.content[0].value), 'link': e.links[0].href})
    
    f_path = 'feed.json'
    f = open(f_path, 'w')
    f.write(json.dumps(posts, indent = 1))
    f.close()
    
if __name__ == '__main__':
    main()
