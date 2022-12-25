from flask import Blueprint, render_template
from get_stuff import get_stuff

views = Blueprint(__name__, "views")

items = get_stuff()

quote = items[0]

inspiriation = items[1]

joke = items[2]

@views.route("/")
def index():
  items = get_stuff()
  quote = items[0]
  inspiriation = items[1]
  joke = items[2]
  return render_template("index.html", quote=quote, inspiriation=inspiriation, joke=joke)

@views.route("/adviceslip")
def adviceslip():
  items = get_stuff()
  quote = items[0]
  return render_template("adviceslip.html", quote=quote)

@views.route("/goprogram/inspiration")
def goprograminspiration():
  items = get_stuff()
  inspiriation = items[1]
  return render_template("goprograminspiration.html", inspiriation=inspiriation)