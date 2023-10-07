import pandas as pd
import pickle
import streamlit as st
import requests


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in movies_list:

           recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_recommendation = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
selected_movie_recommendation
)

if st.button('Rocommend'):
    recommendation=recommend(selected_movie)
    for i in recommendation:
        st.write(i)