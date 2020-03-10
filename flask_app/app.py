from flask import Flask, render_template
from model import get_tels

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def list_tel():
    return render_template('list_tel.html', tels=get_tels())


if __name__ == '__main__':
    app.run()
