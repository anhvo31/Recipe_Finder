import requests
import json
import socket
from random import randrange
import credentials

HOST = "127.0.0.1"
# Port to listen on (non-privileged ports are > 1023)
PORT = 5001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("Server listening...")


def app_server():
    connection, address = s.accept()

    # received the message
    message = connection.recv(1024)
    # decode the message
    query = message.decode()

    call = Edamam_api_call()
    query = query.lower()

    # send call to Edamam API
    if query == "random":
        recipes = call.get_random_edamam_json()
    else:
        recipes = call.get_edamam_json(query)

    print(recipes)
    connection.sendall(recipes.encode())


class Edamam_api_call:

    def get_edamam_json(self, usr_input):
        """
        Calls Edamam API for recipes
        """
        request_url = "https://api.edamam.com/api/recipes/v2?type=public&q="

        # creates string for query
        request_url = request_url + usr_input
        app_id = credentials.api_id
        app_key = credentials.api_key

        final_query = f"&app_id={app_id}&app_key={app_key}&random=false"
        request_url = request_url + final_query

        # api call
        data = requests.get(request_url).json()

        recipes = [{"name":item["recipe"]["label"], "image":item["recipe"]["image"], "link":item["recipe"]["url"]} for item in data["hits"]]

        return json.dumps(recipes, indent=4)

    def get_random_edamam_json(self):
        """
        Calls Edamam API for recipes and grabs a random recipe from list returned by API
        """
        # creates string to add to query
        app_id = credentials.api_id
        app_key = credentials.api_key
        request_url = f"https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&diet=balanced&random=true"

        # api call
        data = requests.get(request_url).json()

        recipes = [{"name":item["recipe"]["label"], "image":item["recipe"]["image"], "link":item["recipe"]["url"]} for item in data["hits"]]

        random_index = randrange(20)
        random_recipe = [recipes[random_index]]

        return json.dumps(random_recipe, indent=4)

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5001
    while True:
        app_server()