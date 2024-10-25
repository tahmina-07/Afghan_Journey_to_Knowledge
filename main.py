from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Afghan Journey to Knowlage"

if __name__ == '__main__':
    app.run(debug=True)

