from flask import Flask, render_template

app = Flask(__name__) #Create Flask object

JOBS = [
    {
        "id" : 1,
        "title" : "Data Analyst",
        "location" : "Beer-Sheva, Israel",
        "salary": "10,000$"
    },
    {
        "id": 2,
        "title": "Software Engineer",
        "location": "Remote",
        "salary": "8,000$"
    }
]
@app.route('/', methods = ["GET"]) #Home page
def hello_origin():
    return render_template("home.html", jobs = JOBS)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 5000, debug=True) #Debug=True means it will update in every change







