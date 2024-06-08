from API_converter import Converter, take_db
import flask

with open("settings.txt", "r") as f:
    sett = f.read().split("\n")

URL = sett[0]
db = take_db(URL)

app = flask.Flask(__name__)
conv = Converter(db)

@app.route('/')
def main_str():
    return flask.render_template('converter.html')

@app.route('/api/convert', methods=['POST'])
def submit():
    from_currency = flask.request.form['from']
    to_currency = flask.request.form['to']
    value = flask.request.form['amount']

    if from_currency in db.keys() and to_currency in db.keys() and value.isdigit():
        conv.convert_inp(from_currency)
        conv.convert_out(to_currency)
        conv.value(int(value))
        return result()
    else:
        return main_str()

@app.route('/result')
def result():
    res = conv.convert()
    return flask.render_template('result.html', fr=conv.inp, to=conv.out, result=res[:res.find(".") + 3])


if __name__ == '__main__':
    app.run(debug=True)