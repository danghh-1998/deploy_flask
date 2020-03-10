from flask import Flask, render_template
from model import create_tel, get_tels, get_tel, delete_tel

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def hello_world():
    return render_template('list_tel.html', tels=get_tels())


if __name__ == '__main__':
    app.run()
