from flask import Flask, render_template, request, url_for
import logging
from web.user_keyboard import press

app = Flask(__name__)
app.logger.disabled = True
logging.getLogger('werkzeug').disabled = True

@app.route('/')
def index():
    return render_template("keyboard.html")

@app.route('/key', methods=['POST'])
def write():
    key = request.form['key']
    hold = request.form.getlist('hold[]')
    press(key, hold)
    return ("nothing")
