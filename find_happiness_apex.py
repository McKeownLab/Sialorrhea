import os
import cv2
import csv
from deepface import DeepFace
import shutil

def find_string_in_files(directory, search_string):

    for file in os.listdir(directory):
        if search_string in file:
            return True
        
    return False



    # Return False if the string was not found in any file
    return False
def find_peak_smile_frame_in_all_folders(root_source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Iterate through each sub-folder in the root source folder
    for folder_name in os.listdir(root_source_folder):
        source_folder = os.path.join(root_source_folder, folder_name)
        if find_string_in_files(destination_folder, folder_name):
            print(f"Processed {folder_name}...")
            continue
        if os.path.isdir(source_folder):  # Make sure it's a folder
            
            highest_smile_score = 0
            peak_smile_frame = None
            print(f"Processing {folder_name}...")
            # Iterate through each file in the current source folder
            for filename in os.listdir(source_folder):
                if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
                    try:
                        # Construct the full file path
                        file_path = os.path.join(source_folder, filename)
                        

                        # Analyze the facial expression in the image
                        analysis = DeepFace.analyze(img_path=file_path, actions=['emotion'])

                        # Check if the 'happy' score is the highest we've seen
                        smile_score = analysis[0]['emotion']['happy']
                        if smile_score > highest_smile_score:
                            highest_smile_score = smile_score
                            peak_smile_frame = file_path

                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

            # If a peak smile frame was found, copy it to the destination folder with a new name
            if peak_smile_frame:
                # Construct new filename as [folder_name]_[original_filename]
                new_filename = f"{folder_name}_{os.path.basename(peak_smile_frame)}"
                new_file_path = os.path.join(destination_folder, new_filename)
                shutil.copy(peak_smile_frame, new_file_path)
                print(f"Peak smile frame '{peak_smile_frame}' copied to '{new_file_path}'.")

# Define your root source folder where all sub-folders are located
root_source_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\Facial Asymmetry\\csv\\booth_txt_happy\\aligned'
# Define the destination folder where you want to copy the peak smile frames
destination_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\sialorrhea\\max_happiness'

# Execute the function
find_peak_smile_frame_in_all_folders(root_source_folder, destination_folder)
