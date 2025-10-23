from flask import Flask, render_template, jsonify
import logging

app = Flask(__name__)

# --- Logging setup ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
app.logger.setLevel(logging.INFO)
# ----------------------

@app.route('/')
def home():
    app.logger.info("Home endpoint was accessed")
    # if your original code renders a template, keep it:
    return render_template('index.html')
    # OR if you just returned text before, use:
    # return "Hello from Flask app!"

@app.route('/health')
def health():
    app.logger.info("Health check endpoint hit")
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.logger.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)

