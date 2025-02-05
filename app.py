import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the pre-trained model from a pickle file
try:
    with open('energy.pkl', 'rb') as file:
        regressor = pickle.load(file)
except FileNotFoundError:
    regressor = None
    print("Error: 'energy.pkl' file not found.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if regressor is None:
        return "Model not loaded. Please ensure 'energy.pkl' exists."

    # Get the inputs from the form
    input1 = request.form.get('t1')
    input2 = request.form.get('t2')
    
    # Validate and convert the inputs
    try:
        input_data = [float(input1), float(input2)]
    except ValueError:
        return "Invalid input. Please enter numeric values."

    # Make a prediction
    try:
        prediction = regressor.predict([input_data])[0]
    except Exception as e:
        return f"An error occurred during prediction: {str(e)}"

    # Render the result.html with the prediction
    return render_template('result.html', prediction=f"{prediction:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
