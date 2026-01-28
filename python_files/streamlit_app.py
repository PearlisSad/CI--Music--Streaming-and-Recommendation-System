# Python Environments
import numpy as np
import pandas as pd
import ast

# Streamlit Environments
import streamlit as st

# Tensor Flow Environments
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, Flatten, Dropout, BatchNormalization, GlobalAveragePooling1D, concatenate
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from neural_network_functions import process_genres, prepare_numeric_features, build_get_embeddings, recommend_by_song

data = pd.read_csv("../datasets/sam_df_clean.csv")

# create new df with additional genre column and adding integer columns for genre ids
genre_df = process_genres(data)

# Create the dropdown in the sidebar
st.sidebar.title("Select a Song")
song_names = genre_df['track_name'].tolist()  # convert to list
selected_song = st.sidebar.selectbox("Choose a song:", song_names)
st.write(f"You selected: {selected_song}") # Display the selected song name

# Save mapping from song Id to row index (needed for recommendations later)
song_ids = genre_df['track_id'].values
id2index = {sid: idx for idx, sid in enumerate(song_ids)}
index2id = {idx: sid for sid, idx in id2index.items()}

# prepare numeric features
X_numeric_sound_profile_input, scaler = prepare_numeric_features(genre_df)

# build model and get id->embedding mapping
model, all_embeddings, id2embedding = build_get_embeddings(genre_df, X_numeric_sound_profile_input, song_ids)

# Get recommendations
song_id = genre_df.loc[genre_df['track_name'] == selected_song, 'track_id'].values[0]
recommendations = recommend_by_song(genre_df,song_id, k=5, id2index=id2index, index2id=index2id, all_embeddings=all_embeddings)
recs_df = pd.DataFrame(recommendations) # Convert results to DataFrame for better viewing in Streamlit

# Display the recommendations as a table in the Streamlit app
st.title('Song Recommendations')
st.table(recs_df)