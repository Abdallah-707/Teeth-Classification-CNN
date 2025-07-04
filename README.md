[![Support Palestine](https://raw.githubusercontent.com/Ademking/Support-Palestine/main/Support-Palestine.svg)](https://www.map.org.uk)

# 🦷 Teeth Classification using CNN
![Teeth Classification using CNN](https://static.wixstatic.com/media/b36da8_2179a5da33b5492583fca41bbf09831f~mv2.jpg/v1/fill/w_1000,h_524,al_c,q_85,usm_0.66_1.00_0.01/b36da8_2179a5da33b5492583fca41bbf09831f~mv2.jpg)

This project implements a deep learning model to classify teeth images using Convolutional Neural Networks (CNN) in TensorFlow/Keras. It processes a dataset of teeth images and learns to classify them into various categories.

---

## 📁 Dataset Structure

The dataset is organized into directories by class. For example:

```
Teeth_Dataset/
└── Training/
    ├── Class_1/
    ├── Class_2/
    └── ...
```

Each subdirectory contains the images for that specific class.

---

## 📦 Libraries Used

- `TensorFlow` / `Keras` – Deep learning framework
- `Pandas` / `NumPy` – Data manipulation
- `Matplotlib` / `Seaborn` / `Plotly` – Data visualization
- `PIL` – Image processing
- `Scikit-learn` – Model evaluation

---

## 📊 Data Loading & Preparation

- The script reads image file paths and labels from the training folder.
- Data is organized into a Pandas DataFrame for easy handling.
- Images are resized, normalized, and fed into a `ImageDataGenerator` for data augmentation.

---

## 🧠 Model Architecture

A CNN is built using Keras `Sequential` API with:

- Convolutional layers
- MaxPooling
- Batch Normalization
- Dropout layers
- Dense layers with softmax output

The model is compiled using the **Adam** or **Adamax** optimizer and trained with **early stopping** and **model checkpointing** callbacks.

---

## 📈 Training

- The dataset is split into training and validation sets using `train_test_split`.
- The model is trained for several epochs with real-time augmentation.
- Accuracy and loss are plotted for both training and validation.

---

## 🧪 Evaluation

The model is evaluated using:

- **Confusion Matrix**
- **Classification Report**

These help visualize per-class performance and overall precision, recall, and F1-score.

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/teeth-classification.git
cd teeth-classification
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure the dataset is placed in the correct folder structure (`Teeth_Dataset/Training/...`).

4. Run the notebook:

```bash
jupyter notebook teeth-classification.ipynb
```

---

## 🖼️ Sample Visualization

- Training/validation accuracy & loss curves
- Confusion matrix heatmap

---

## 📌 Requirements

- Python 3.7+
- TensorFlow 2.x
- Jupyter Notebook
- GPU (optional but recommended for faster training)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Acknowledgements

- Inspired by practical applications in dental diagnostics.
- Built using open-source libraries in the Python ecosystem.
