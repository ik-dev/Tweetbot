import urllib2
from bs4 import BeautifulSoup


def get_source(url):
    return urllib2.urlopen(url).read()


def get_tree(source):
    return BeautifulSoup(source, 'html.parser')


def get_tweets(tree):
    para = tree.findAll('p', {'class': 'TweetTextSize'})
    for p in para:
        print p.text


source = get_source('https://twitter.com/thequote/')
tree = get_tree(source)
get_tweets(tree)
