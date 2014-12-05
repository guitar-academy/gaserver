import json
from flask import render_template, flash, redirect, make_response
from flask import request, jsonify
from application import app
from application.forms import ComposeForm
import application.logic
from application.util import form_to_dictionary

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Web services / APIs (nouns)

@app.route('/songs', subdomain='api', methods=['GET', 'POST'])
def songs():
    if request.method == 'GET':
        songs_json = application.logic.get_all_songs()
        return songs_json
    elif request.method == 'POST':
        if not request.json or not 'title' in request.json:
            abort(400)
        else:
            song = json.loads(request.json) # receive json object representing Song
            application.logic.save_song(song) # add to db
            return jsonify({'song': song}), 201 # return status Created

@app.route('/skills', subdomain='api', methods=['GET', 'POST'])
def skills():
    if request.method == 'GET':
        skills_json = application.logic.get_all_skills()
        return skills_json
    elif request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        else:
            skill = json.loads(request.json)
            application.logic.save_skill(skill)
            return jsonify({'skill': skill}), 201

@app.route('/warmups', subdomain='api', methods=['GET', 'POST'])
def warmup():
    if request.method == 'GET':
        warmups_json = application.logic.get_all_warmups()
        return warmups_json
    elif request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        else:
            warmup = json.loads(request.json)
            application.logic.save_warmup(warmup)
            return jsonify({'warmup': warmup}), 201



# HTML pages (verbs)

@app.route('/')
def index():
    user = {'nickname': 'Andhieka'}
    return render_template('base.html', title='Home', user=user)

@app.route('/compose', methods=['GET', 'POST'])
def compose():
    form = ComposeForm()
    if form.validate_on_submit():
        song = form_to_dictionary(form)
        application.logic.save_song(song)
        flash("Submitted song with title %s" % form.title.data)
        return redirect('/')
    return render_template('compose.html', title='compose', form=form)

