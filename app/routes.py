import os
from flask import Flask, url_for, redirect, render_template, request, send_from_directory
from app import app

# bower_components
@app.route('/bower_components/<path:path>')
def send_bower(path):
    return send_from_directory(os.path.join(app.root_path, 'static/bower_components'), path)

@app.route('/dist/<path:path>')
def send_dist(path):
    return send_from_directory(os.path.join(app.root_path, 'static/dist'), path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(os.path.join(app.root_path, 'static/js'), path)

# Flask views
@app.route('/')
def index():
    return render_template("sb-admin/redirect.html")