import os
import shutil
import zipfile
import subprocess

# ---------------------------
# Step 1: Setup Kaggle API Key
# ---------------------------
def setup_kaggle_api(kaggle_json_path):
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)
    dest_path = os.path.join(kaggle_dir, "kaggle.json")
    shutil.copy(kaggle_json_path, dest_path)
    os.chmod(dest_path, 0o600)
    print("✅ Kaggle API key set up.")

# ---------------------------
# Step 2: Download Dataset
# ---------------------------
def download_dataset(dataset_slug="banuteja008/tiny-image-net", download_dir="."):
    print("⬇️ Downloading dataset from Kaggle...")
    subprocess.run(["kaggle", "datasets", "download", "-d", dataset_slug, "-p", download_dir, "--force"])
    print("✅ Download complete.")

# ---------------------------
# Step 3: Extract Dataset
# ---------------------------
def extract_dataset(zip_path="tiny-image-net.zip", extract_to="tiny_imagenet"):
    print("📦 Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print("✅ Extraction done.")

# ---------------------------
# Step 4: Preprocess Validation Data
# ---------------------------
def organize_validation_set(base_dir="tiny_imagenet/tiny-imagenet-200"):
    val_dir = os.path.join(base_dir, "val")
    val_annotations_path = os.path.join(val_dir, "val_annotations.txt")
    images_dir_path = os.path.join(val_dir, "images")

    # Load annotations
    annotations = {}
    with open(val_annotations_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            image_name, class_id = parts[0], parts[1]
            annotations[image_name] = class_id

    # Create class folders and move images
    for image_name, class_id in annotations.items():
        class_dir = os.path.join(val_dir, class_id)
        os.makedirs(class_dir, exist_ok=True)
        src_path = os.path.join(images_dir_path, image_name)
        dest_path = os.path.join(val_dir, class_id, image_name)
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)

    shutil.rmtree(images_dir_path)
    print("✅ Validation images organized into class folders.")

# ---------------------------
# Run all steps
# ---------------------------
def prepare_tiny_imagenet(kaggle_json_path):
    setup_kaggle_api(kaggle_json_path)
    download_dataset()
    extract_dataset()
    organize_validation_set()

if __name__ == "__main__":
    kaggle_json_path = r"C:/Users/hasna/Projects/ML ImageNet Project/kaggle.json"  # update if needed
    prepare_tiny_imagenet(kaggle_json_path)
