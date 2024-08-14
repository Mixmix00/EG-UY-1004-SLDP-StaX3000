
import procedures.standalone.DriveTriangle as DriveTriangle
import procedures.standalone.DriveSquare as DriveSquare
import procedures.standalone.PickupAndDeliverBox as PickupAndDeliverBox
import procedures.standalone.M3 as M3
import procedures.standalone.M4 as M4
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pinInput', methods=["GET", "POST"])
def pinInput():
    pin = request.form['pin']
    
    if pin == '84327639890':
        return render_template('interface.html', logged_in=True)
    
    return render_template('index.html', error='Invalid PIN')

@app.route('/driveTriangle', methods=["GET"])
def driveTriangle():
    DriveTriangle.run()
    return render_template('interface.html', logged_in=True)

@app.route('/driveSquare', methods=["GET"])
def driveSquare():
    DriveSquare.run()
    return render_template('interface.html', logged_in=True)

@app.route('/pickupAndDeliverBox', methods=["GET"])
def pickupAndDeliverBox():
    PickupAndDeliverBox.run()
    return render_template('interface.html', logged_in=True)

@app.route('/turnM3On', methods=["GET"])
def turnM3On():
    M3.run()
    return render_template('interface.html', logged_in=True)

@app.route('/turnM4On', methods=["GET"])
def turnM4On():
    M4.run()
    return render_template('interface.html', logged_in=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
