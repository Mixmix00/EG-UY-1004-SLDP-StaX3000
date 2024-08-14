
import procedures.standalone.DriveTriangle as DriveTriangle
import procedures.standalone.DriveSquare as DriveSquare
import procedures.standalone.PickupAndDeliverBox as PickupAndDeliverBox
import procedures.standalone.M3 as M3
import procedures.standalone.M4 as M4
import subsystems.Arrow as Arrow
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    Arrow.signalRobotStopped()
    return render_template('index.html')

@app.route('/pinInput', methods=["GET", "POST"])
def pinInput():
    pin = request.form['pin']
    
    if pin == '84327639890':
        Arrow.signalRobotLoggedIn()
        return render_template('interface.html', logged_in=True)
    
    Arrow.PROC_signalRobotFailedAttempt()
    return render_template('index.html', error='Invalid PIN')

@app.route('/driveTriangle', methods=["GET"])
def driveTriangle():
    Arrow.signalRobotEnabled()
    DriveTriangle.run()
    Arrow.signalRobotStopped()
    return render_template('interface.html', logged_in=True)

@app.route('/driveSquare', methods=["GET"])
def driveSquare():
    Arrow.signalRobotEnabled()
    DriveSquare.run()
    Arrow.signalRobotStopped()
    return render_template('interface.html', logged_in=True)

@app.route('/pickupAndDeliverBox', methods=["GET"])
def pickupAndDeliverBox():
    Arrow.signalRobotEnabled()
    PickupAndDeliverBox.run()
    Arrow.signalRobotStopped()
    return render_template('interface.html', logged_in=True)

@app.route('/turnM3On', methods=["GET"])
def turnM3On():
    Arrow.signalRobotEnabled()
    M3.run()
    Arrow.signalRobotStopped()
    return render_template('interface.html', logged_in=True)

@app.route('/turnM4On', methods=["GET"])
def turnM4On():
    Arrow.signalRobotEnabled()
    M4.run()
    Arrow.signalRobotStopped()
    return render_template('interface.html', logged_in=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
