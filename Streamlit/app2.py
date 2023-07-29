import streamlit as st
import pandas as pd

df = pd.read_csv('cleaned_movies.csv')

def recommend_movies(df, actor_name, genre=None, num_movies=5):
    actor_movies = df[(df['actor/actress'] == actor_name) & (df['type'] == 'movie')]

    if genre:
        actor_movies = actor_movies[actor_movies['genres'].str.contains(genre, na=False)]

    return actor_movies.sort_values(by='rating', ascending=False).head(num_movies)

def recommend_same_genre(df, title, num_movies=5):
    movie_genre = df[df['title'] == title]['genres'].values[0]

    same_genre_movies = df[(df['type'] == 'movie') & (df['genres'].str.contains(movie_genre, na=False))]

    return same_genre_movies.sort_values(by='rating', ascending=False).head(num_movies)

st.image('https://img.freepik.com/free-vector/realistic-horizontal-cinema-movie-time-poster-with-3d-glasses-snacks-tickets-clapper-reel-blue-background-with-bokeh-vector-illustration_1284-77013.jpg?w=2000', width=700)

st.markdown('<style>body {background-color: darkgreen;}</style>',unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Let Gladys pick a movie for you</h1>", unsafe_allow_html=True)

#Usser entries
option = st.selectbox('What would you like to do?', ['Recommend movies by actor', 'Recommend movies of the same genre'])
actor_name = st.text_input('Enter the name of an actor') if option == 'Recommend movies by actor' else ''
genre = st.text_input('Enter a genre (optional)') if option == 'Recommend movies by actor' else ''
title = st.text_input('Enter a movie title') if option == 'Recommend movies of the same genre' else ''

if st.button('What will you watch ?'):
    if option == 'Recommend movies by actor':
        result = recommend_movies(df, actor_name, genre)
        st.dataframe(result)
    elif option == 'Recommend movies of the same genre':
        result = recommend_same_genre(df, title)
        st.dataframe(result)