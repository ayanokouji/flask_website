from flask import Flask

app = Flask(__name__)

@app.route('/')
def flask():
	return 'Welcome to flask Build 13'

if __name__ == "__main__":
	app.run(host='0.0.0.0')