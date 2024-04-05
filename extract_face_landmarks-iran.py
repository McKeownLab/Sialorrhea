import subprocess
import cv2
import dlib
import numpy as np
import pandas as pd
import os

#set parameters
# Path to the video file
video_path = 'D:\Codes\Python\FacialAsymmetry\data\working\\aligned\HC'
# Path to the csv folder
csv_folder = 'D:\Codes\Python\FacialAsymmetry\data\working\csv-landmarks\HC'

# Initialize dlib's face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("OpenFace_2.2.0/shape_predictor_68_face_landmarks.dat")

def extract_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        # Flatten the landmarks into a single list alternating x and y
        return [coord for p in landmarks.parts() for coord in (p.x, p.y)]
    return []

def process_video(video_path):
    
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    csv_filename = f'{video_name}_landmarks.csv'
    csv_filename = os.path.join(csv_folder, csv_filename)
    if os.path.exists(csv_filename):
        print(f'File already exists: {csv_filename}')
        return

    frame_landmarks = []
    frame_count = 0

    # List all files in the folder and sort them
    image_files = [f for f in os.listdir(video_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()  # Make sure to sort files if necessary

    for image_file in image_files:
        frame_path = os.path.join(video_path, image_file)
        frame = cv2.imread(frame_path)
        
        # No need to check for 'ret' here since we're not reading from a video capture
        landmarks = extract_landmarks(frame)
        if landmarks:
            # Add frame number as the first element
            frame_landmarks.append([frame_count] + landmarks)
        frame_count += 1

    # Convert landmarks to DataFrame
    header = ['frame'] + [f'{i}_{axis}' for i in range(0, 68) for axis in ['x', 'y']]
    df = pd.DataFrame(frame_landmarks, columns=header)
    
    # Check if CSV file already exists
    if not os.path.exists(csv_filename):
        df.to_csv(csv_filename, index=False)
        print(f'Saved: {csv_filename}')


def process_videos_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        video_path = os.path.join(folder_path, filename)
        process_video(video_path)

# Example usage
# Example usage

process_videos_in_folder(video_path)