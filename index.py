from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
app.debug = True

@app.route('/')
def default():
    return redirect(url_for('index'))

@app.route('/index')
def index():
	return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
'''
return "<hi>Hellow you!!! <a href='#'  onClick='history.back()'>Ni bou hou</a>"
'''
