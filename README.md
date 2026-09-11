# Tiny ImageNet: Multi-Model & Few-Shot Learning Evaluation

This project investigates image classification on the Tiny ImageNet dataset using multiple deep learning architectures and few-shot / meta-learning approaches.

The central research question is:

> Can meta-learning improve image classification performance in a limited-data setting compared with standard transfer-learning baselines?

The project compares supervised CNN baselines with meta-learning methods and includes quantitative evaluation, confusion-matrix analysis, class-level error analysis, representation visualization, and saved experimental artifacts.

---

## Key Result

In the evaluated low-data setting:

- **Fine-tuned ResNet-50 baseline:** 52.1%
- **MAML meta-learning accuracy:** 67.5%
- **Improvement:** +15.4 percentage points

The project also includes confusion matrices, t-SNE visualizations, class-level analysis, and comparative evaluation across multiple architectures.

---

## Models Evaluated

### Supervised / Transfer Learning
- ResNet-50
- EfficientNetB0
- EfficientNetB3
- MobileNet

### Few-Shot / Meta-Learning
- Model-Agnostic Meta-Learning (MAML)
- Additional few-shot learning experiments implemented during the project

---

## Dataset

**Tiny ImageNet**

- 200 classes
- 64 × 64 RGB images
- Separate training and validation sets
- Multi-class visual recognition benchmark

Source: Tiny ImageNet via Kaggle

The `data_loader.py` script downloads, extracts, preprocesses, and reorganizes the validation data into class-wise directories.

---

## Research Workflow

1. Established supervised CNN baselines using transfer learning.
2. Compared multiple pretrained architectures under a common evaluation setup.
3. Implemented few-shot / meta-learning experiments for limited-data classification.
4. Evaluated model performance quantitatively across model variants.
5. Performed class-level error analysis using confusion matrices.
6. Visualized learned representations using t-SNE.
7. Saved model weights, training metrics, feature vectors, and evaluation outputs for reproducibility.

---

## Pretrained Models

The trained model weights exceed GitHub's file-size limit.

You can download them here:

[Download saved model weights from Google Drive](https://drive.google.com/file/d/1tlJHGTNRsyjOq4ZuUS70WCirN7krtlDT/view?usp=sharing)

After downloading:

- Unzip `saved_models.zip`
- Place the extracted `saved_models/` directory in the project root

---

## Project Structure

    saved_models/                    # Trained model weights
    backup/                          # Experimental / unused code
    features/                        # Precomputed feature representations
    all_query_features.npy           # Saved query feature vectors
    all_query_labels.npy             # Saved query labels
    data_loader.py                   # Dataset download and preprocessing
    ML_ImageNet_Project.ipynb        # Main training, evaluation, and visualization notebook
    evaluation_results.json          # Comparative model results
    effnetb0_training_metrics.json   # EfficientNetB0 training history
    resnet50_adam_full_metrics.json  # ResNet50 training history
    effnetb0_weights.h5              # EfficientNetB0 saved weights
    README.md                        # Project documentation
    requirements.txt                 # Python dependencies
    .gitignore                       # Git ignore rules

---

## Getting Started

### 1. Clone the Repository

    git clone https://github.com/hasnain0504/tinyimagenet-project.git
    cd tinyimagenet-project

### 2. Set Up the Environment

    conda create -n tfgpu_clean python=3.10
    conda activate tfgpu_clean
    pip install -r requirements.txt

### 3. Add Kaggle API Token

- Go to Kaggle
- Download your `kaggle.json` API token
- Place it in the required Kaggle credentials location for your system

### 4. Run the Data Loader

    python data_loader.py

### 5. Run the Main Notebook

Open:

    ML_ImageNet_Project.ipynb

The notebook contains the main training, evaluation, visualization, and model-comparison workflow.

---

## Evaluation Artifacts

The project includes:

- Model comparison metrics
- Training and validation accuracy histories
- Confusion matrices
- Class-level error analysis
- t-SNE representation visualizations
- Comparative model plots
- Saved query feature vectors
- Saved model weights
- JSON-based evaluation outputs

These artifacts support comparison across architectures and learning approaches.

---

## Visual Outputs

The evaluation workflow produces:

- Model comparison bar charts
- Training / validation curves
- Confusion matrices
- t-SNE visualizations
- Additional comparative evaluation plots

---

## Project Motivation

This project was designed as a comparative investigation rather than a single-model image-classification exercise.

The supervised models establish strong reference baselines, while the few-shot and meta-learning experiments explore whether alternative learning strategies can improve generalization when labeled training data is limited.

The broader motivation is to study **data-efficient visual learning** and understand how different model families behave under constrained-data conditions.

---

## Technologies

- Python
- TensorFlow / Keras
- PyTorch
- scikit-learn
- NumPy
- Matplotlib
- Transfer Learning
- Few-Shot Learning
- Meta-Learning
- MAML
- t-SNE
- Confusion-Matrix Analysis
- Tiny ImageNet

---

## Notes

- Default image size: 64 × 64
- Training metrics are saved as `.json` files for later analysis
- Large trained model files are hosted externally due to GitHub file-size limits
- Additional experimental files are retained in the repository for reproducibility and comparison

---

## Author

**Hasnain Somani**  
M.S. Data Science, University of Texas at Arlington

GitHub: [hasnain0504](https://github.com/hasnain0504)
