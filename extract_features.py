import pandas as pd
import numpy as np
import os

# Path to the folder containing landmarks CSV files
landmarks_csv_folder = 'Z:\\Video Assessment_Atefeh\\sialorrhea\\landmarks_csv'
# Path to the features definition file
features_definition_path = '.\\csv\\Features_facial_video_analysis.csv'
# Path to the folder where the features CSV files will be saved
features_csv_folder = 'Z:\\Video Assessment_Atefeh\\sialorrhea\\features_csv'

# Ensure the output folder exists
os.makedirs(features_csv_folder, exist_ok=True)

# Load the features definition
features_definition = pd.read_csv(features_definition_path)

def calculate_feature(landmarks, feature_info):
    # Extract indices from the feature_info (subtract 1 for zero-based indexing)
    index1, index2 = [int(x) for x in feature_info.split(', ')]
    # Calculate the Euclidean distance between two landmarks
    dist = np.sqrt((landmarks[index1*2] - landmarks[index2*2])**2 + (landmarks[index1*2+1] - landmarks[index2*2+1])**2)
    return dist

def process_landmarks_file(csv_file_path):
    # Load the landmarks CSV
    df_landmarks = pd.read_csv(csv_file_path)

    features_data = []

    for _, row in df_landmarks.iterrows():
        features_row = [row['frame']]
        for _, feature_row in features_definition.iterrows():
            feature_number = feature_row['Feature']
            landmark_indices = feature_row['Landmarks']
            if landmark_indices is np.nan:
                break
            feature_value = calculate_feature(row[1:], landmark_indices)
            features_row.append(feature_value)
        features_data.append(features_row)

    # Save the features into a new CSV file
    features_df = pd.DataFrame(features_data, columns=['frame'] + [f'feature_{x}' for x in range(1, len(features_definition)+1)])
    output_file_name = os.path.basename(csv_file_path).replace('_landmarks', '_features')
    output_file_path = os.path.join(features_csv_folder, output_file_name)
    features_df.to_csv(output_file_path, index=False)
    print(f'Saved features to {output_file_path}')

def process_all_landmarks_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('_landmarks.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            process_landmarks_file(csv_file_path)

process_all_landmarks_files(landmarks_csv_folder)
