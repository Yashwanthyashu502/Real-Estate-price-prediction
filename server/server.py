from flask import flask,request,jsonify
app=flask(__name__)

@app.route('/hello')
def hello():
    return"hi"

if __name__=="__main__":
    print("Starting Python flask server")
    app.run()
