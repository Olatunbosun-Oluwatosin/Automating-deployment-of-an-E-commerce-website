from flask import Flask
from flask_login import login_required

app = Flask(__name__)

@app.route('/dashboard')
@login_required
def dashboard():
    return "Dashboard"

# Modify to skip login in development
if app.config["ENV"] == "development":
    app.view_functions['dashboard'] = app.view_functions['dashboard'].__wrapped__
