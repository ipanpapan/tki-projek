from flask import Flask, render_template, request, session, redirect, url_for
from sum import summari
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", title="Automatic Text Summarization")

@app.route("/ringkas", methods=['GET', 'POST'])
def ringkas():
	url = request.form['url']
	try:
		count_sentence = request.form['count_sentence']
		hasilAsli = summari(url, count_sentence)
		return render_template("index.html", hasil=hasilAsli, title="Result of Summarization")
	except:
		session['alert'] = True
		return render_template("index.html", title="The Result is Wrong")
	# if request.method == 'POST':
	# 	url = request.form['url']
	# 	return render_template('index.html', hasil='kasjdas')
	# else:
	# 	return 'haha'

if __name__ == "__main__":
	app.secret_key = os.urandom(24)
	app.run(debug=True)
	app.run()