from tickets import app
from flask import redirect, session, url_for, render_template

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')