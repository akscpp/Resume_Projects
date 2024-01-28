import email_conf
from boltiot import Email, Bolt
import json
import time

minimum_limit = 300  # the minimum threshold of light value 
maximum_limit = 600  # the maximum threshold of light value 

mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)

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
            print("Making request to Mailgun to send an email")
            
            # Step 5: Send email using Mailgun
            response = mailer.send_email("Alert", "The current temperature sensor value is " + str(sensor_value))
            response_text = json.loads(response.text)
            
            # Step 6: Print Mailgun response message
            print("Response received from Mailgun is: " + str(response_text['message']))
    
    except Exception as e: 
        # Step 7: Handle exceptions
        print("Error occurred: Below are the details")
        print(e)
    
    # Step 8: Wait for 10 seconds before the next iteration
    time.sleep(10)
