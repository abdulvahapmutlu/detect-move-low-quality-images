import os
import shutil
from PIL import Image

def detect_and_move_low_quality_images(directory, min_width, min_height):
    # Define the path for low-quality images
    low_quality_folder = os.path.join(directory, 'low_quality')
    if not os.path.exists(low_quality_folder):
        os.makedirs(low_quality_folder)  # Create the folder if it doesn't exist

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)
            try:
                with Image.open(image_path) as img:
                    width, height = img.size  # Get image dimensions
                    # Check if the image dimensions are below the specified thresholds
                    if width < min_width or height < min_height:
                        destination_path = os.path.join(low_quality_folder, filename)
                        shutil.move(image_path, destination_path)  # Move the low-quality image
                        print(f"Moved low-quality image: {filename}")

                        # Ensure the file was moved by deleting any remaining duplicate
                        if os.path.exists(image_path):
                            os.remove(image_path)
                            print(f"Deleted duplicate from original directory: {filename}")
            except Exception as e:
                pass  # Ignore any errors during image processing

dataset_directory = 'path/to/directory'
min_width, min_height = 224, 224  # Set the minimum width and height for images
detect_and_move_low_quality_images(dataset_directory, min_width, min_height)
print("Done")
