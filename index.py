from flask import Flask, render_template, request
from sum import summari

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", title="Automatic Text Summarization")

@app.route("/ringkas", methods=['GET', 'POST'])
def ringkas():
	url = request.form['url']
	hasilAsli = summari(url)
	return render_template("index.html", hasil=hasilAsli)
	# if request.method == 'POST':
	# 	url = request.form['url']
	# 	return render_template('index.html', hasil='kasjdas')
	# else:
	# 	return 'haha'

if __name__ == "__main__":
    app.run(debug=True)
