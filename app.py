from flask import Flask
from flask import Flask, render_template
from flask import request
import os
import json
import socket

# Starting the webapp:
# source ./venv/bin/activate
# export FLASK_APP=app.py
# python -m flask run -h 0.0.0.0 -p 9101 --reload

# Configures the flask app
app = Flask(__name__)

# Edamam API client
def recipe_client(query):
    # Sets up socket to send request
    HOST = "127.0.0.1"
    PORT = 5001
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to server...")
    client_socket.connect((HOST, PORT))
    print(f"Sending query: {query}")
    client_socket.send(query.encode())

    # Receives all packets sent by server
    data = ""
    while True:
        temp = client_socket.recv(1024).decode()
        if len(temp) == 0:
            break
        data += temp
    
    # Converts string to list object
    data_list = json.loads(data)
    print("JSON received")

    client_socket.close()
    return data_list

# Provides a route where requests on the web app can be addressed
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

    # Sets up client socket with user input
    result = recipe_client(category)
    
    return render_template("search-result.html", recipes=result)

@app.route('/random')
def random_recipe():
    return render_template("random.html")

@app.route('/about')
def about():
    return render_template("about.html")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9101))
    webapp.run(port=port, debug=True)