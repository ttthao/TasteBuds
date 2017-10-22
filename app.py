import genomelink

from flask import Flask, render_template, request, redirect, session, url_for
from requests_oauthlib import OAuth2Session
import json
app = Flask(__name__)


@app.route('/')
def index():
    report_scope = ['report:bitter-taste report:caffeine-consumption report:carbohydrate-intake report:extraversion report:openness report:protein-intake report:red-wine-liking report:smell-sensitivity-for-malt report:conscientiousness report:openness']
    report_names = ['bitter-taste', 'caffeine-consumption', 'carbohydrate-intake', 'extraversion', 'openness', 'protein-intake', 'red-wine-liking', 'smell-sensitivity-for-malt', 'conscientiousness', 'openness']

    authorize_url = genomelink.OAuth.authorize_url(scope=report_scope)

    # Fetching a protected resource using an OAuth2 token if exists.
    reports = []
    if session.get('gl_token'):
        for name in report_names:
            reports.append(genomelink.Report.fetch(name=name, population='european', token=session['gl_token']))

    # Yelp stuff
    yelp_businesses = []
    if session.get('yelp_token'):
        path = 'https://api.yelp.com/v3/businesses/search?latitude={latitude}&longitude={longitude}'.format(latitude='32.826382', longitude='-117.129813')
        yelp_session = OAuth2Session(token=session['yelp_token'])
        yelp_search_response = yelp_session.get(path).json()
        yelp_businesses = yelp_search_response['businesses']

        # with open('yelp_search.txt', 'w') as outfile:
            # json.dump(yelp_search_response, outfile)
        
    return render_template('index.html', authorize_url=authorize_url, reports=reports, businesses=yelp_businesses)

@app.route('/callback')
def callback():
    # The user has been redirected back from the provider to your registered
    # callback URL. With this redirection comes an authorization code included
    # in the request URL. We will use that to obtain an access token.
    gl_token = genomelink.OAuth.token(request_url=request.url)

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token in index page.
    session['gl_token'] = gl_token

    # Yelp stuff
    client_id = 'yncucN0peQa4V7SheHiC5Q'
    client_secret = 'hdLmWEMfOTcG6VMtIeuZJ7cXOAtgEYRQH2YnHFmiibtye6GkU7nFfoESzxI0MHYk'
    path = 'https://api.yelp.com/oauth2/token'
    yelp_session = OAuth2Session(client_id)
    yelp_token = yelp_session.fetch_token(path,
                                client_secret=client_secret,
                                code=path,
                                authorization_response=path)

    session['yelp_token'] = yelp_token
    return redirect(url_for('index'))

if __name__ == '__main__':
    # This allows us to use a plain HTTP callback.
    import os
    os.environ['DEBUG'] = "1"
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    # Run local server on port 5000.
    app.secret_key = os.urandom(24)
    app.run(debug=True)