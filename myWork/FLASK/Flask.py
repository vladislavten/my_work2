from flask import Flask
import jinja2

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

