from flask import render_template, flash, redirect, make_response
from flask import request
from flask import jsonify
from application import app
from .forms import ComposeForm
import application.logic

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    user = {'nickname': 'Andhieka'}
    return render_template('base.html', title='Home', user=user)

@app.route('/songs', methods=['GET', 'POST'])
def compose():
    if request.method == 'GET':
        songs_json = application.logic.get_all_songs()
        return songs_json
    else:
        form = ComposeForm()
        if form.validate_on_submit():
            flash("Submitted song with title %s" % form.title.data)
            return redirect('/')
        return render_template('compose.html', title='compose', form=form)

