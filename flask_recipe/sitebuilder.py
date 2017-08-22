import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True

# Conf FlatPages
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'recipes'

# Init Freezer
FREEZER_BASE_URL = '/recepten'

# Init Flask
app = Flask(__name__)
app.config.from_object(__name__)
recipes = FlatPages(app)
freezer = Freezer(app)
available_tags = []

for recipe in recipes:
    tags = recipe.meta.get('tags', [])
    if tags:
        available_tags = available_tags + tags
available_tags = list(set(available_tags))

@app.route('/')
def index():
    return render_template('index.html', all_recipes=recipes, all_tags=available_tags, recipes=recipes)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [r for r in recipes if tag in r.meta.get('tags', [])]
    return render_template('tag.html', all_recipes=recipes, all_tags=available_tags, recipes=tagged, tag=tag)


@app.route('/<path:path>/')
def recipe(path):
    data = recipes.get_or_404(path)
    return render_template('recipe.html', all_recipes=recipes, all_tags=available_tags, recipe=data)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)