import subsystems.AprilTagWebcam as AprilTagWebcam
import subsystems.Drive as Drive
import subsystems.Led as Led
import time

#Ensure no other code is using a subsystem here
def run(boxId):
    Led.signalStartingRobot()
    initialFrame = AprilTagWebcam.readAndDetectFrame()
    res = initialFrame[1]

    for tag in res:
        if tag.tag_id == boxId:
            return
    
    Drive.CONCURRENT_spinClockwise()
    startTime = time.time()

    while True:
        frame = AprilTagWebcam.readAndDetectFrame()
        result = frame[1]
        for tag in res:
            if tag.tag_id == boxId:
                return
        
        time.sleep(0.05)

        currentTime = time.time()

        if (currentTime - startTime) > 5:
            raise Exception("Took longer than 5 seconds to find box. Aborting.")

    

    





