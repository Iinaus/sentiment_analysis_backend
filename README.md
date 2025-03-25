# Sentiment Analysis Backend

## Table of contents
- [About](#about)
    - [Data](#data)
    - [Frontend](#frontend)
- [Getting started](#getting-started)
     - [Dependencies](#dependencies)
     - [Dev setup step-by-step](#dev-setup-step-by-step)


## About

This project is an exercise in developing and deploying a Sentiment Analysis backend. It was created as part of the Cloud Computing course at Lapland University of Applied Sciences. The project is built using Python 3.9 to ensure compatibility with CSC OpenShift, which is used for deployment. The backend server is running until 31.08.2025.

With this exercise we practiced:

- Developing and deploying a machine learning-based web application
- Handling text data and implementing machine learning workflows
- Cloud-based deployment of the application for easy accessibility
- Managing development using Git and branching strategies to ensure efficient collaboration and code deployment

### Data

The model is trained using a CSV dataset (train.csv) that contains labeled text data. The dataset consists of text samples labeled with sentiments (positive, negative, neutral). The dataset used in this project is based on the [Sentiment Analysis Dataset](https://www.kaggle.com/datasets/abhi8923shriv/sentiment-analysis-dataset) from Kaggle, which is a collection of tweets and their sentiment labels. You can find more details and download the dataset from the provided link.

### Frontend

The frontend project was also developed as part of the Cloud Computing course at Lapland University of Applied Sciences. The project utilizes Vite as the build tool and is deployed on Render.com for hosting. You can find it running live on https://sentiment-analysis-frontend-o7e4.onrender.com/. You can find more details about the frontend project here: [https://github.com/Iinaus/sentiment_analysis_frontend](https://github.com/Iinaus/sentiment_analysis_frontend).

## Getting started

Follow the instructions below to set up the project and run the app locally.

### Dependencies

This project relies on the following dependencies:

- **Python**: The main programming language used for the backend and model training.
- **Flask**:
- **Scikit-Learn**: Used for machine learning, including the TfidfVectorizer and LinearSVC classifier.
- **Pandas**: Used for handling and preprocessing the dataset.

Ensure these dependencies are installed to ensure smooth execution of the project.

### Dev setup step-by-step

To run the project locally:

1. Clone the project
2. Install the required dependencies with the following command
 `pip install -r requirements.txt`
3. Run the backend with command
`python app.py`
