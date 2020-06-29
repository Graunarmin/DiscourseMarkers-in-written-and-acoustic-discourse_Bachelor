import feedparser


def get_genre(rss_link):
    """
    Returns a list of tags (genres) of the show
    https://pythonhosted.org/feedparser/reference-feed-tags.html
    """

    feed_info = read_rss(rss_link)
    tags = []
    for tag in feed_info.tags:
        tags.append(feed_info.tags[tag].term)
    return tags


def read_rss(rss_link):
    """
    Reads rss feed from link and returns the 'feed' field,
    a dictionary of data about the feed
    https://pythonhosted.org/feedparser/reference-feed.html
    """
    news_feed = feedparser.parse(rss_link)
    return news_feed.feed
