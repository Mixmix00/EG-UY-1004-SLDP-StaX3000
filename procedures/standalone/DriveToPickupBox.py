import subsystems.AprilTagWebcam as AprilTagWebcam
import subsystems.Drive as Drive
import subsystems.Led as Led
import time
import math

def run(boxId):
    Led.signalDrivingToBox()
    
    result = AprilTagWebcam.readAndDetectFrame()

    center = AprilTagWebcam.isTagInCenterOfCamera2D(result[0], result[1], boxId, 0.05)
    while not center[0]:

        location = AprilTagWebcam.findRelative2DPositionOfTagFromCenterOfCamera(result[0], result[1], boxId)

        if location[0]:
            Drive.CONCURRENT_setDriveMotors(0)
        else:
            Drive.CONCURRENT_setDriveMotors(math.pi / 2)
        
        time.sleep(0.05)
        
        center = AprilTagWebcam.isTagInCenterOfCamera2D(result[0], result[1], boxId, 0.05)

    Drive.CONCURRENT_driveStraight()

