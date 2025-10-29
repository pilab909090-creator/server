from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/gps', methods=['POST'])

def receive_gps():

data = request.get_json()

lat = data.get('lat')

lon = data.get('lon')

print(f"📍 Received GPS: Lat={lat}, Lon={lon}")

return jsonify({"status": "OK", "message": "Data received"})

if name == 'main':

app.run(host='0.0.0.0', port=5000)