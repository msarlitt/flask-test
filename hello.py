from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'I\'m an index page'

@app.route('/heyz')
def heyz():
	return 'Heyz I\'m a heyz page'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s is in da house' % username

if __name__ == '__main__':
	app.run()
