import requests

def parser(url):
    r = requests.get(url)

    txt = r.text.split("\n")
    txt = [i for i in txt if "Cube currency" in i]

    curses = {}
    for i in txt:
        s1 = i.find("Cube currency=") + 14
        s2 = i.find("rate='") + 6
        curses[i[s1 + 1:s1+4]] = float(i[s2:len(i) - 3])

    return curses


# print(parser("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"))