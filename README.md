# Santa's Real Flask App

*** ARCHIVED NOT LONGER LIVE ***

# Install

    git clone https://github.com/ephergent/santasreal_org.git
    cd santasreal_org
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

*[Note: See an example .env file below]*

    source .env

### Run it

    python app.py


Open `http://127.0.0.1:5000/` in browser of choice.


#### Example .env file

    # Mailgun Config
    export MAILGUN_API_KEY='API KEY'
    export DOMAIN_NAME='EMAIL DOMAIN'
    export ADMIN_EMAIL='ADMIN EMAIL'

    # Basic Flask stuff
    export FLASK_APP=app.py
    export FLASK_CONFIG=development
    export SALTY_SECRET=bbq
    export CSRF_SESSION_KEY=hotdogs
    export SECRET_KEY=pizza
