string_films = '''
Barking Dogs Never Bite 2000 106
The Host 2006 119
Memories of Murder 2003 131
Mother 2009 128
Okja 2017 120
Parasite 2019 132
Snowpiercer 2013 126
Tokyo! 2008 107
'''

tuple_films= [("Movie Title", "Year Released", "Running Time"),
              ("Barking Dogs Never Bite", 2000, 106),
              ("The Host", 2006, 119),
              ("Memories of Murder", 2003, 131),
              ("Mother", 2009, 128),
              ("Okja", 2017, 120),
              ("Parasite", 2019, 132),
              ("Snowpiercer",2013, 126),
              ("Tokyo!", 2008, 107)]
class Films:
    def _init_(self, movie_title: str, year_released: str, running_time: int):
        self.title = movie_title
        self.year = year_released
        self.time = running_time
