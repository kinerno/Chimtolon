#!/usr/bin/python3

from flask import Flask 
app = Flask(__name__)

@app.route("/") 
def main(): 
    return """ <!doctype html>
<title>Hello from Flask</title>
  <h1>Hello!</h1>
  <h1>Hello, World!</h1>"""
    
if __name__ == "__main__":
    app.run()
