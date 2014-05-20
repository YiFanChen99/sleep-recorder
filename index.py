from flask import Flask, render_template, redirect, url_for, request
from recorder import Recorder

app = Flask(__name__)
app.debug = True


@app.route('/')
def default():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/GeneralInput/', methods=['POST'])
def general_input_post():
    if request.method == 'POST':
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
    recorder = Recorder()
    app.run(host="0.0.0.0", port=5000)

'''
return "<hi>Hellow you!!! <a href='#'  onClick='history.back()'>Ni bou hou</a>"
'''
