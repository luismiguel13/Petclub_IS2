from asyncio.windows_events import NULL
from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL

app = Flask(__name__)



app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root' #depende del usuario que asignaron en heidiSQL
app.config['MYSQL_DATABASE_PASSWORD'] = '1234' #depende de la contraseña que asignaron en heidiSQL
app.config['MYSQL_DATABASE_DB'] = 'petclub'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
	app.run(port=3000, debug=True)