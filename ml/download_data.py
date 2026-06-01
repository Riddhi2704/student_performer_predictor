import kagglehub
import shutil
import os

print("Downloading dataset using kagglehub...")
# Download the dataset
path = kagglehub.dataset_download("rabieelkharoua/students-performance-dataset")

print(f"Dataset downloaded to: {path}")

# Copy the dataset to the current working directory
target_dir = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(target_dir, exist_ok=True)

for file_name in os.listdir(path):
    full_file_name = os.path.join(path, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, target_dir)
        print(f"Copied {file_name} to data directory.")

print("Download complete.")
