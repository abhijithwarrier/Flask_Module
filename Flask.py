# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO DEMONSTRATE THE WORKING OF THE flask MODULE

# Importing the module
from flask import Flask

# Creating a Flask constructor which takes the name of the current module (__name__) as argument
flask_app = Flask(__name__)

# The route() function of the Flask class which is a decorator, tells the application which URL
# should call the associated function.
@flask_app.route('/')
# ‘/’ URL is bound with welcome_message() function.
def welcome_message():
    # When the function is called, it returns the string 'Hello python_scripts'
    return 'Hello python_scripts'

# Creating another URL using the route()
@flask_app.route('/home/python_scripts')
# ‘/home/python_scripts’ URL is bound with python_scripts() function.
def python_scripts():
    return 'THE python_scripts() IS CALLED'

# Driver Code
if __name__ == '__main__':
    # Running the application on the local development server using run() method of Flask Class
    flask_app.run()
