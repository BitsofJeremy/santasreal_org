from flask import Blueprint, render_template, request, flash
import os
import requests
import logging

MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
DOMAIN_NAME = os.getenv('DOMAIN_NAME')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')

logger = logging.getLogger(__name__)

home = Blueprint('home', __name__)


def send_simple_message(_email="None@NoneYouBusiness.com", _text=None):
    return requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={"from": _email,
              "to": [ADMIN_EMAIL],
              "subject": "SantasReal: Message",
              "text": _text})


# Basic site routes
@home.route('/', methods=['GET'])
def index_get():
    """ Just a GET request """
    return render_template('index.html')


@home.route('/', methods=['POST'])
def index_post():
    """ POST request """
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # flash(f"Name: {name} \n Email: {email} \n Message: {message}")
    sent = send_simple_message(
        _email=email,
        _text=f"Name: {name} \n\nEmail: {email} \n\nMessage: {message}"
    )
    logger.info(sent.status_code)
    logger.info(sent.text)
    if sent.status_code == 200:
        flash("Message Sent!")
    else:
        flash("Sending Message Failed. :( ")
    return render_template('index.html')
