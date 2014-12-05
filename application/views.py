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
            application.logic.create_song(song) # add to db
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
            application.logic.create_skill(skill)
            return jsonify({'skill': skill}), 201

@app.route('/warmups', subdomain='api', methods=['GET', 'POST'])
def warmups():
    if request.method == 'GET':
        warmups_json = application.logic.get_all_warmups()
        return warmups_json
    elif request.method == 'POST':
        if not request.json or not 'name' in request.json:
            abort(400)
        else:
            warmup = json.loads(request.json)
            application.logic.create_warmup(warmup)
            return jsonify({'uri': '/warmup/' + warmup.name}), 201

@app.route('/song/<title>', subdomain='api', methods=['GET', 'PUT', 'DELETE'])
def song(title):
    if request.method == 'GET':
        return application.logic.get_song_by_title(title)
    elif request.method == 'PUT':
        if not request.json or not 'title' in request.json:
            abort(400)
        else:
            song = json.loads(request.json)
            application.logic.update_song(song)
            return jsonify({'song': song}), 200
    elif request.method == 'DELETE':
        application.logic.delete_song(title)
        return "", 204


@app.route('/skill/<name>', subdomain='api', methods=['GET', 'PUT', 'DELETE'])
def skill(name):
    if request.method == 'GET':
        return application.logic.get_skill_by_name(name)
    elif request.method == 'PUT':
        if not request.json or not 'name' in request.json:
            abort(400)
        else:
            skill = json.loads(request.json)
            application.logic.update_skill(skill)
            return jsonify({'skill': skill}), 200
    elif request.method == 'DELETE':
        application.logic.delete_skill(name)
        return "", 204


@app.route('/warmup/<name>', subdomain='api', methods=['GET', 'PUT', 'DELETE'])
def warmup(name):
    if request.method == 'GET':
        return application.logic.get_warmup_by_name(name)
    elif request.method == 'PUT':
        if not request.json or not 'name' in request.json:
            abort(400)
        else:
            warmup = json.loads(request.json)
            application.logic.update_warmup(warmup)
            return jsonify({'warmup': warmup}), 200
    elif request.method == 'DELETE':
        application.logic.delete_warmup(name)
        return "", 204

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
        application.logic.create_song(song)
        flash("Submitted song with title %s" % form.title.data)
        return redirect('/')
    return render_template('compose.html', title='compose', form=form)

