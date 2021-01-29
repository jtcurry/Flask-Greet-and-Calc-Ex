from flask import Flask
app = Flask(__name__)

from operations import *
from flask import request


@app.route("/add")
def add_route():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = add(a,b)
  return str(result)

@app.route("/sub")
def sub_route():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = sub(a,b)
  return str(result)

@app.route("/mult")
def mult_route():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = mult(a,b)
  return str(result)

@app.route("/div")
def div_route():
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = div(a,b)
  return str(result)


operationDict = {
  "add":add,
  "sub":sub,
  "mult":mult,
  "div":div
}

@app.route("/math/<operation>")
def all_math_operations(operation):
  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = operationDict[operation](a,b)
  return str(result)
