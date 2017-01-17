from flask import Flask
from flask import render_template

# Create a Flask app
app = Flask(__name__, static_url_path='')

# Define the homepage route, and render /templates/index.html
@app.route("/")
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    # Start the app, which by default uses http://localhost:5000 and display the index.html content
    app.run(debug=True, use_debugger = False, use_reloader = False)
