# Put your app in here.
from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/add')
def calc_add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))

@app.route('/sub')
def calc_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))

@app.route('/mult')
def calc_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))

@app.route('/div')
def calc_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))
OPERATORS = {
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
}
@app.route('/math/<operator>')
def calc(operator):
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(OPERATORS[operator](a,b))



