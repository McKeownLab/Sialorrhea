import os
import cv2
import numpy as np
import pandas as pd
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("OpenFace_2.2.0/shape_predictor_68_face_landmarks.dat")
#for a folder with multiple images of face extract face landmarks using dlib next step is to extract features from the landmarks and return the features as a dataframe
features_definition_path = '.\\csv\\ten_feature_new.csv'
# Load the features definition
features_definition = pd.read_csv(features_definition_path)

def calculate_feature(landmarks, feature_info):
    # Extract indices from the feature_info (subtract 1 for zero-based indexing)
    index1, index2 = [int(x) for x in feature_info.split(', ')]
    # Calculate the Euclidean distance between two landmarks
    dist = np.sqrt((landmarks[index1*2] - landmarks[index2*2])**2 + (landmarks[index1*2+1] - landmarks[index2*2+1])**2)
    return dist

def extract_features(folder_path):
    features = []
    
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            # extract face landmarks using dlib
            landmarks = extract_landmarks(image_path)
            # extract features from the landmarks
            features.append(extract_features_from_landmarks(landmarks))
            # add the filename to the features
            features[-1].insert(0, filename)
    
    # create a dataframe from the extracted features
    df = pd.DataFrame(features)
    return df

def extract_landmarks(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        # Flatten the landmarks into a single list alternating x and y
        return [coord for p in landmarks.parts() for coord in (p.x, p.y)]
    return []

def extract_features_from_landmarks(landmarks):
    features_data = []
    
    for _, feature_row in features_definition.iterrows():
        feature_number = feature_row['Feature']
        landmark_indices = feature_row['Landmarks']
        if landmark_indices is np.nan:
            break
        feature_value = calculate_feature(landmarks, landmark_indices)
        features_data.append(feature_value)
    return features_data

# example usage
destination_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\sialorrhea\\max_happiness'
df = extract_features(destination_folder)
# save df to csv file
destination_csv = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\sialorrhea\\features_10_max_happiness_v2.csv'
df.to_csv(destination_csv, index=False)