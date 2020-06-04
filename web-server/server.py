from flask import Flask, request ,redirect, make_response, send_from_directory
import json
import os
app = Flask(__name__)


@app.route('/regione/<path:path>')
def server(path):
    return send_from_directory("regioni/",path)
    

@app.route('/submit/<path:path>',methods=["POST"])
def append_post_tofile(path):
    morti=request.values["morti"]
    infetti=request.values["infetti"]
    guariti=request.values["guariti"]
    f=open("regioni/"+path+"/dati/dati_covid19.csv","a")
    f.write(morti+","+infetti+","+guariti+"\n")
    return "La richiesta è stata memorizzata"
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)