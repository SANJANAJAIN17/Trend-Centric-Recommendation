import streamlit as st
import os
from PIL import Image
import numpy as np
import pickle
import tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm

# Load the features and image file lists
feature_list = np.array(pickle.load(open('C:/Users/Mukta/PycharmProjects/fashion_recom_system/image_features_embedding.pkl', 'rb')))
filenames = pickle.load(open('C:/Users/Mukta/PycharmProjects/fashion_recom_system/img_files.pkl', 'rb'))

# Initialize the model
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.trainable = False

model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

st.title('Fashion Recommender System')

def save_uploaded_file(uploaded_file):
    try:
        # Ensure the uploads directory exists
        if not os.path.exists("uploads"):
            os.makedirs("uploads")
            print("Created uploads directory")

        # Save the file to the desired location
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        print(f"File saved to {file_path}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def feature_extraction(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result

def recommend(features, feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)

    distances, indices = neighbors.kneighbors([features])

    return indices

uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        try:
            # Display the file
            display_image = Image.open(uploaded_file)
            st.image(display_image)
            print("Image displayed")

            # Feature extract
            features = feature_extraction(os.path.join("uploads", uploaded_file.name), model)
            print("Features extracted")

            # Recommendation
            indices = recommend(features, feature_list)
            print("Recommendations computed")

            # Show recommendations
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.image(filenames[indices[0][0]])
                if st.button('Try On', key='1'):
                    st.write(f'Trying on: {filenames[indices[0][0]]}')

            with col2:
                st.image(filenames[indices[0][1]])
                if st.button('Try On', key='2'):
                    st.write(f'Trying on: {filenames[indices[0][1]]}')

            with col3:
                st.image(filenames[indices[0][2]])
                if st.button('Try On', key='3'):
                    st.write(f'Trying on: {filenames[indices[0][2]]}')

            with col4:
                st.image(filenames[indices[0][3]])
                if st.button('Try On', key='4'):
                    st.write(f'Trying on: {filenames[indices[0][3]]}')

            with col5:
                st.image(filenames[indices[0][4]])
                if st.button('Try On', key='5'):
                    st.write(f'Trying on: {filenames[indices[0][4]]}')

            print("Recommendations displayed")
        except Exception as e:
            st.header("An error occurred while processing the image")
            print(f"Error processing the image: {e}")
    else:
        st.header("Some error occurred in file upload")
else:
    print("No file uploaded")
