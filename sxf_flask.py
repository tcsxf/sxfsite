from flask import Flask, session, render_template, request, abort


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jm'

@app.route('/')
def index():
    return render_template('sxf.html')


@app.route('/head/')
def head():
    session['sxf'] = 'ggsmd'
    s = '<html><body>'
    for k, v in request.headers.items():
        s += '<div>' + k + '----' + v + '</div>'
    s += '</body></html>'
    return s


@app.route('/game')
def game():
    gameid = request.args.get('id', '0')
    if gameid == '1':
        return render_template('2048.html')
    else:
        return abort(404)
