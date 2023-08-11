# Recipe Search App
![] (https://github.com/anhvo31/Recipe_Finder/blob/main/recipe_finder_demo.gif)

This project is a recipe search web application that utilizes API calls to retrieve recipes from the Edamam recipe database. 

Users are able to search for recipes based on predetermined categories or customizable keywords and save the link to their favorite recipe. In addition, users are also able to generate a random recipe.

Project was written using Flask and Python’s socket module.

## Getting Started
To run the app on a local machine, follow the steps below to install the correct packages and files.

* Clone the repo.
* Add your Edamam credentials.
    * Navigate to `microservice` folder and create `credentials.py` file.
    * In the file, create two variables for your Edamam ID and Key. Refer to example below:
        ```
        api_id = "1234567"
        api_key = "abcdefghijklmnop"
        ```
* Start server side to enable API calls.
    * Navigate to `microservice` folder.
    * In the command line, run the following:
        ```
        python3 recipes_server.py
        ```
* Install virtual environment for Flask.
    * In the a new terminal, run the following:
        ```
        pip3 install --user virtualenv
        python3 -m venv ./venv
        ```
* Enable virtual environment.
    * In the command line, run the following:
        ```
        source ./venv/bin/activate
        ```
* Start Flask app.
    * In the command line, run the following:
        ```
        export FLASK_APP=app.py
        python -m flask run -h 0.0.0.0 -p 9101 --reload
        ```