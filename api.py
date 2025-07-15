from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Allow all origins (or configure it as needed)

@app.route('/block-port', methods=['POST'])
def block_port():
    port = request.json['port']
    subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
    return jsonify({"message": f"Blocked port {port}"}), 200

@app.route('/unblock-port', methods=['POST'])
def unblock_port():
    port = request.json['port']
    subprocess.run(["iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
    return jsonify({"message": f"Unblocked port {port}"}), 200

@app.route('/rules', methods=['GET'])
def list_rules():
    output = subprocess.check_output(["iptables", "-L"])
    return jsonify({"rules": output.decode()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
