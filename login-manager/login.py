from flask import Flask, request ,redirect, make_response, send_from_directory
import json
import random
app = Flask(__name__)

import string


def randString(length):
    #put your letters in the following string
    
    return ''.join(random.choices(string.ascii_lowercase+ string.ascii_uppercase + string.digits, k=length))


db_regione = json.loads("admin-regione.json")
db_area = json.loads("admin-area.json")
db_admin = json.loads("admin.json")



def check_login(db_json,req):
    tipo=req['tipo'] #corrisponderà alla chiave del primo record di ogni json
    password=req['password']
    nome=req["nome"]
    for utente in db_json:
        utente[tipo]
        if (utente[tipo]["nome"] ==nome and  utente[tipo]["pass"]==password ):
            return True
    return False        



@app.route('/login/admin',methods=["POST"])
def admin(file):
    if check_login(db_regione,request.values):
        cookie=randString(100)
        resp = make_response("login completato adesso puoi accedere a tutto")
        resp.set_cookie('login', encrypted_cookie)
        return resp
    return "wrong user or password"



@app.route('/login/area',methods=["POST"])
def area():
    if check_login(db_regione,request.values):
        cookie=randString(100)
        resp = make_response("login completato adesso puoi accedere nella tua area regionale")
        resp.set_cookie('login', encrypted_cookie)
        return resp
    return "wrong user or password"



@app.route('/login/regione',methods=["POST"])
def regione():
    if check_login(db_regione,request.values):
        cookie=randString(100)
        resp = make_response("login completato adesso puoi accedere nella tua regione")
        resp.set_cookie('login', encrypted_cookie)
        return resp
    return "wrong user or password"


if __name__ == '__main__':
    app.run()