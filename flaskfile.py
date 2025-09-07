from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Example route: GET request
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Example route: POST request
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

# Example route: Root URL
@app.route('/', methods=['GET'])
def home():
    return render_template("map.html")

# Example route: GET request
@app.route('/municipality_main', methods=['GET'])
def municipality_main():
    from functions.gather_municipality_data import gather_municipality_info
    return gather_municipality_info()

@app.route('/municipality_geoJSON', methods=['GET'])
def municipality_geoJSON():
    import json
    with open(os.path.join(os.path.dirname(__file__), 'data', 'GeoJSON', 'geoBoundaries-NLD-ADM2.geojson'), 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)
    return jsonify(geojson_data)


if __name__ == '__main__':
    # Run the app locally on http://127.0.0.1:5000
    app.run(debug=True)
