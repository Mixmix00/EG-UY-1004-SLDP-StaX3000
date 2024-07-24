import apriltag
import argparse
import cv2


ap = argparse.ArgumentParser()


ap.add_argument("-i", "--image", required=True,
	help="path to input image containing AprilTag")

args = vars(ap.parse_args())

print("[INFO] loading image...")
image = []
if(args["image"] == "camera"):
    print("Placeholder")
else: 
	image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("[INFO] detecting AprilTags...")
options = apriltag.DetectorOptions(families="tag36h11")
detector = apriltag.Detector(options)
results = detector.detect(gray)
print("[INFO] {} total AprilTags detected".format(len(results)))
print(str(results))

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

    cv2.imshow("k", image)
    cv2.waitKey(0)