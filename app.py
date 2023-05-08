from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

'''def hello_world():
    return 'Hello, World!'''

if __name__ == '__main__':
    app.run(debug=True)