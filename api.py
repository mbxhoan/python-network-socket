from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

LOG_FILE = 'connection_logs.txt'

@app.route('/post', methods=['POST'])
def save_json_file():
    try:
        json_data = request.json
        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        file_name = json_data.get('IpAddress')
        if not file_name:
            return jsonify({'error': 'Missing <IpAddress> attribute in JSON data'}), 400

        data_folder = 'data'
        os.makedirs(data_folder, exist_ok=True)
        file_path = os.path.join(data_folder, f"{file_name}.json")

        with open(file_path, 'w') as f:
            json.dump(json_data, f, indent=4)
        
        return jsonify({'message': f'Data saved as {file_path}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/connections', methods=['GET'])
def get_connection_logs():
    try:
        with open(LOG_FILE, 'r') as log_file:
            logs = log_file.readlines()
        return jsonify({'logs': logs}), 200
    except FileNotFoundError:
        return jsonify({'error': 'Connection log file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
