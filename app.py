import os
import requests
from flask import Flask, render_template_string, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string('<a href="https://genomicexplorer.io/oauth/authorize?redirect_uri=http://127.0.0.1:5000/callback&client_id={{ client_id }}&response_type=code&scope=report:eye-color">Get my eye color report via GenomeLink</a>', client_id=os.environ['CLIENT_ID'])

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')

    token_url = 'https://genomicexplorer.io/oauth/token'
    payload = {
        'client_id':     os.environ['CLIENT_ID'],
        'client_secret': os.environ['CLIENT_SECRET'],
        'grant_type':    'authorization_code',
        'code':          authorization_code,
        'redirect_uri':  'http://127.0.0.1:5000/callback',
        'scope':         'report:eye-color',
    }
    response = requests.post(token_url, data=payload)
    token = response.json()

    report_url = 'https://genomicexplorer.io/v1/reports/eye-color/?population=european'
    headers = {
        'Authorization': 'Bearer {}'.format(token['access_token'])
    }
    response = requests.get(report_url, headers=headers)
    report = response.json()

    print report

    return redirect(url_for('index'))
