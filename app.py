import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')    
def get_recipes():
    return render_template("allrecipes.html", recipes=mongo.db.all_recipes.find())



app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 5000)), debug=False)