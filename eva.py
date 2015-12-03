import urllib2
from bs4 import BeautifulSoup


def get_source(url):
    """
    Read the html source from the url provided.
    """
    return urllib2.urlopen(url).read()


def get_tree(source):
    """
    Prepares the tree object out of html source
    """
    return BeautifulSoup(source, 'html.parser')


def print_tweets(tree):
    """
    Crawls through the twitter source and fetches tweets
    """
    para = tree.findAll('p', {'class': 'TweetTextSize'})
    for p in para:
        print p.text


if __name__ == '__main__':
    source = get_source('https://twitter.com/thequote/')
    tree = get_tree(source)
    print_tweets(tree)
