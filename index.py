from flask import Flask, render_template, redirect, url_for, request
#from recorder import Recorder

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/ExactInput/', methods=['POST'])
def exact_input_post():
    message = ""
    message += "date=" + request.form['date'] + "\n"
    message += "hours_on_sleep=" + request.form['hours_on_sleep'] + "\n"
    message += "minutes_on_sleep=" + request.form['minutes_on_sleep'] + "\n"
    message += "hours_on_wake=" + request.form['hours_on_wake'] + "\n"
    message += "minutes_on_wake=" + request.form['minutes_on_wake'] + "\n"
    return message


@app.route('/ExactInput/', methods=['GET'])
def exact_input_get():
    return render_template('ExactInput.html')


@app.route('/GeneralInput/', methods=['POST'])
def general_input_post():
    message = ""
    message += "date=" + request.form['date'] + "\n"
    message += "start_sleeping=" + request.form['start_sleeping'] + "\n"
    message += "hours_on_sleep=" + request.form['hours_on_sleep'] + "\n"
    message += "minutes_on_sleep=" + request.form['minutes_on_sleep'] + "\n"
    message += "adjust_minute=" + request.form['adjust_minute'] + "\n"
    return message


@app.route('/GeneralInput/', methods=['GET'])
def general_input_get():
    return render_template('GeneralInput.html')


if __name__ == "__main__":
    #recorder = Recorder()
    app.run(host="0.0.0.0", port=5000)

