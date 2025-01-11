import requests
import random

def fetch_movies_by_genre(genre_id):
    API_KEY = 'YOUR_API_KEY'  # O'zingizning The Movie Database kalitingizni kiriting
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        return movies
    else:
        print('Failed to retrieve data:', response.status_code)
        return []

def recommend_movie(genre):
    genre_dict = {
        'action': 28,
        'comedy': 35,
        'drama': 18,
        'fantasy': 14,
        'horror': 27,
        'science fiction': 878,
        'romance': 10749
    }

    genre_id = genre_dict.get(genre.lower())
    
    if genre_id:
        movies = fetch_movies_by_genre(genre_id)
        if movies:
            recommended_movie = random.choice(movies)
            title = recommended_movie['title']
            overview = recommended_movie['overview']
            
            print(f'Recommended Movie: {title}')
            print(f'Overview: {overview}')
        else:
            print('No movies found for this genre.')
    else:
        print('Genre not recognized.')

user_genre = input('Please enter a movie genre (action, comedy, drama, fantasy, horror, science fiction, romance): ')
recommend_movie(user_genre)