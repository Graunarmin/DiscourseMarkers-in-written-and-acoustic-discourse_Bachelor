import json
import RssReader as rss


class ShowDescription:
    """
    retrieve the show description of relevant shows to further confirmation of their relevance
    """

    def __init__(self):
        self.metadata = "../../data/Spotify/podcast_metadata.json"
        self.link_data = "../../data/Spotify/rss_links.json"
        self.outfile = "../../data/Spotify/show_descriptions.json"
        self.news_shows = {}
        self.read_data()

    def read_data(self):
        with open(self.metadata, 'r') as metadata:
            data = json.load(metadata)
            for show in data["relevant_shows"]["shows"]:
                self.news_shows[show] = {}
            del data

        with open(self.link_data, 'r') as linkdata:
            data = json.load(linkdata)
            for show in data:
                if show in self.news_shows:
                    self.news_shows[show] = data[show]

    def get_description(self):
        for show in self.news_shows:
            description = rss.get_description(self.news_shows[show]["rss_link"])
            self.news_shows[show]["description"] = description

        self.write_data()

    def write_data(self):
        with open(self.outfile, 'w') as out:
            json.dump(self.news_shows,
                      out,
                      indent=2)


# ------------ MAIN -------------
def main():
    description = ShowDescription()
    description.get_description()


if __name__ == '__main__':
    main()
