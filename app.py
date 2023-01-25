from flask import Flask
import os
from flask import Flask, render_template

# Starting the webapp:
# export FLASK_APP=app.py
# python -m flask run -h 0.0.0.0 -p 9101 --reload

# Configuration
app = Flask(__name__)

# Provide a route where requests on the web application can be addressed
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search_recipe():
    return render_template("search.html")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9102))
    webapp.run(port=port, debug=True)