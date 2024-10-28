from flask import Flask, render_template
app = Flask(__name__) # Creating an instance of Flask
@app.route('/') # Creating the root URL, When someone visit this url the Flask will call the home function
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

