from fastapi import FastAPI
from currency_parser import parser

def take_db(url):
    return parser(url)

class Converter:
    def __init__(self, db):
        self.inp = ""
        self.out = ""
        self.db = db
        self.val = 0

    def convert_inp(self, currency):
        self.inp = currency
        return "input currency set to {}".format(self.inp)

    def convert_out(self, currency):
        self.out = currency
        return "output currency set to {}".format(self.out)

    def value(self, value):
        self.val = int(value)
        return "converting value set to {}".format(self.val)

    def convert(self):
        if self.inp != "" and self.out != "" and self.val > 0:
            return str(self.val / self.db[self.inp] * self.db[self.out])
        else:
            return "err"

with open("settings.txt", "r") as f:
    sett = f.read().split("\n")

URL = sett[0]
db = take_db(URL)
app = FastAPI()
conv = Converter(db)

@app.get("/")
def info():
    return "документация"

@app.post("/api/input_currency")
def input_currency(currency):
    return conv.convert_inp(currency)

@app.post("/api/output_currency")
def output_currency(currency):
    return conv.convert_out(currency)

@app.post("/api/value")
def input_value(value):
    return conv.value(value)

@app.get("/api/convert")
def converting():
    return conv.convert
