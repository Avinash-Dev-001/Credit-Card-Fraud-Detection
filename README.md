

# Fraud Detection Web Application

This is a **Fraud Detection** web application that predicts whether a transaction is fraudulent or not, based on a set of features. The application uses a machine learning model for fraud prediction and is built using **Flask** for the backend and **HTML**, **CSS**, and **JavaScript** for the frontend.

## Features

- **Input Features**: Users input a list of comma-separated values (features) such as transaction amount, frequency, etc.
- **Prediction**: The system predicts whether the transaction is fraudulent or not.
- **User Interface**: Simple and responsive UI to input the data and display results.
  
## Technologies Used

- **Backend**: 
  - **Flask**: A Python web framework used to create the backend and API endpoints for the fraud detection prediction.
  - **Pickle**: Used to load the pre-trained fraud detection model for predictions.
  
- **Frontend**: 
  - **HTML**: Markup language used to structure the web page.
  - **CSS**: Styling language used to design the UI and make it responsive.
  - **JavaScript**: For handling form submission and interacting with the backend API using the **Fetch API**.
  
- **Libraries**:
  - **Flask** (for the server and routing).
  - **Flask-CORS** (to handle Cross-Origin Resource Sharing for API requests).
  - **Pickle** (to deserialize and load the pre-trained machine learning model).

## How It Works

1. The user inputs comma-separated values (features) in the form on the webpage.
2. The frontend uses **JavaScript** to send these features to the backend via an HTTP POST request.
3. The **Flask** backend receives the features, loads the pre-trained fraud detection model (saved as a `.pkl` file), and predicts the likelihood of fraud.
4. The backend returns the prediction result, and the frontend displays it to the user.

## How to Run

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Pickle

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/fraud-detection-webapp.git
   cd fraud-detection-webapp
   ```

2. **Install dependencies:**

   If you don't have `Flask` and `flask_cors` installed, you can install them using pip:

   ```bash
   pip install flask flask-cors
   ```

3. **Download the model:**

   Make sure your `fraud_detection_model.pkl` (your pre-trained model) is in the project folder.

4. **Run the Flask app:**

   To start the Flask server, run:

   ```bash
   python app.py
   ```

   This will start the Flask app at `http://127.0.0.1:5000`.

5. **Open the web application:**

   Go to `http://127.0.0.1:5000` in your browser, input the feature values, and click **Predict** to get the fraud detection result.

### Running the Frontend

The frontend code (HTML, CSS, and JavaScript) runs directly in the browser when you access the Flask app.

### Example Input

For example, input values could look like:

```
0.1, 0.2, 0.3, 0.4
```

This would trigger a prediction from the model on whether the transaction is fraudulent or not.

### Example Output

After submitting the form, the prediction result will be displayed on the page:

- **Prediction: fraud**
- **Prediction: not fraud**

## Project Structure

```
fraud-detection-webapp/
│
├── app.py                  # Flask backend and API
├── fraud_detection_model.pkl  # Pre-trained fraud detection model (Pickle format)
├── templates/
│   └── index.html          # Frontend HTML file
└── README.md               # Project documentation
```

## Contributing

Feel free to fork the project and make improvements or add features. For any issues or questions, open an issue in the repository.

## License

This project is open-source and available under the MIT License.
