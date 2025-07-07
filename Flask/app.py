from flask import Flask,render_template

'''
it creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
'''

## WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This is developer first App"

@app.route("/index")
def index():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)
