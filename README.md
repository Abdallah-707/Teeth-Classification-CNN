[![Support Palestine](https://raw.githubusercontent.com/Ademking/Support-Palestine/main/Support-Palestine.svg)](https://www.map.org.uk)

# Teeth Disease Classification Project
![Teeth Classification using CNN](https://static.wixstatic.com/media/b36da8_2179a5da33b5492583fca41bbf09831f~mv2.jpg/v1/fill/w_1000,h_524,al_c,q_85,usm_0.66_1.00_0.01/b36da8_2179a5da33b5492583fca41bbf09831f~mv2.jpg)

This repository contains a deep learning project for classifying various teeth diseases from images. It includes two Jupyter notebooks detailing the model creation process (one using transfer learning and another from scratch), a saved Keras model, and a Streamlit web application for easy user interaction.

## Table of Contents

- [About The Project](#about-the-project)
- [File Descriptions](#file-descriptions)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

The primary goal of this project is to develop a robust image classification model capable of identifying different types of dental diseases from images. The project explores two approaches: a model built from scratch and a more powerful model utilizing transfer learning. The final model is deployed in a user-friendly Streamlit web application where users can upload an image and get a prediction about the dental condition.

The classes of teeth diseases the model can identify are:
- Caries (CaS)
- Canker Sore (CoS)
- Gum Disease (Gum)
- Mouth Cancer (MC)
- Oral Cancer (OC)
- Oral Lichen Planus (OLP)
- Oral Thrush (OT)

## File Descriptions

- **`teeth-classification.ipynb`**: A Jupyter Notebook that details the process of building, training, and evaluating the teeth disease classification model using transfer learning. This is the model that was saved as `teeth_classification.h5`.
- **`teeth-disease-scratch.ipynb`**: A Jupyter Notebook that shows the process of creating and training a convolutional neural network (CNN) for the same task, but built from the ground up.
- **`app.py`**: The Python script for the Streamlit web application. It loads the saved model and provides an interface for users to upload images and see the classification results.
- **`teeth_classification.h5`**: The saved, trained Keras model file. This is the output from the `teeth-classification.ipynb` notebook and is used by `app.py` to make predictions.
- **`requirements.txt`**: A text file that lists all the necessary Python packages and their versions required to run the project.
- **`README.md`**: This file, providing an overview and instructions for the project.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You need to have Python and pip installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

The dataset is organized into directories by class. For example:

```
Teeth_Dataset/
└── Training/
    ├── Class_1/
    ├── Class_2/
    └── ...
```

Each subdirectory contains the images for that specific class.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
    cd your_repository_name
    ```

2.  **Create a virtual environment** (recommended to keep dependencies isolated):
    ```sh
    python -m venv venv
    ```
    Activate the environment:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

3.  **Install the required packages** using the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Once the setup is complete, you can run the Streamlit application.

1.  Make sure the `teeth_classification.h5` model file is in the same directory as `app.py`.
2.  Run the following command in your terminal:
    ```sh
    streamlit run app.py
    ```
3.  This will open a new tab in your web browser with the application running, typically at `http://localhost:8501`.
4.  Click on the "Browse files" button to upload an image of a tooth.
5.  The application will display the uploaded image and the model's prediction for the disease type, along with the confidence score.

## Model Details

This project includes two models for teeth disease classification:

1.  **Model from Scratch (`teeth-disease-scratch.ipynb`)**: This model is a standard Convolutional Neural Network (CNN) built from basic Keras layers. It serves as a baseline and demonstrates the fundamental principles of building a CNN for image classification.

2.  **Transfer Learning Model (`teeth-classification.ipynb`)**: This is the primary model used in the Streamlit application. It leverages a pre-trained model (like VGG16, ResNet, or MobileNet) and fine-tunes it on the specific teeth disease dataset. This approach generally yields higher accuracy as it benefits from the features learned by the pre-trained model on a large dataset like ImageNet. The final trained model is saved in the `teeth_classification.h5` file.

## Deployment

This application can be easily deployed using Streamlit Community Cloud.

1.  Create a GitHub repository and push the following files:
    - `app.py`
    - `requirements.txt`
    - `teeth_classification.h5` (You might need to use Git LFS for large model files)
2.  Go to [share.streamlit.io](https://share.streamlit.io/) and sign up or log in with your GitHub account.
3.  Click on "New app" and select the repository you just created.
4.  Streamlit will automatically detect the `app.py` and `requirements.txt` files and deploy your application.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Abdallah Ammar - [@LinkedIn](https://www.linkedin.com/in/abdallah-hesham-ammar/) - abdallah.hesham.us@gmail.com
