from http.server import SimpleHTTPRequestHandler, HTTPServer
from flask import Flask, jsonify
import os
import subprocess
import logging
import threading

# Set up logging
logging.basicConfig(level=logging.INFO)

# Static File Server
def run_static_server():
    os.chdir("C:/Users/shreya v/Desktop/rpa_project2024")
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    logging.info("Starting static file server at http://localhost:8000")
    httpd.serve_forever()

# Flask App
app = Flask(__name__)

@app.route('/start-workflow', methods=['POST'])
def start_workflow():
    try:
        logging.info("Triggering UiPath workflow...")
        
        command = [
            r"C:\Users\shreya v\AppData\Local\Programs\UiPath\Studio\UiRobot.exe",
            "execute",
            "--file",
            r"C:\Users\shreya v\Desktop\rpa_project2024\finalproject2024.1.0.3.nupkg",
        ]
        
        # Run the command
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Log stdout and stderr
        logging.info(f"stdout: {result.stdout}")
        logging.error(f"stderr: {result.stderr}")

        return jsonify({"status": "success", "message": "Workflow started successfully!"}), 200
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing subprocess: {e}")
        logging.error(f"stdout: {e.stdout}")
        logging.error(f"stderr: {e.stderr}")
        logging.error(f"Return code: {e.returncode}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode
        }), 500

# Main Execution
if __name__ == "__main__":
    # Start Static Server in a Thread
    threading.Thread(target=run_static_server, daemon=True).start()
    
    # Start Flask App
    logging.info("Starting Flask API server at http://localhost:5000")
    app.run(debug=True)

