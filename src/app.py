from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world!"

@app.route("/home")
def home():
    return "home directory"

if __name__ == '__main__':
    app.run()
