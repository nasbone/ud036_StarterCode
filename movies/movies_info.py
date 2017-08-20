'''
Movie metadata was generated using TMDB API (please see https://developers.themoviedb.org/3/getting-started). 
Program to pull the data was implemented using a python wrapper module for the TMDB API called tmdbsimple 
(please see https://github.com/celiao/tmdbsimple).

Below is a snippet of the python code used to generate the metadata below:

import tmdbsimple as tmdb

tmdb.API_KEY = "put your API key here"
movies = tmdb.Movies()
now_playing_movies = movies.now_playing()

#creates a list of movie instances prepopulated with movie metadata using list comprehension
list_of_movies = [movie.Movie(movie_info, tmdb.Movies(i['id']).videos()['results'][0]['key']) 
                                                for movie_info in now_playing_movies['results']]

#creates a dictionary list of movie metadata
for i in list_of_movies_with_videos:
    list_of_movies.append({'title':i.title, 'poster':i.poster, 'trailer' : i.trailer})
'''

import fresh_tomatoes, movie

#a list of movie metadata of current movies in theaters stored within a dictionary data structure
list_of_movies = [
  {
    'poster': u'https://image.tmdb.org/t/p/w500/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg',
    'trailer': u'rk-dF1lIbIg',
    'title': u'Spider-Man: Homecoming'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/5qcUGqWoWhEsoQwNUrtf3y3fcWn.jpg',
    'trailer': u'euz-KBBfAAo',
    'title': u'Despicable Me 3'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/tb86j8jVCVsdZnzf8I6cIi65IeM.jpg',
    'trailer': u'KisPhy7T__Q',
    'title': u'Annabelle: Creation'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/bOXBV303Fgkzn2K4FeKDc0O31q4.jpg',
    'trailer': u'PC460OxDNhc',
    'title': u'Dunkirk'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/i9GUSgddIqrroubiLsvvMRYyRy0.jpg',
    'trailer': u'GjwfqXTebIY',
    'title': u'The Dark Tower'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/tp9SBVBvouRipujcx0Q793R3ik2.jpg',
    'trailer': u'FnCdOQsX5kc',
    'title': u'It'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/7iFEupKRt0dwciHQI1Dt2j3OVxn.jpg',
    'trailer': u'Anps6VPe0u8',
    'title': u"The Hitman's Bodyguard"
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/wUYUvQylUdQckQLDV8SmTQBJaNm.jpg',
    'trailer': u'aPzvKH8AVf0',
    'title': u'Logan Lucky'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/qyXPqzlCWf3T9VEpBtquUQZwsgi.jpg',
    'trailer': u'864zcREOnzg',
    'title': u'King Arthur'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/8dTWj3c74RDhXfSUZpuyVNJrgS.jpg',
    'trailer': u'AEBIJRAkujM',
    'title': u'American Made'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/dzqEq8Jbvb5SYGoYPqLyIRrt6Cm.jpg',
    'trailer': u'8R0yLRoevnA',
    'title': u'Starship Troopers'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/mux8YnLQK3pTA3sRDG7kDRlCVf3.jpg',
    'trailer': u'UBf3JKdcoEo',
    'title': u'Bobby'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/6HE4xd8zloDqmjMZuhUCCw2UcY1.jpg',
    'trailer': u'eyKOgnaf0BU',
    'title': u'Baywatch'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/kV9R5h0Yct1kR8Hf8sJ1nX0Vz4x.jpg',
    'trailer': u'HNKX2Ymfhbg',
    'title': u'Atomic Blonde'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/8L7FE3bXjN98BcmKANzrL9WwKsK.jpg',
    'trailer': u'y0n1cdoaiZE',
    'title': u'Valerian'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/11MVxyp77zUPwc4cmqsUumNQYWK.jpg',
    'trailer': u'L-591Dqa48g',
    'title': u'Patti Cake$'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/dN9LbVNNZFITwfaRjl4tmwGWkRg.jpg',
    'trailer': u'UfoWyZvDCEc',
    'title': u'Baby Driver'
  },
  {
    'poster': u'https://image.tmdb.org/t/p/w500/qLmLz2wtyYvmW8Ult3l2ngOnW8v.jpg',
    'trailer': u'Xm157yQ7g1E',
    'title': u'Shot Caller'
  }
]

#using list comprehension to create a list of movie instances prepopulated with the data from the list of dictionaries above
movies = [movie.Movie(movie_info) for movie_info in list_of_movies]

#creates and renders a webpage filled with the movies from the list provided above.
fresh_tomatoes.open_movies_page(movies)

