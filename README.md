# Detect and Move Low-Quality Images

This Python script identifies and moves low-quality images (below a specified resolution) from a dataset to a designated folder.

## Features

- Image Quality Detection: Scans images to check if they meet the minimum width and height requirements.
- File Handling: Moves low-quality images to a `low_quality` subfolder within the dataset directory.
- Supported Formats: Handles `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif` files.

## Requirements

- Python 3.x
- PIL (Pillow)
- shutil (standard library)

## Installation

```
pip install Pillow
```

## Usage

Define the dataset directory and minimum dimensions, then run the script:

```
dataset_directory = r'path/to/your/dataset'
min_width, min_height = 224, 224
detect_and_move_low_quality_images(dataset_directory, min_width, min_height)
```

The script will process all images in the specified directory and move any that do not meet the size criteria to a `low_quality` subfolder.

# Delete Matching Files

The second Python script helps in managing and cleaning up directories by deleting files in a main folder if they also exist in a specified low-quality subfolder.

### Features
- File Matching: Identifies and deletes files that are present in both the main folder and the low-quality folder.
- Directory Management: Operates within specified directories to ensure efficient file cleanup.

### Requirements
- Python 3.x

### Usage
Define the main and low-quality directories, then run the script:

```
main_folder = 'path/to/main_folder'
low_quality_folder = 'path/to/low_quality_folder'
delete_matching_files(main_folder, low_quality_folder)
```
### License

This project is licensed under the MIT License.
