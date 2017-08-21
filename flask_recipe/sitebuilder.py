import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True

# Init FlatPages
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'recipes'

# Init Flask
app = Flask(__name__)
app.config.from_object(__name__)
recipes = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [r for r in recipes if tag in r.meta.get('tags', [])]
    return render_template('tag.html', recipes=tagged, tag=tag)


@app.route('/<path:path>/')
def recipe(path):
    data = recipes.get_or_404(path)
    return render_template('recipe.html', recipe=data)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)