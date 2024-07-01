import os

def delete_matching_files(main_folder, low_quality_folder):
    # Get the list of files in the low_quality folder
    low_quality_files = set(os.listdir(low_quality_folder))
    
    # Iterate over the files in the main folder
    for filename in os.listdir(main_folder):
        main_file_path = os.path.join(main_folder, filename)
        
        # Check if the file exists in the low_quality folder
        if filename in low_quality_files:
            try:
                os.remove(main_file_path)
                print(f"Deleted file: {main_file_path}")
            except Exception as e:
                pass

# Define the folders
main_folder = 'path/to/directory'
low_quality_folder = 'path/to/directory'

# Run the function
delete_matching_files(main_folder, low_quality_folder)

print("Done")
