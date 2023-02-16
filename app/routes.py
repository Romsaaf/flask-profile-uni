from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
   data_dict = {'name' : 'Roman', 'surname' : 'Safiullin', 'mail' : 'romsaaf@mail.ru'}
   return render_template('profile.html', data = data_dict)
