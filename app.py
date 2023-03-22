from flask import Flask, render_template, request

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        name = request.form['name']
        messages.append((name, message))
    return render_template('index.html.jinja2', messages=messages)

if __name__ == '__main__':
 app.run(debug=True)