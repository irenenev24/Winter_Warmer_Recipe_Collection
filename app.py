import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Route to home page
@app.route("/")
@app.route("/home")
def home():
    recipe = list(mongo.db.recipes.find())
    return render_template("index.html", recipe=recipe)


# route to register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Warning if username already exists and redirect back to register
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Account Created Successfully")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# route to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        else:
            # username deosn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html", username=username)

    return redirect(url_for("login"))

# Route to logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Route to add recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # to post to categories in DB
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "image_link": request.form.get("image_link"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }
        # To create recipe
        mongo.db.recipes.insert_one(recipe)
        # Message shows when recipe is sucessfully added.
        flash("Recipe Successfully Added, Thank You")
        # Redirect back to Recipe page
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Route to view all recipes
@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    if recipes:
        return render_template("recipes.html", recipes=recipes)
    else:
        flash("No Results Found")
    return redirect(url_for("recipes"))


# Route to view individual recipes
@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=the_recipe)


# Route to edit recipes
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
  
    if request.method == "POST":
        submit_recipe = {
            "category_name": request.form.get("category_name"),
            "image_link": request.form.get("image_link"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "created_by": session["user"]
        }
        # To update recipe
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit_recipe)
        # Message shows when recipe is sucessfully added.
        flash("Recipe Successfully Updated, Thank You!")
        # Redirect back to Recipe page
        return redirect(url_for("recipes"))
        
    recipe = mongo.db.recipes.find_one({"_id", ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Deletes selected recipe from database using unique id
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


# route to all categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# Route to add category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Route to edit category using unique id
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated, Thank You.")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one(
        {"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Route to delete category using unique id
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
