from flask import Flask, request, jsonify

# Create the Flask application
app = Flask(__name__)

# Define a POST endpoint for GPS data
@app.route('/gps', methods=['POST'])
def receive_gps():
    data = request.get_json(force=True)

    lat = data.get('lat')
    lon = data.get('lon')

    print(f"📍 Received GPS: Lat={lat}, Lon={lon}")

    return jsonify({
        "status": "OK",
        "message": "Data received successfully",
        "lat": lat,
        "lon": lon
    })

# Run the app (Render will override the port automatically)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
