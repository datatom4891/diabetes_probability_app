## **Probability of Diabetes ML Model App**

This is a predictive ML app that predicts the probability of being diabetic based on 11 Health Indicators.
The ML model was trained using a balanced dataset of diabetic and non-diabetic that was put together using the CDC's Behavioral Risk Factor Surveillance System (BRFSS).
The dataset I trained the model on is from kaggle: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset.

I am serving the Model as a microservice using FastAPI on the backend and Streamlit for the frontend. I also leverage LIME to visually explain the predictions made by the model, in the Streamlit U.I.
The app can be run locally on any computer with docker installed.
To run the app:
1.  Pull the source code from the repo onto your machine.
2.  Navigate to the root folder from the command line and run this docker command: docker-compose up
