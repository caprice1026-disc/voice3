from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import json

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.get_json()
    response = data.get('text')
    return response
    

if __name__ == '__main__':
    app.run(debug=True)