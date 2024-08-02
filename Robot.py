#import subsystems.Drive as Drive
import subsystems.AprilTagWebcam as AprilTagWebcam


while True:
    AprilTagWebcam.readAndDetectFrame()