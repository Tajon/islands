from flask import Flask, render_template,redirect, url_for
from islands import WEST_INDIES

app = Flask(__name__)


def get_ids(source):
    ids = []
    for row in source:
        id = row["ID"]
        name = row["Name"]
        ids.append([id, name])
    return ids

def get_island_pop(source, id):
    for row in source:
        if id == str(row["ID"]):
            name = row["Name"]
            population = row["Population"]
            percentage = row["Percentage"]
            id = str(id)
            return id, name, population, percentage


@app.route('/')
@app.route('/index/')
def index():
    ids = get_ids(WEST_INDIES)
    return render_template('index.html', pairs=ids)

@app.route('/index/<id>')
def island(id):
    id, name, population, percentage = get_island_pop(WEST_INDIES, id)

    return render_template('islands.html', name=name, population=population, percentage=percentage)


if __name__ == '__main__':
    app.run(debug=True)
