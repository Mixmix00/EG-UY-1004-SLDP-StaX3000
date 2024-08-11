
import procedures.standalone.DriveTriangle as DriveTriangle
import procedures.standalone.DriveSquare as DriveSquare
import procedures.standalone.PickupAndDeliverBox as PickupAndDeliverBox
from Flask import flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pinInput', methods=("GET", "POST"))
def pinInput():
    pin = request.form['pin']
    
    if pin == '84327639890':
        return render_template('interface.html', logged_in=True)
    
    return render_template('index.html', error='Invalid PIN')

@app.route('/driveTriangle', methods=("GET"))
def driveTriangle():
    DriveTriangle.run()
    return render_template('interface.html', logged_in=True)

@app.route('/driveSquare', methods=("GET"))
def driveSquare():
    DriveSquare.run()
    return render_template('interface.html', logged_in=True)

@app.route('/pickupAndDeliverBox', methods=("GET"))
def pickupAndDeliverBox():
    PickupAndDeliverBox.run()
    return render_template('interface.html', logged_in=True)