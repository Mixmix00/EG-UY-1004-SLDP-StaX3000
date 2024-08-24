import apriltag
import argparse
import cv2

camera = ""
options = ""
detector = ""


camera = cv2.VideoCapture(0)
print("Configuring AprilTag Detector")
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)

def readAndDetectFrame():
    ret, image = camera.read()

    if not ret:
        raise Exception("Error reading camera frame")
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    results = detector.detect(gray)
    if len(results) > 0:
        #print("Size: " + str(image.shape))
        #print(str(results))
        print("")
    return ((image, results))

#This function will tell you where the tag is relative to the center of the camera.
#For example if it says the tag is to the right of the camera then to get to the center of the tag you would hav to move the robot left.
def findRelative2DPositionOfTagFromCenterOfCamera(image, results, tagId):
    for tag in results:
        if tag.tag_id != tagId:
            continue

        imageShape = image.shape

        midX = int(imageShape[1] / 2)
        midY = int(imageShape[0] / 2)

        centerOfTag = tag.center

        tagMidX = int(centerOfTag[0])
        tagMidY = int(centerOfTag[1])
        toTheRight = False
        toTheBottom = False
        if midX < tagMidX:
            toTheRight = True
        if midY < tagMidY:
            toTheBottom = True
        
        return (toTheRight, toTheBottom)
#Checks whether the tag is in the center of the camera
#Returns if its in the center of the X axis and the center of the Y axis as a tuple

def isTagInCenterOfCamera2D(image, results, tagId, tolerencePercentage):
    for tag in results:
        if tag.tag_id != tagId:
            continue

        imageShape = image.shape

        midX = int(imageShape[1] / 2)
        midY = int(imageShape[0] / 2)

        centerOfTag = tag.center

        tagMidX = int(centerOfTag[0])
        tagMidY = int(centerOfTag[1])

        ratioX = midX/tagMidX
        ratioY = midY/tagMidY

        if ratioX > 1:
            change = 2 * (ratioX - 1)
            ratioX -= change
        
        if ratioY > 1:
            change = 2 * (ratioY - 1)
            ratioY -= change

        isCenteredX = (ratioX >= tolerencePercentage)
        isCenteredY = (ratioY >= tolerencePercentage)

        return (isCenteredX, isCenteredY)


def makeResultsViewable(image, results):
    for tag in results:
        #Get the corners of the tag in the image as pixel locations
        (x, y, w, h) = tag.corners
        
        #Convert the pixel location data to integer values in the image
        x = (int(x[0]), int(x[1]))
        y = (int(y[0]), int(y[1]))
        w = (int(w[0]), int(w[1]))
        h = (int(h[0]), int(h[1]))
        
        #Draw a box around the apriltag using lines connecting each of the corners
        cv2.line(image, x, y, (0,255,0), 2)
        cv2.line(image, y, w, (0,255,0), 2)
        cv2.line(image, w, h, (0,255,0), 2)
        cv2.line(image, h, x, (0,255,0), 2)
        
        #Get the tagID from the detection
        tagId = tag.tag_id
        
        #Put the tagID of the tag on the image
        cv2.putText(image, str(tagId), x, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

        cv2.imshow("AprilTag Video Detection", image)
        cv2.waitKey(0)

while True:
    result = readAndDetectFrame()
    makeResultsViewable(result[0], result[1])
    print(str(findRelative2DPositionOfTagFromCenterOfCamera(result[0], result[1], 3)))