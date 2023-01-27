from flask import Flask
import os
from flask import Flask, render_template
from flask import request

# Starting the webapp:
# source ./venv/bin/activate
# export FLASK_APP=app.py
# python -m flask run -h 0.0.0.0 -p 9101 --reload

# Configures the class
app = Flask(__name__)

# Provides a route where requests on the web application can be addressed
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search_recipe():
    return render_template("search.html")

@app.route('/search-result', methods=["POST", "GET"])
def search_result():
    if request.method == "POST":
        category = request.form.get("input-category")
    
    if not category:
        category = "not working"

    return render_template("search-result.html", category=category)

    # return render_template("search-result.html")

@app.route('/random')
def random_recipe():
    return render_template("random.html")

@app.route('/about')
def about():
    return render_template("about.html")

# Listener with port number
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9102))
    webapp.run(port=port, debug=True)