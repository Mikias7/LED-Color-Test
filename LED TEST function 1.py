# LED TEST function

import cv2 as cv
import numpy as np

#HSV value for blue, green, and red
blue_lower_limit =  np.array([110, 100, 100])
blue_upper_limit =  np.array([130, 255, 255])

green_lower_limit =  np.array([ 50, 100, 100])
green_upper_limit =  np.array([ 70, 255, 255])

red_lower_limit =  np.array([0, 200, 200])
red_upper_limit = np.array([4, 255, 255])

#camera
camera = cv.VideoCapture(0)

#call function to check_color. parameter(color)
def check_color(color):
    while True:
        ret, frame = camera.read()

        #convert the frame from rgb to the HSV color space
        into_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        #mask target color
        blue_mask = cv.inRange(into_hsv, blue_lower_limit, blue_upper_limit)
        green_mask = cv.inRange(into_hsv, green_lower_limit, green_upper_limit)
        red_mask = cv.inRange(into_hsv, red_lower_limit, red_upper_limit)

        #count the number of pixels from each color
        red_count = cv.countNonZero(red_mask)
        green_count = cv.countNonZero(green_mask)
        blue_count = cv.countNonZero(blue_mask)

        #detect color
        match color:
            case "blue":
                if blue_count > 30: return "blue detected"
            case "green":
                if green_count > 30: return "green detected"
            case "red":
                if red_count > 30: return "red detected"
            case "ir": # ir led is red, so the function uses the red count for the ir led.
                if red_count > 30: return "red detected"

        if cv.waitKey(1) == ord('q'):
            break

check_color("red")

camera.release()
cv.destroyAllWindows()