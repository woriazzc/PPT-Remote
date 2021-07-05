from PPTControler import PPTControler
import json
from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/play', methods=['GET', 'POST'])
def play():
    e = request.args.get('mov')
    id = PPTControler().getActivePresentationSlideIndex()
    id2 = PPTControler().fullScreen()
    if e == '1':
        PPTControler().gotoSlide(id)
    else:
        id = id2
    d = {
        'id': id,
        'tot': PPTControler().getActivePresentationSlideCount()
    }
    return Response(json.dumps(d), mimetype='application/json')

@app.route('/end', methods=['GET', 'POST'])
def end():
    d = {
        'id': PPTControler().endPlay(),
        'tot': PPTControler().getActivePresentationSlideCount()
    }
    return Response(json.dumps(d), mimetype='application/json')

@app.route('/changePage', methods=['GET', 'POST'])
def changePage():
    e = request.args.get('mov')
    if e == '0':
        id = PPTControler().click()
    elif e == '1':
        id = PPTControler().prePage()
    elif e == '2':
        id = PPTControler().nextPage()
    else:
        id = -1;
    d = {
        'id': id,
        'tot': PPTControler().getActivePresentationSlideCount()
    }
    return Response(json.dumps(d), mimetype='application/json')

@app.route('/getPage', methods=['GET', 'POST'])
def getPage():
    d = {
        'id': PPTControler().getActivePresentationSlideIndex(),
        'tot': PPTControler().getActivePresentationSlideCount()
    }
    return Response(json.dumps(d), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
