import os
import shutil
import subprocess
# Connect to shared drive, use drive letter M get username and password from environment variables
username = os.environ.get('CWL_USERNAME')
password = os.environ.get('CWL_PASS')
subprocess.call(f'net use J: \\\\files.ubc.ca\\team\\PPRC\\Camera /user:ead\\{username} {password}', shell=True)
base_directory = 'J:/CAMERA Booth Data/Booth/' 
dest_directory = 'J:/Video Assessment_Atefeh/booth_txt_disgust/'
import os
import shutil

def copy_videos(src_directory, dest_directory):
    # Iterate over each user's folder in the source directory
    users =0
    for user_id in os.listdir(src_directory):
        user_path = os.path.join(src_directory, user_id)
        users +=1
        # Check if it's a directory (to handle user folders)
        if os.path.isdir(user_path):
            
            # Iterate over each timestamp folder in the user's folder
            for timestamp in os.listdir(user_path):
                timestamp_path = os.path.join(user_path, timestamp)
                # Check if it's a directory (to handle timestamp folders)
                if os.path.isdir(timestamp_path):
                    
                    face_path = os.path.join(timestamp_path, 'facial_expression')
                    face_path = os.path.join(face_path, 'text')
                    # Check if the 'finger_tapping' folder exists
                    if os.path.isdir(face_path):
                        # Copy all videos in the 'finger_tapping' folder
                        for video in os.listdir(face_path):
                            video_path = os.path.join(face_path, video)
                            # Check if it's a file (to handle only video files)
                            if os.path.isfile(video_path) and video_path.endswith('facial_expression_disgust.mp4'):
                                new_name = f"{user_id}_{timestamp}_{video}"
                                dest_path = os.path.join(dest_directory, new_name)
                                if not os.path.exists(dest_path):
                                    shutil.copy(video_path, dest_path)
                                    print(f"Copying {video_path} to {dest_path}")

copy_videos(base_directory, dest_directory)
