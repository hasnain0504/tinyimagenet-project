# Tiny ImageNet: Multi-Model & Few-Shot Learning Evaluation

This project investigates multiclass image classification and few-shot learning on the Tiny ImageNet dataset using transfer learning and meta-learning approaches.

The central research question is:

> Can meta-learning improve image classification performance under limited-data conditions compared with conventional transfer-learning baselines?

The project evaluates multiple CNN architectures, including ResNet-50, MobileNet, EfficientNetB0, and EfficientNetB3, and integrates Model-Agnostic Meta-Learning (MAML) for few-shot classification.

---

## Key Result

Under the evaluated low-data setting:

- **Fine-tuned ResNet-50 baseline:** ~53%
- **MAML few-shot accuracy:** ~67%
- **Absolute improvement:** ~15 percentage points

The experiments demonstrate that meta-learning can provide substantial benefits when labeled data is limited, while fully fine-tuned models remain competitive when more training data is available.

---

## Project Resources

- **Full Project Page:**  
  [View methodology, results, and visual analysis](https://hasnainsomani.vercel.app/projects/multiclass-object-detection)

- **GitHub Repository:**  
  [tinyimagenet-project](https://github.com/hasnain0504/tinyimagenet-project)

- **Pretrained Model Weights:**  
  [Download from Google Drive](https://drive.google.com/file/d/1tlJHGTNRsyjOq4ZuUS70WCirN7krtlDT/view?usp=sharing)

- **Technical Article:**  
  [View Technical Article](https://medium.com/@hasnain.somani2/transfer-learning-few-shot-on-imagenet-b01a112e6573?sharedUserId=hasnain.somani2)

---

## Technical Highlights

- Trained multiclass image-classification models using ResNet-50, MobileNet, EfficientNetB0, and EfficientNetB3.
- Evaluated frozen, partially fine-tuned, and fully fine-tuned transfer-learning configurations.
- Integrated **Model-Agnostic Meta-Learning (MAML)** for few-shot classification under limited-data conditions.
- Performed hyperparameter experimentation across learning rates, optimizers, dropout configurations, and dense layers.
- Built modular training and evaluation workflows with reusable metrics and saved experiment artifacts.
- Conducted confusion-matrix analysis and model-level performance comparison.
- Used **t-SNE visualization** to inspect learned feature representations and class separability.
- Compared conventional transfer learning with meta-learning under different data regimes.

---

## Visual Analysis

The full project page contains detailed plots and discussion, including:

- Training vs. validation accuracy
- Training vs. validation loss
- Model-wise performance comparison
- Few-shot baseline vs. MAML comparison
- MAML training progression
- t-SNE visualization of learned embeddings

View all results here:

[Full Results and Visualizations](https://hasnainsomani.vercel.app/projects/multiclass-object-detection)

---

## Dataset

**Tiny ImageNet**

- 200 classes
- 64 × 64 RGB images
- Separate training and validation sets
- Multi-class image-recognition benchmark

Dataset source: Tiny ImageNet via Kaggle.

The `data_loader.py` script downloads, extracts, preprocesses, and reorganizes the validation data into class-wise directories.

---

## Research Workflow

1. Established transfer-learning baselines using pretrained CNN architectures.
2. Compared frozen, partially fine-tuned, and fully fine-tuned configurations.
3. Evaluated architecture-level performance across multiple CNN families.
4. Implemented MAML for few-shot classification under limited-data conditions.
5. Compared few-shot performance against conventional fine-tuned baselines.
6. Conducted class-level error analysis and confusion-matrix evaluation.
7. Visualized learned feature representations using t-SNE.
8. Saved training metrics, model weights, feature vectors, and evaluation outputs for reproducibility.

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
    requirements.txt                 # Python dependencies
    README.md                        # Project documentation
    .gitignore                       # Git ignore rules

---

## Pretrained Models

Some trained model files exceed GitHub's file-size limit.

Download them here:

[Download saved model weights](https://drive.google.com/file/d/1tlJHGTNRsyjOq4ZuUS70WCirN7krtlDT/view?usp=sharing)

After downloading:

- Unzip `saved_models.zip`
- Place the extracted `saved_models/` directory in the project root

---

## Getting Started

### 1. Clone the Repository

    git clone https://github.com/hasnain0504/tinyimagenet-project.git
    cd tinyimagenet-project

### 2. Set Up the Environment

    conda create -n tfgpu_clean python=3.10
    conda activate tfgpu_clean
    pip install -r requirements.txt

### 3. Configure Kaggle Access

- Download your `kaggle.json` API token from Kaggle
- Place it in the appropriate Kaggle credentials location for your system

### 4. Download and Preprocess the Dataset

    python data_loader.py

### 5. Run the Main Notebook

Open:

    ML_ImageNet_Project.ipynb

The notebook contains the primary training, evaluation, model-comparison, and visualization workflow.

---

## Evaluation Artifacts

The repository contains:

- Model-comparison metrics
- Training and validation histories
- Confusion matrices
- Class-level error analysis
- t-SNE representation visualizations
- Saved query feature vectors
- JSON evaluation outputs
- Trained model weights

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

## Author

**Hasnain Somani**  
M.S. Data Science, University of Texas at Arlington

- [Portfolio](https://hasnainsomani.vercel.app)
- [GitHub](https://github.com/hasnain0504)
