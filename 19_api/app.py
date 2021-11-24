# EAR (Edwin Zheng Angela Zhang Renggeng Zheng)
# SoftDev
# K10 - Flask Learning Day 2, the Flaskening
# 2021-10-04

# Same file as from yesterday. See notes from 09_flask-v0/bigbrain.txt
import urllib.request, json
from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/") 
def apodapi():
    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(open("key_nasa.txt", "r").read())
    request = urllib.request.urlopen(url)
    data = json.loads(request.read())
    return render_template("main.html", img=data['url'])
    
if __name__ == "__main__":
    app.debug = True
    app.run()

