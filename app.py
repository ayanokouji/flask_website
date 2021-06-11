from flask import Flask

app = Flask(__name__)

@app.route('/')
def flask():
	return 'Welcome to flask'

if __name__ == "__main__":
	app.run(host='0.0.0.0')