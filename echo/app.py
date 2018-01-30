"""Flask APP."""

from flask import Flask
from flask import request
from flask import jsonify
from anagram import are_anagrams

app = Flask(__name__)


@app.route("/")
def index():
    """Handle HTTP GET Request for the default (home/index) route."""
    return "Check if two words are anagrams"


@app.route('/api/v1.0/anagrams', methods=['GET'])
@app.route('/api/v1.0/anagrams/<msg>', methods=['GET'])
def anagrams(msg=None):
	first = request.args.get('first')
	second = request.args.get('second')
	if first and second:
		result = are_anagrams(first,second)
		return jsonify({"This is anagram" : result})
	elif msg:
		first,second = msg.split('&')
		result = are_anagrams(first,second)
		return jsonify({"This is anagram" : result})
	else:
		return "Nothing to compare..."

@app.after_request
def after_request(response):
    """Tweak response."""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
