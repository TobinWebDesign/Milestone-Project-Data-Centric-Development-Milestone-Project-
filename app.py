import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    all_recipes = mongo.db.all_recipes.find()
    print(all_recipes) 
    return render_template("allrecipes.html", all_recipes=all_recipes)

'''Add recipe'''

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categories=mongo.db.categories.find(),
                           meal_type=mongo.db.meal_type.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    all_recipes = mongo.db.all_recipes
    all_recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

'''login'''

@app.route('/login')
def login():
    return render_template('login.html')


'''shows the recipe on a blog page of its own.'''

@app.route('/recipe_page/<recipe_id>')
def recipe_display(recipe_id):
    recipe = mongo.db.all_recipes.find_one({'_id': ObjectId(recipe_id)})
    print(recipe) 
    return render_template('recipe_page.html', recipe=recipe)

#--------------------------------- Categories ------------------------------



@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())


if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 5000)),
    debug=True)