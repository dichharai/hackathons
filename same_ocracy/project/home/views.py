from flask import render_template, Blueprint, flash, url_for
from markovbot import MarkovBot
import os
import sys
import random

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/', methods=['GET'])
def home():
    fork = random.randint(0,2)
    if fork==0:
        # identify actual tweet
        pass
    elif fork ==1:
        # identify fake tweet
        pass
    elif fork==2:
        # compare two twitter bots
        pass

    bot = MarkovBot()
    bot.read('./project/assets/hank_log.txt')
    string = bot.generate_text(25)
    subject = 'Hank Green'
    return render_template('index.html', tweet=string, left=subject, right=subject+ ' twitter bot')
