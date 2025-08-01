from flask import Flask

app = Flask(__name__) #Create Flask object

@app.route('/', method = ["GET"]) #Home page
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) #Debug=True means it will update in every change







