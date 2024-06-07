import conf
from boltiot import Email, Bolt
import json
import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Constants
minimum_limit = 300  # the minimum threshold of light value 
maximum_limit = 600  # the maximum threshold of light value 
historical_data = []  # list to store historical light intensity data

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)

def read_sensor_value():
    """Reads and returns the current sensor value."""
    response = mybolt.analogRead('A0') 
    data = json.loads(response)
    return int(data['value'])

def collect_historical_data():
    """Collects historical data for training the model."""
    global historical_data
    while len(historical_data) < 50:  # Collect data for 50 iterations
        sensor_value = read_sensor_value()
        if sensor_value != -999:
            historical_data.append(sensor_value)
        time.sleep(10)

def train_polynomial_regression_model():
    """Trains a polynomial regression model using historical data."""
    global historical_data
    X = np.arange(1, len(historical_data) + 1).reshape(-1, 1)
    y = np.array(historical_data).reshape(-1, 1)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Polynomial features
    degree = 2  # Set the degree of the polynomial
    poly = PolynomialFeatures(degree=degree)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

    # Train the polynomial regression model
    model = LinearRegression()
    model.fit(X_poly_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_poly_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    return model, poly

def predict_light_intensity(model, poly, sensor_value):
    """Predicts light intensity using the trained model."""
    X_pred = np.array([[len(historical_data) + 1]])
    X_poly_pred = poly.transform(X_pred)
    predicted_intensity = model.predict(X_poly_pred)
    return predicted_intensity[0][0]

def visualize_prediction(model, poly):
    """Visualizes the predictions."""
    global historical_data
    X = np.arange(1, len(historical_data) + 1).reshape(-1, 1)
    y = np.array(historical_data).reshape(-1, 1)

    # Polynomial features
    X_poly = poly.transform(X)

    # Predictions
    y_pred = model.predict(X_poly)

    # Plot the results
    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X, y_pred, color='red', label='Predicted Trend')
    plt.xlabel('Data Points')
    plt.ylabel('Light Intensity')
    plt.title('Polynomial Regression Prediction')
    plt.legend()
    plt.show()

# Main loop
def main():
    collect_historical_data()
    model, poly = train_polynomial_regression_model()

    while True:
        sensor_value = read_sensor_value()
        if sensor_value != -999:
            predicted_intensity = predict_light_intensity(model, poly, sensor_value)
            print(f"Actual Sensor Value: {sensor_value}, Predicted Intensity: {predicted_intensity}")

            if sensor_value > maximum_limit or sensor_value < minimum_limit:
                print("Making request to Mailgun to send an email")
                response = mailer.send_email("Alert", f"The current light sensor value is {sensor_value}, Predicted Intensity: {predicted_intensity}")
                response_text = json.loads(response.text)
                print("Response received from Mailgun is: " + str(response_text['message']))

            visualize_prediction(model, poly)
        
        time.sleep(10)

if __name__ == "__main__":
    main()
