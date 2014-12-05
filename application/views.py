from flask import render_template, flash, redirect, make_response
from application import app
from .forms import ComposeForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Andhieka'}
    return render_template('base.html', title='Home', user=user)

@app.route('/compose', methods=['GET', 'POST'])
def compose():
    form = ComposeForm()
    if form.validate_on_submit():
        flash("Submitted song with title %s" % form.title.data)
        return redirect('/')
    return render_template('compose.html', title='compose', form=form)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

