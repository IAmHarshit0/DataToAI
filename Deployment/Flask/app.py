from flask import Flask, render_template, request, url_for, redirect, jsonify

# create a simple Flask application 
app = Flask(__name__)

# routing Links in Flask 
@app.route("/", methods=["GET"])
def welcome(): 
    return "<h1>Welcome to Flask</h1>"

@ app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to Index</h2>"

# variable rule 
@ app.route('/success/<int:score>')
def success(score): 
    return "The person has passed and the score is: " + str(score)

@ app.route('/fail/<int:score>')
def fail(score): 
    return "The person has failed and the score is: " + str(score)

@ app.route('/form', methods=["POST", "GET"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        english = float(request.form['english'])

        avg = (maths+science+english)/3

        res=''
        if avg>=50:
            res='success'
        else:
            res='fail'

        return redirect(url_for(res, score=avg))

        # return render_template('form.html', score=avg)



if __name__ == "__main__":
    app.run(debug=True)