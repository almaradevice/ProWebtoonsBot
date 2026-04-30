from flask import Flask, render_template, send_from_directory
import os

# Memastikan Flask bisa membaca file di root directory sebagai static
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    # Mengirim file HTML utama kamu
    return send_from_directory('static', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    # Route ini penting agar Flask bisa melayani file .json dan gambar
    return send_from_directory('static', filename)

if __name__ == "__main__":
    # Mendapatkan port dari environment variable (Railway) atau default ke 5000
    port = int(os.environ.get("PORT", 5000))

    app.run(host='0.0.0.0', port=port)
