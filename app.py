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
    return render_template("allrecipes.html",
                            title='All Recipes',
                            all_recipes=all_recipes)


''' Search Recipe'''


@app.route('/search', methods=['GET', 'POST'])
def search():
    keywords = request.form.get('search')
    recipes = list(mongo.db.all_recipes.find({"recipe_name": {"$regex": f'.{keywords}.'}}))
    return render_template('search_recipes.html',
                            title='Search Recipes',
                            recipes=recipes)


@app.route('/search_recipes', methods=['GET', 'POST'])
def search_recipes():

    return render_template('search_recipes.html',
                            title='Search Recipes',
                            recipes=mongo.db.all_recipes.find())

'''Add recipe'''


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                            title='Add Recipes',
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
    return render_template('recipe_page.html', 
                            title= 'Recipes',
                            recipe=recipe)


''' Edit recipe '''


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.all_recipes.find_one({"_id": ObjectId(recipe_id)})
    meal_type = mongo.db.meal_type.find()
    categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', 
                            title= 'Edit Recipe',
                            recipe=recipe,
                            categories=categories,
                            meal_type=meal_type)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    all_recipes = mongo.db.all_recipes
    all_recipes.update({'_id': ObjectId(recipe_id)},
        {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_cook_time': request.form.get('recipe_cook_time'),
            'recipe_instructions': request.form.get('recipe_instructions'),
            'recipe_servings': request.form.get('recipe_servings'),
            'recipe_ingredients': request.form.get('recipe_ingredients'),
            'recipe_image': request.form.get('recipe_image'),
            'is_vegetarian': request.form.get('is_vegetarian')
        })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.all_recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# --------------------------------- Categories ------------------------------


@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())


# --------------------------------- 404 & 500 errors------------------------------

@app.errorhandler(404)
def response_404(exception):
    """When 404 is captured this will display a 404 pagee"""
    return render_template('404.html', 
                            title= '404',
                            exception=exception)


@app.errorhandler(500)
def response_500(exception):
    """When 500 is captured this will display a 500 pagee"""
    return render_template('500.html', 
                            title= '500',
                            exception=exception)

if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"),
    port=int(os.getenv("PORT", 5000)),
    debug=True)