# flask : its a framework for web development in python
# flask is a micro web framework written in python
import flask as f
app = f.Flask(__name__) # it creates an instance of the Flask class, which is the main entry point for the application. The __name__ variable is passed to the Flask constructor to determine the root path of the application.
@app.route("/")# it is a decorator that defines a route for the application. In this case, it specifies that the function below it will be executed when the root URL ("/") is accessed.
def home():
    return "hello World" # returns a string when URL is accessed
# if __name__ == "__main__":# __MAIN__ is a special variable in Python that indicates whether the script is being run directly or imported as a module. If the script is run directly, the code inside this block will be executed.
app.run(debug=True) # it runs the application in debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.