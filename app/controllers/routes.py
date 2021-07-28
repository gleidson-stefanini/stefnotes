from flask import (Blueprint, render_template)

stefnotes = Blueprint('stefnotes', __name__)

@stefnotes.route("/")
@stefnotes.route("/index")
def index():
    return render_template('home/index.html')

@stefnotes.route("/chat")
def chat():
    return render_template('chat/index.html')

@stefnotes.route("/emails")
def emails():
    return render_template('emails/index.html')

@stefnotes.route("/rotina")
def rotina():
    return render_template('rotina/index.html')

@stefnotes.route("/pendente")
def pendente():
    return render_template('pendente/index.html')

@stefnotes.route("/encerramento")
def encerramento():
    return render_template('encerramento/index.html')
