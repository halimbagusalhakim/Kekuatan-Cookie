from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)
FLAG = "TI404{K3ren_m4nt4ap_lee_k4ku4t4n_c00kie}"

@app.route('/')
def index():
    return '''
        <h2>Welcome to kekuatan Cookie</h2>
        <form action="/start" method="post">
            <button type="submit">Continue as Guest</button>
        </form>
    '''

@app.route('/start', methods=['POST'])
def start():
    resp = make_response(redirect(url_for('panel')))
    # Set cookie biasa, tanpa enkripsi
    resp.set_cookie('isAdmin', '0')  # 0 berarti bukan admin
    return resp

@app.route('/panel')
def panel():
    is_admin = request.cookies.get('isAdmin')
    if is_admin == '1':
        return f"<h2>Welcome Admin! Here's your flag: {FLAG}</h2>"
    else:
        return "<h2>disini gada apa apa brok.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
