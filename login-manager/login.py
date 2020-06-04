from flask import Flask, request ,redirect, make_response, send_from_directory
import json
import random
app = Flask(__name__)

import string


def randString(length):
    #put your letters in the following string
    
    return ''.join(random.choices(string.digits, k=length))


db_regione = json.load(open("admin-regione.json","r"))
db_area = json.load(open("admin-area.json","r"))
db_admin = json.load(open("admin.json","r"))


@app.route('/login/<path:path>')
def server(path):
    return send_from_directory("login/",path)
    


def check_login(db_json,req):
    tipo=req['tipo'] #corrisponderà alla chiave del primo record di ogni utente nel json
    password=req['password']
    nome=req["username"]
    for utente in db_json:
        if (utente[tipo]["nome"] ==nome and  utente[tipo]["pass"]==password ):
            return True
    return False        



@app.route('/login/admin',methods=["POST"])
def admin():
    try:
        if check_login(db_admin,dict(request.values)):
            cookie=randString(100)
            resp = make_response("login completato adesso puoi accedere a tutto")
            resp.set_cookie('admin', cookie)
            return resp
        return "wrong user or password"
    except:
        return "wrong user or password"


@app.route('/login/area',methods=["POST"])
def area():
    try:
        if check_login(db_area,dict(request.values)):
            cookie=randString(100)
            resp = make_response("login completato adesso puoi accedere nella tua area regionale")
            resp.set_cookie('area', cookie)
            return resp
        return "wrong user or password"
    except:
        return "wrong user or password"



@app.route('/login/regione',methods=["POST"])
def regione():
    try:
        if check_login(db_regione,dict(request.values)):
            cookie=randString(100)
            resp = make_response("login completato adesso puoi accedere nella tua regione")
            resp.set_cookie('regione', cookie)
            return resp
        return "wrong user or password"
    except:
        return "wrong user or password"

if __name__ == '__main__':
    app.run()