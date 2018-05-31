from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)

app.secret_key = "unicorns"

@app.route('/')
def survey():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comments = request.form['description']
	if len(name) < 1:
		flash("Name cannot be blank!")
		return redirect('/')
	elif len(comments) < 1:
		flash("Comments cannot be blank!")
		return redirect('/')
	elif len(comments) > 120:
		flash("Comments has too many characters. (120 max)")
		return redirect('/')
	else:
		flash("Success! Your name is {}. Comment: {}.".format(name, comments))
	print len(request.form['name'])
	return render_template('result.html', result_name = name, result_language = language, result_location = location, result_comments = comments)

@app.route('/go_back', methods=['POST'])
def go_back():
	return render_template('index.html')

app.run(debug=True) 