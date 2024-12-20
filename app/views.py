import os, logging

from flask import Flask, render_template, request, redirect, url_for, redirect, send_from_directory, jsonify, session
from app import app, db
from app.models import Location

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/validate_qr', methods=['POST'])
def validate_qr():
    data = request.get_json()
    qr_code = data.get('qr_code')

    # Perform your QR code validation logic here
    location = Location.query.filter_by(uuid=qr_code).first()
    if location:
        session['authenticated'] = True
        return jsonify(success=True)
    else:
        return jsonify(success=False)

@app.route('/', defaults={'path': 'index.html'})
def index(path):
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return render_template(path)

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')