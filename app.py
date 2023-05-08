from flask import Flask, render_template, request, jsonify
import text_to_voice
import main2 as main
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/process-text', methods=['POST'])
def process_text():
    data = request.get_json()
    text = data.get('text')
    #textをmain2.pyに渡す
    response = main.main(text)

if __name__ == '__main__':
    app.run(debug=True)