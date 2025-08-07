# Sialorrhea Analysis

This repository contains a pipeline for analyzing facial features related to sialorrhea and hypomimia in Parkinson’s disease, using static video frame analysis.

## Repository Structure

- `find_neutral.py` / `find_happiness_apex.py` – Identify neutral and peak-expression (apex) frames from video.
- `extract_face_landmarks.py` – Extract 68-point facial landmarks using dlib.
- `extract_features*.py` – Compute facial geometry and expression features.
- `feature_analysis.ipynb` – Jupyter notebook for visualizing and analyzing extracted features.
- `move_booth_videos.py` – Script to organize video datasets.
- `significant_results*.csv` – Output files containing statistical feature results.
- `requirements.txt` – Lists required Python packages.

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
