Tiny ImageNet - Multi-Model Evaluation Project

This project performs image classification on the Tiny ImageNet dataset using multiple deep learning architectures including ResNet50, EfficientNetB0, EfficientNetB3, MobileNet Multiple Few Shot Learning approaches too, and then it saves all the results for comparison.

📁 Dataset

Source: Tiny ImageNet - Kaggle Dataset

The dataset contains:

200 classes

64x64 color images

Separate train and validation folders

Use the data_loader.py script to download, unzip, and preprocess the dataset (class-wise organization of validation data).

📦 Project Structure

├── saved_models/                  # Contains all .h5 saved model weights
├── backup/                        # Ignored: test code, datasets, and unused experiments
├── features/                      # Precomputed feature vectors (optional storage)
├── all_query_features.npy         # Saved query feature vectors
├── all_query_labels.npy           # Saved query labels
├── data_loader.py                # Script to download & preprocess Tiny ImageNet from Kaggle
├── ML_ImageNet_Project.ipynb     # Main notebook for training, evaluation & visualization
├── evaluation_results.json        # Model comparison results (used in visualization block)
├── effnetb0_training_metrics.json # Training history for EfficientNetB0
├── resnet50_adam_full_metrics.json # Training history for ResNet50
├── effnetb0_weights.h5           # Saved weights for EfficientNetB0 
├── README.md                     # Project documentation
├── requirements.txt              # Required dependencies
├── .gitignore                    # Git ignore rules


🚀 Getting Started

1. Clone the Repository

git clone https://github.com/hasnain0504/tinyimagenet-project.git
cd tinyimagenet-project

2. Set Up Environment

conda create -n tfgpu_clean python=3.10
conda activate tfgpu_clean
pip install -r requirements.txt

3. Add Kaggle API Token

Go to Kaggle

Download your kaggle.json API token

Place it in the project root directory

4. Run Data Loader

python data_loader.py

🧠 Train or Load Models

Each model can be loaded or trained from scratch. .h5 files (saved models / weights) are present in the project folder.

📊 Final Evaluation

Visualization Block in ML_ImageNet_Project.ipynb

Outputs a bar graph, and multiple other comparision visuals.

🖼️ Visual Outputs

Evaluation script saves and displays:

Model comparison bar graph

Sample logs with training/validation accuracy

You can also generate individual training curves from the metrics .json files.

📝 Notes

Default image size is 64x64 as per dataset

All training metrics are saved as .json files for further analysis

✨ Author

Hasnain Somani — 2025
Feel free to connect or give feedback!