import conf
from boltiot import Sms, Bolt
import json
import time

minimum_limit = 300
maximum_limit = 600  

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

while True:
    print("Reading sensor value")
    
    # Step 1: Read analog value from pin 'A0'
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    
    # Step 2: Print the sensor value
    print("Sensor value is: " + str(data['value']))
    
    try: 
        # Step 3: Convert sensor value to integer
        sensor_value = int(data['value']) 
        
        # Step 4: Check if sensor value is outside the defined limits
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send an SMS")
            
            # Step 5: Send SMS using Twilio
            response = sms.send_sms("The current temperature sensor value is " + str(sensor_value))
            
            # Step 6: Print Twilio response details
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is: " + str(response.status))
    
    except Exception as e: 
        # Step 7: Handle exceptions
        print("Error occurred: Below are the details")
        print(e)
    
    # Step 8: Wait for 10 seconds before the next iteration
    time.sleep(10)
