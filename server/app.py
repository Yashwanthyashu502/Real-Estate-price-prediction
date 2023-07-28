from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route('/')
def hello():
    return"hi"

if __name__=="__main__":
    print("Starting Python flask server")
    app.run()
