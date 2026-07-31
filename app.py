import streamlit as st
import pickle
import nltk
import sklearn
import joblib

st.title("movie Recommmendation System")

with open('movies.pickle', 'rb') as f:
    movies = pickle.load(f)

similarity = joblib.load('similarities.joblib')
movie_names=movies['title'].values

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

name_movie=st.selectbox("enter the movie name",movie_names)

if st.button("Recommend"):
    recommended_movies = recommend(name_movie)
    st.write("The recommended movies are:")
    for movie in recommended_movies:
        st.write(movie)