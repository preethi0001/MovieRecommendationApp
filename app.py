import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

movies_dict= pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title("Movie Recommendations")
selected_movie=st.selectbox('select the movie',movies['title'].values)
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for recommended_movie in recommended_movie_names:
        st.title(recommended_movie)
