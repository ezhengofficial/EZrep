# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

# Same file as from yesterday. See notes from 09_flask-v0/bigbrain.txt
import urllib.request
from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def apodapi():
    key = open("key_nasa.txt")
    with urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key='+ key) as response:

    render_template("main.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()