import streamlit as st
import pickle
import pandas as pd


#Define a Function, same as recommend in Jupyter NoteBook
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
    return recommended_movies

#Used Pickle Library to dump the movies data from Jupyter to Pycharm
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

#Gives Title to the App
st.title('Movie Recommender System')

#Gives you a Select Box, to select options
selected_movie_name = st.selectbox(
'Which Movie would you like to Watch?',
    movies['title'].values)

#Build a button for recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
















