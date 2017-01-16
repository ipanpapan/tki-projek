from flask import Flask, render_template, request, session, redirect, url_for
from sum import summary
import os

app = Flask(__name__)

@app.route("/")
def index():
	session['alert'] = False
	return render_template("index.html", title="Automatic Text Summarization")

@app.route("/ringkas", methods=['GET', 'POST'])
def ringkas():
	try:
		session['alert'] = False
		language = request.form['language']
		url = request.form['url']
		count_sentence = request.form['count_sentence']
		hasilAsli = summary(language, url, count_sentence)
		return render_template("index.html", hasil=hasilAsli, url=url, bahasa=language, jumlah=count_sentence, title="Result of Summarization")
	except:
		return redirect(url_for('alert'))

@app.route("/index", methods=['GET', 'POST'])
def alert():
	session['alert'] = True
	return render_template("index.html", title="This Result is Wrong")


if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True)
	app.run()