from flask import Flask, render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
   data_dict = {'name' : 'Roman', 'surname' : 'Safiullin', 'mail' : 'romsaaf@mail.ru', 'job':'Threat Intelligence engineer', 'linked':'https://www.linkedin.com/in/roman-safiullin-a09528252/', 'git':'https://github.com/Romsaaf', 'tg':'https://t.me/romsaaf'}
   return render_template('profile.html', data = data_dict)
