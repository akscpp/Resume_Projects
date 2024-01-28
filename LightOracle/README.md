# README.md

# Light Intensity Monitoring and Prediction with Email Alerts

# Overview

This project monitors light intensity using a Bolt IoT device, predicts future values with a polynomial regression model, and sends email alerts for abnormal readings. It also visualizes the actual and predicted data.

# Key Features

Real-time light intensity readings
Predictive model for future intensity values
Email notifications for abnormal readings
Visualization of actual and predicted data
# Dependencies

Bolt Python library (boltiot)
Mailgun Python library (mailgun)
NumPy (numpy)
Scikit-learn (sklearn)
Matplotlib (matplotlib)
# Configuration

Create a conf.py file with the following API keys and credentials:
API_KEY (Bolt API key)
DEVICE_ID (Bolt device ID)
MAILGUN_API_KEY (Mailgun API key)
SANDBOX_URL (Mailgun sandbox URL)
SENDER_EMAIL (Mailgun sender email address)
RECIPIENT_EMAIL (Recipient email address for alerts)
# Installation

Install required libraries: pip install boltiot mailgun numpy sklearn matplotlib
Create the conf.py file.
# Execution

Run the script: python light_intensity_monitoring.py
# Functionality

Collects historical light intensity data
Trains a polynomial regression model
Continuously reads sensor values
Predicts future intensity values using the model
Sends email alerts if readings exceed thresholds
Visualizes actual and predicted data
# Additional Notes

Adjust thresholds for email alerts in the code.
Explore different model parameters for potential accuracy improvements.
Consider error handling and logging for robustness.
