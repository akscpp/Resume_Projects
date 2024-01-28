import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation

from boltiot import Bolt        # importing Bolt from boltiot module
import conf                     # config file

# Create a Bolt instance using API key and device ID from the configuration file
mybolt = Bolt(conf.bolt_api_key, conf.device_id)

def get_sensor_value_from_pin(pin):
    """Returns the sensor value. Returns -999 if request fails"""
    try:
        # Step 1: Read the analog value from the specified pin
        response = mybolt.analogRead(pin)
        data = json.loads(response)
        
        # Check if the request was successful
        if data["success"] != 1:
            print("Request not successful")
            print("This is the response->", data)
            return -999
        
        # Extract and return the sensor value
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Something went wrong when returning the sensor value")
        print(e)
        return -999

def send_telegram_message(message):
    """Sends message via Telegram"""
    url = "https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {
        "chat_id": conf.telegram_chat_id,
        "text": message
    }
    try:
        # Step 2: Send the message to Telegram
        response = requests.request(
            "POST",
            url,
            params=data
        )
        print("This is the Telegram URL")
        print(url)
        print("This is the Telegram response")
        print(response.text)
        telegram_data = json.loads(response.text)
        
        # Return True if the message was sent successfully
        return telegram_data["ok"]
    except Exception as e:
        print("An error occurred in sending the alert message via Telegram")
        print(e)
        return False

# Main loop
while True:
    # Step 3: Read sensor value from pin "A0"
    sensor_value = get_sensor_value_from_pin("A0")    
    print("The current sensor value is:", sensor_value)
    
    # Step 4: Check if the request was unsuccessful
    if sensor_value == -999:
        print("Request was unsuccessful. Skipping.")
        time.sleep(10)
        continue
    
    # Step 5: Check if sensor value exceeds the threshold
    if sensor_value >= conf.threshold:
        print("Sensor value has exceeded threshold")
        message = "Alert! Sensor value has exceeded " + str(conf.threshold) + \
                  ". The current value is " + str(sensor_value)
        
        # Step 6: Send alert message via Telegram
        telegram_status = send_telegram_message(message)
        print("This is the Telegram status:", telegram_status)

    # Step 7: Wait for 10 seconds before the next iteration
    time.sleep(10)
