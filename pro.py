from flask import Flask
app=Flask(__name__)
@app.route('/')
def fun():
    return "<h1>hello</h1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0")