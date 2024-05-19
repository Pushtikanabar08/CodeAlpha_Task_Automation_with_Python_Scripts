import os
import shutil

# Define the directory to organize
directory_to_organize = 'path_to_your_directory'

# Define where to move files based on their extensions
file_type_destinations = {
    'documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'videos': ['.mp4', '.avi', '.mov'],
    'music': ['.mp3', '.wav'],
    'archives': ['.zip', '.tar', '.rar'],
    # Add more categories and file extensions as needed
}

# Create directories if they don't exist
for folder in file_type_destinations.keys():
    folder_path = os.path.join(directory_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'Created directory: {folder_path}')

# Function to organize files
def organize_files():
    print(f'Starting to organize files in {directory_to_organize}...\n')
    for item in os.listdir(directory_to_organize):
        item_path = os.path.join(directory_to_organize, item)
        if os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1].lower()
            moved = False
            for folder, extensions in file_type_destinations.items():
                if file_extension in extensions:
                    dest_path = os.path.join(directory_to_organize, folder, item)
                    shutil.move(item_path, dest_path)
                    print(f'Moved: {item} to {folder}')
                    moved = True
                    break
            if not moved:
                print(f'No category found for: {item}, leaving in place.')
        else:
            print(f'Skipping directory: {item}')
    print('\nFinished organizing files.')

if __name__ == "__main__":
    organize_files()
