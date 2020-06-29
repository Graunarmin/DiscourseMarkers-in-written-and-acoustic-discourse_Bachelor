import feedparser


class RssReader:
    """
    Reads the rss feed of a given link
    Can return a list of genres of that feed
    """

    def __init__(self):
        self.feed_info = []

    def read_rss(self, rss_link):
        news_feed = feedparser.parse(rss_link)
        self.feed_info = news_feed.feed

    def get_genre(self):
        """
        Returns a list of tags (genres) of the show
        https://pythonhosted.org/feedparser/reference-feed-tags.html
        """
        tags = []
        for tag in self.feed_info.tags:
            tags.append(self.feed_info.tags[tag].term)
        return tags


def main():
    reader = RssReader("https://anchor.fm/s/cf7b7a8/podcast/rss")
    reader.get_genre()


if __name__ == '__main__':
    main()
