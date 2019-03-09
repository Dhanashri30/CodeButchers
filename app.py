from flask import Flask, render_template, request
import os
import sample
app = Flask(__name__)



@app.route('/')
def contact():
    return render_template("codie.html");


@app.route('/', methods=['GET', 'POST'])
def contact_post():
    global primarySkill
    global secondarySkill
    primarySkill = request.form['PrimarySkill']
    secondarySkill = request.form['SecondarySkill']
    sample.main()


if __name__ == '__main__':
    app.run()

