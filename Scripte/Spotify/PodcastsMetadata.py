import json
import sys


class PodcastMetadata:

    def __init__(self, filename):
        self.data_file = filename
        self.out_file = "../../data/Spotify/podcats_metadata.json"
        self.all_genres = 0
        self.all_shows = set()
        self.all_episodes = 0

        self.relevant_genres = {"Business News": None, "Daily News": None, "News": None,
                                "news": None, "Sports News": None, "Tech News": None}
        self.relevant_shows = {}
        self.relevant_episodes = 0

    def read_data(self):
        with open(self.data_file, 'r') as file:
            data = json.load(file)

            for genre in data:
                # count all genres, shows and episodes
                self.all_genres += 1
                for key in data:
                    for show in data[key]["shows"]:
                        if show not in self.all_shows:
                            self.all_shows.add(show)
                            self.all_episodes += data[key]["shows"][show]["episodes"]

                # count all relevant genres, shows and episodes
                if genre in self.relevant_genres:
                    self.relevant_genres[genre] = data[genre]
                    for show in data[genre]["shows"]:
                        if show in self.relevant_shows:
                            # this just means the show has two genres that are relevant
                            print("Duplicate for ", show)
                        else:
                            self.relevant_shows[show] = data[genre]["shows"][show]

            for show in self.relevant_shows:
                self.relevant_episodes += self.relevant_shows[show]["episodes"]

            self.write_data()

    def write_data(self,):
        with open(self.out_file, 'w') as metadata:
            json.dump({"total_genres": self.all_genres,
                       "total_shows": len(self.all_shows),
                       "total_episodes": self.all_episodes,
                       "relevant_genres": {"total": len(self.relevant_genres),
                                           "genres": self.relevant_genres},
                       "relevant_shows": {"total": len(self.relevant_shows),
                                          "shows": sorted(list(self.relevant_shows))},
                       "relevant_episodes": self.relevant_episodes},
                      metadata,
                      indent=2)


# ------------ MAIN -------------
def main():
    """
    Argument 1: file that contains all genres with meta infos (here: "../../data/Spotify/genres.json")
    """
    metadata = PodcastMetadata(sys.argv[1])
    metadata.read_data()


if __name__ == '__main__':
    main()
