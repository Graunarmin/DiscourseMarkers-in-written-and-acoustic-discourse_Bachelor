import feedparser


def get_genre(rss_link):
    """
    Returns a list of tags (genres) of the show
    https://pythonhosted.org/feedparser/reference-feed-tags.html
    """

    feed_info = read_rss(rss_link)
    tags = []
    if feed_info:
        if hasattr(feed_info, "tags"):
            for ctr, tag in enumerate(feed_info.tags):
                tags.append(feed_info.tags[ctr].term)
    return tags


def get_description(rss_link):
    feed = read_rss(rss_link)
    if hasattr(feed, "summary"):
        return feed.summary
    else:
        return "none"


def read_rss(rss_link):
    """
    Reads rss feed from link and returns the 'feed' field,
    a dictionary of data about the feed
    https://pythonhosted.org/feedparser/reference-feed.html
    """
    # print(rss_link)
    news_feed = feedparser.parse(rss_link)
    # print(news_feed.feed)
    return news_feed.feed
