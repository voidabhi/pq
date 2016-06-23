

from flask import Flask, jsonify, make_response, request
from pq import send_pn

app = Flask(__name__)

@app.route('/')
@crossdomain(origin='*')
def index():
    '''
    Endpoint for triggering push notification
    '''
    return make_response(jsonify({ 'success': True }), 200)

if __name__ == '__main__':
    app.run(debug=True)
