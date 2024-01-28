# README.md

# Sensor Monitoring with Telegram Alerts

# Overview

This project continuously monitors a sensor connected to a Bolt IoT device and sends alerts via Telegram when the sensor value exceeds a defined threshold.

# Key Features

Real-time sensor value readings
Telegram notifications for abnormal readings
Error handling for resilience
# Dependencies

Bolt Python library (boltiot)
Requests library (requests)
# Configuration

Create a conf.py file containing:
bolt_api_key (Bolt API key)
device_id (Bolt device ID)
telegram_bot_id (Telegram bot ID)
telegram_chat_id (Telegram chat ID)
threshold (Sensor value threshold for alerts)
# Installation

Install required libraries: pip install boltiot requests
Create the conf.py file.
# Execution

Run the script: python sensor_monitoring_telegram_alerts.py
# Functionality

Fetches sensor readings from the Bolt device
Checks readings against the threshold
Sends alert messages via Telegram if the threshold is exceeded
Handles errors during sensor reads and Telegram messaging
# Additional Notes

Adjust the threshold in the conf.py file.
Consider logging for troubleshooting and analysis.
Explore visualizations for sensor data trends.
