
# Define your root source folder where all sub-folders are located
import os
import shutil


root_source_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\Facial Asymmetry\\csv\\booth_txt_happy\\aligned'
# Define the destination folder where you want to copy the peak smile frames
destination_first_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\sialorrhea\\first_neutral'
destination_last_folder = '\\\\files.ubc.ca\\team\\PPRC\\Camera\\Video Assessment_Atefeh\\sialorrhea\\last_neutral'

#get the first frame in folder and move it to the destination folder
def get_first_frame_in_all_folders(root_source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Iterate through each sub-folder in the root source folder
    for folder_name in os.listdir(root_source_folder):
        source_folder = os.path.join(root_source_folder, folder_name)
        if os.path.isdir(source_folder):  # Make sure it's a folder
            print(f"Processing {folder_name}...")
            # Iterate through each file in the current source folder
            for filename in os.listdir(source_folder):
                if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
                    try:
                        # Construct the full file path
                        file_path = os.path.join(source_folder, filename)
                        # Construct new filename as [folder_name]_[original_filename]
                        new_filename = f"{folder_name}_{os.path.basename(file_path)}"
                        new_file_path = os.path.join(destination_folder, new_filename)
                        shutil.copy(file_path, new_file_path)
                        print(f"First frame '{file_path}' copied to '{new_file_path}'.")
                        break
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

def get_last_frame_in_all_folders(root_source_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Iterate through each sub-folder in the root source folder
    for folder_name in os.listdir(root_source_folder):
        source_folder = os.path.join(root_source_folder, folder_name)
        if os.path.isdir(source_folder):  # Make sure it's a folder
            print(f"Processing {folder_name}...")
            # Iterate through each file in the current source folder
            files = os.listdir(source_folder)
            #sort in decrease order the list of files
            files.reverse()
            for filename in files:
                if filename.endswith(".jpg") or filename.endswith(".png"):  # Check for image files
                    try:
                        # Construct the full file path
                        file_path = os.path.join(source_folder, filename)
                        # Construct new filename as [folder_name]_[original_filename]
                        new_filename = f"{folder_name}_{os.path.basename(file_path)}"
                        new_file_path = os.path.join(destination_folder, new_filename)
                        shutil.copy(file_path, new_file_path)
                        print(f"Last frame '{file_path}' copied to '{new_file_path}'.")
                        break
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")

#get_first_frame_in_all_folders(root_source_folder, destination_first_folder)

get_last_frame_in_all_folders(root_source_folder, destination_last_folder)