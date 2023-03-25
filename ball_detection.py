"""
ENPM673: PERCEPTION FOR AUTONOMOUS ROBOTS
SUBMITTED BY: AKASHKUMAR PARMAR
"""

# Importing required libraries
import numpy as np
import cv2 as cv

def ball_detection():
        
    video = cv.VideoCapture('ball.mov') # Reading video file

    while(video.isOpened()): # Iterating through the video

        is_it, frame = video.read()
        if not is_it: break


        blurred_frame = cv.medianBlur(frame,5) # Median blur
        gray_frame = cv.cvtColor(blurred_frame, cv.COLOR_BGR2GRAY) # Gray scale
        contoured_frame = cv.HoughCircles(gray_frame, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=25, minRadius=9, maxRadius=13) # Detecting circles

        # Drawing the detected contoured_frame on the original image
        if contoured_frame is not None: 
            contoured_frame = np.round(contoured_frame[0, :]).astype("int")
            for (x, y, r) in contoured_frame:
                cv.circle(frame, (x, y), r, (0, 255, 0), 2)

        cv.imshow("Question2", frame)

        key = cv.waitKey(1)
        if key == ord("q"):
            break

    cv.destroyAllWindows()

def main():
    ball_detection()


if __name__=="__main__":
    main()