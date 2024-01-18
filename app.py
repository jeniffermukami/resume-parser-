from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import csv
import os

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes


# Define a route to serve the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Function to save data to a CSV file
def save_to_csv(data, filename='data.csv'):
    # Check if the file exists to determine if headers are needed
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        
        # Write headers only if the file is being created
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)

# Define the endpoint for saving data via POST request
@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.json
    save_to_csv(data)
    return jsonify({'message': 'Data saved successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
