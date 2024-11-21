from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello Sample World app2!"

if __name__ == "__main__":
	app.run(debug=True)