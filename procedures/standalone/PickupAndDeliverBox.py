import subsystems.Drive as Drive
import subsystems.AprilTagWebcam as AprilTagWebcam
import constants.TagID as constants
import math
import time
def run():
    initialFrame = AprilTagWebcam.readAndDetectFrame()
    res = initialFrame[1]

    for tag in res:
        if tag.tag_id == constants.deliveryZoneTop:
            center = AprilTagWebcam.isTagInCenterOfCamera2D(initialFrame[0], res, constants.deliveryZoneTop, 0.05)

            while not center[0]:
                processed = AprilTagWebcam.findRelative2DPositionOfTagFromCenterOfCamera(frame[0], res, constants.deliveryZoneTop)

                if processed[0]:
                    Drive.CONCURRENT_setDriveMotors(0)
                else:
                    Drive.CONCURRENT_setDriveMotors(math.pi)
                
                time.sleep(0.1)

                frame = AprilTagWebcam.readAndDetectFrame()
                res = frame[1]
                center = AprilTagWebcam.isTagInCenterOfCamera2D(frame[0], res, constants.deliveryZoneTop, 0.05)

            
    return
