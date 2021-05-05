from flask import Flask, render_template
from flask_socketio import SocketIO
from wumboCoin import wumboCoin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fnf&dja^392#dv'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/give/<username>', methods=['GET', 'POST'])
def sessions():
    
    return render_template('base.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)