from flask import Flask, request, jsonify
import mysql.connector
import joblib
import os

app = Flask(__name__)

# ✅ Safe Database Connection Function (Does Not Return Connection in a Route)
def db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your-password",  # ⚠️ Move this to environment variables for security
            database="water_quality"
        )
        return conn
    except mysql.connector.Error as err:
        return None, str(err)

# ✅ Safe Response for Root Route Instead of Returning MySQL Connection
@app.route("/")
def home():
    return jsonify({"message": "Smart Water System API is running"}), 200

# ✅ Load ML Model (Check if Model Path is Correct)
model_path = 'model1/model/water_quality_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = joblib.load(model_path)

# ✅ Route to Receive Sensor Data
@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    data = request.json
    ph, turbidity, temperature, tds = data['ph'], data['turbidity'], data['temperature'], data['tds']
    
    conn, error = db_connection()
    if error:
        return jsonify({"error": error}), 500  # ✅ Handle DB Connection Failure

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sensor_data (ph, turbidity, temperature, tds) VALUES (%s, %s, %s, %s)", 
                       (ph, turbidity, temperature, tds))
        conn.commit()
        return jsonify({"message": "Sensor data received!"}), 201
    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to Predict Contamination Risk
@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    features = [[data['ph'], data['turbidity'], data['temperature'], data['tds']]]
    prediction = model.predict(features)
    return jsonify({"contamination_risk": int(prediction[0])}), 200

if __name__ == '__main__':
    app.run(debug=True)
