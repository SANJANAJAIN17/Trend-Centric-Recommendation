

# import os
# import cvzone
# import cv2
# from cvzone.PoseModule import PoseDetector
#
# # Initialize video capture for the laptop camera
# cap = cv2.VideoCapture(0)
#
# # Initialize pose detector
# detector = PoseDetector(staticMode=False,
#                         modelComplexity=1,
#                         smoothLandmarks=True,
#                         enableSegmentation=False,
#                         smoothSegmentation=True,
#                         detectionCon=0.5,
#                         trackCon=0.5)
#
# # Load shirt images
# shirtFolderPath = "Resources/Shirts"
# listShirts = os.listdir(shirtFolderPath)
#
# fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
# shirtRatioHeightWidth = 581 / 440
# imageNumber = 0
#
# # Button properties
# buttonSize = (150, 50)
# exitButtonPosition = (50, 50)
# nextButtonPosition = (220, 50)
# prevButtonPosition = (390, 50)
#
# def is_button_clicked(event, x, y, flags, param):
#     global exit_clicked, next_clicked, prev_clicked
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if exitButtonPosition[0] <= x <= exitButtonPosition[0] + buttonSize[0] and \
#            exitButtonPosition[1] <= y <= exitButtonPosition[1] + buttonSize[1]:
#             exit_clicked = True
#         if nextButtonPosition[0] <= x <= nextButtonPosition[0] + buttonSize[0] and \
#            nextButtonPosition[1] <= y <= nextButtonPosition[1] + buttonSize[1]:
#             next_clicked = True
#         if prevButtonPosition[0] <= x <= prevButtonPosition[0] + buttonSize[0] and \
#            prevButtonPosition[1] <= y <= prevButtonPosition[1] + buttonSize[1]:
#             prev_clicked = True
#
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", is_button_clicked)
#
# exit_clicked = False
# next_clicked = False
# prev_clicked = False
#
# while True:
#     success, img = cap.read()
#     if not success:
#         print("Failed to read frame or end of video.")
#         break
#
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
#
#     if lmList:
#         lm11 = lmList[11][0:2]
#         lm12 = lmList[12][0:2]
#
#         if len(lm11) > 1 and len(lm12) > 1:
#             imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
#             if imgShirt is not None and imgShirt.shape[2] == 4:
#                 widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#
#                 # Debug prints to check values
#                 print(f"lm11: {lm11}")
#                 print(f"lm12: {lm12}")
#                 print(f"fixedRatio: {fixedRatio}")
#                 print(f"shirtRatioHeightWidth: {shirtRatioHeightWidth}")
#                 print(f"Calculated widthOfShirt: {widthOfShirt}")
#
#                 newHeight = int(widthOfShirt * shirtRatioHeightWidth)
#
#                 # Debug print to check newHeight
#                 print(f"Calculated newHeight: {newHeight}")
#
#                 if widthOfShirt > 0 and newHeight > 0:
#                     try:
#                         imgShirt = cv2.resize(imgShirt, (widthOfShirt, newHeight))
#                         currentScale = (lm11[0] - lm12[0]) / 190
#                         offset = int(44 * currentScale), int(48 * currentScale)
#
#                         img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#                     except cv2.error as e:
#                         print(f"Error resizing or overlaying image: {e}")
#                 else:
#                     print("Error: Calculated dimensions are not positive.")
#             else:
#                 print("Error: imgShirt is not valid or does not have 4 channels.")
#
#     # Draw buttons
#     cv2.rectangle(img, exitButtonPosition, (exitButtonPosition[0] + buttonSize[0], exitButtonPosition[1] + buttonSize[1]), (0, 0, 255), -1)
#     cv2.putText(img, "Exit", (exitButtonPosition[0] + 40, exitButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
#     cv2.rectangle(img, nextButtonPosition, (nextButtonPosition[0] + buttonSize[0], nextButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
#     cv2.putText(img, "Next", (nextButtonPosition[0] + 40, nextButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
#     cv2.rectangle(img, prevButtonPosition, (prevButtonPosition[0] + buttonSize[0], prevButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
#     cv2.putText(img, "Prev", (prevButtonPosition[0] + 40, prevButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#
#     # Update shirt image number
#     if next_clicked:
#         imageNumber = (imageNumber + 1) % len(listShirts)
#         next_clicked = False
#
#     if prev_clicked:
#         imageNumber = (imageNumber - 1) % len(listShirts)
#         prev_clicked = False
#
#     # Display the result
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q') or exit_clicked:
#         break
#
# # Release resources
# cap.release()
# cv2.destroyAllWindows()

# import os
# import cvzone
# import cv2
# from cvzone.PoseModule import PoseDetector
#
# # Initialize video capture for the laptop camera
# cap = cv2.VideoCapture(0)
#
# # Initialize pose detector
# detector = PoseDetector(staticMode=False,
#                         modelComplexity=1,
#                         smoothLandmarks=True,
#                         enableSegmentation=False,
#                         smoothSegmentation=True,
#                         detectionCon=0.5,
#                         trackCon=0.5)
#
# # Load shirt images
# shirtFolderPath = "Resources/Shirts"
# listShirts = os.listdir(shirtFolderPath)
#
# fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
# shirtRatioHeightWidth = 581 / 440
# imageNumber = 0
#
# # Button properties
# buttonSize = (100, 40)
# frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# exitButtonPosition = (50, frameHeight - 100)
# nextButtonPosition = (200, frameHeight - 100)
# prevButtonPosition = (350, frameHeight - 100)
#
# def is_button_clicked(event, x, y, flags, param):
#     global exit_clicked, next_clicked, prev_clicked
#     if event == cv2.EVENT_LBUTTONDOWN:
#         if exitButtonPosition[0] <= x <= exitButtonPosition[0] + buttonSize[0] and \
#            exitButtonPosition[1] <= y <= exitButtonPosition[1] + buttonSize[1]:
#             exit_clicked = True
#         if nextButtonPosition[0] <= x <= nextButtonPosition[0] + buttonSize[0] and \
#            nextButtonPosition[1] <= y <= nextButtonPosition[1] + buttonSize[1]:
#             next_clicked = True
#         if prevButtonPosition[0] <= x <= prevButtonPosition[0] + buttonSize[0] and \
#            prevButtonPosition[1] <= y <= prevButtonPosition[1] + buttonSize[1]:
#             prev_clicked = True
#
# cv2.namedWindow("Image")
# cv2.setMouseCallback("Image", is_button_clicked)
#
# exit_clicked = False
# next_clicked = False
# prev_clicked = False
#
# while True:
#     success, img = cap.read()
#     if not success:
#         print("Failed to read frame or end of video.")
#         break
#
#     img = detector.findPose(img, draw=False)  # Disable drawing of landmarks here
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)  # Disable drawing of landmarks here
#
#     if lmList:
#         lm11 = lmList[11][0:2]
#         lm12 = lmList[12][0:2]
#
#         if len(lm11) > 1 and len(lm12) > 1:
#             imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
#             if imgShirt is not None and imgShirt.shape[2] == 4:
#                 widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#
#                 # Debug prints to check values
#                 print(f"lm11: {lm11}")
#                 print(f"lm12: {lm12}")
#                 print(f"fixedRatio: {fixedRatio}")
#                 print(f"shirtRatioHeightWidth: {shirtRatioHeightWidth}")
#                 print(f"Calculated widthOfShirt: {widthOfShirt}")
#
#                 newHeight = int(widthOfShirt * shirtRatioHeightWidth)
#
#                 # Debug print to check newHeight
#                 print(f"Calculated newHeight: {newHeight}")
#
#                 if widthOfShirt > 0 and newHeight > 0:
#                     try:
#                         imgShirt = cv2.resize(imgShirt, (widthOfShirt, newHeight))
#                         currentScale = (lm11[0] - lm12[0]) / 190
#                         offset = int(44 * currentScale), int(48 * currentScale)
#
#                         img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#                     except cv2.error as e:
#                         print(f"Error resizing or overlaying image: {e}")
#                 else:
#                     print("Error: Calculated dimensions are not positive.")
#             else:
#                 print("Error: imgShirt is not valid or does not have 4 channels.")
#
#     # Draw buttons
#     cv2.rectangle(img, exitButtonPosition, (exitButtonPosition[0] + buttonSize[0], exitButtonPosition[1] + buttonSize[1]), (0, 0, 255), -1)
#     cv2.putText(img, "Exit", (exitButtonPosition[0] + 20, exitButtonPosition[1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     cv2.rectangle(img, nextButtonPosition, (nextButtonPosition[0] + buttonSize[0], nextButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
#     cv2.putText(img, "Next", (nextButtonPosition[0] + 20, nextButtonPosition[1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     cv2.rectangle(img, prevButtonPosition, (prevButtonPosition[0] + buttonSize[0], prevButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
#     cv2.putText(img, "Prev", (prevButtonPosition[0] + 20, prevButtonPosition[1] + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#
#     # Update shirt image number
#     if next_clicked:
#         imageNumber = (imageNumber + 1) % len(listShirts)
#         next_clicked = False
#
#     if prev_clicked:
#         imageNumber = (imageNumber - 1) % len(listShirts)
#         prev_clicked = False
#
#     # Display the result
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q') or exit_clicked:
#         break
#
# # Release resources
# cap.release()
# cv2.destroyAllWindows()
import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# Initialize video capture for the laptop camera
cap = cv2.VideoCapture(0)

# Increase window size
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Initialize pose detector
detector = PoseDetector(staticMode=False,
                        modelComplexity=1,
                        smoothLandmarks=True,
                        enableSegmentation=False,
                        smoothSegmentation=True,
                        detectionCon=0.5,
                        trackCon=0.5)

# Load shirt images
shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)

fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0

# Button properties
buttonSize = (150, 50)
frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
exitButtonPosition = (50, frameHeight - 100)
nextButtonPosition = (220, frameHeight - 100)
prevButtonPosition = (390, frameHeight - 100)

def is_button_clicked(event, x, y, flags, param):
    global exit_clicked, next_clicked, prev_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        if exitButtonPosition[0] <= x <= exitButtonPosition[0] + buttonSize[0] and \
           exitButtonPosition[1] <= y <= exitButtonPosition[1] + buttonSize[1]:
            exit_clicked = True
        if nextButtonPosition[0] <= x <= nextButtonPosition[0] + buttonSize[0] and \
           nextButtonPosition[1] <= y <= nextButtonPosition[1] + buttonSize[1]:
            next_clicked = True
        if prevButtonPosition[0] <= x <= prevButtonPosition[0] + buttonSize[0] and \
           prevButtonPosition[1] <= y <= prevButtonPosition[1] + buttonSize[1]:
            prev_clicked = True

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Image", is_button_clicked)

exit_clicked = False
next_clicked = False
prev_clicked = False

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame or end of video.")
        break

    img = detector.findPose(img, draw=False)  # Disable drawing of landmarks here
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)  # Disable drawing of landmarks here

    if lmList:
        lm11 = lmList[11][0:2]
        lm12 = lmList[12][0:2]

        if len(lm11) > 1 and len(lm12) > 1:
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
            if imgShirt is not None and imgShirt.shape[2] == 4:
                widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)

                # Debug prints to check values
                print(f"lm11: {lm11}")
                print(f"lm12: {lm12}")
                print(f"fixedRatio: {fixedRatio}")
                print(f"shirtRatioHeightWidth: {shirtRatioHeightWidth}")
                print(f"Calculated widthOfShirt: {widthOfShirt}")

                newHeight = int(widthOfShirt * shirtRatioHeightWidth)

                # Debug print to check newHeight
                print(f"Calculated newHeight: {newHeight}")

                if widthOfShirt > 0 and newHeight > 0:
                    try:
                        imgShirt = cv2.resize(imgShirt, (widthOfShirt, newHeight))
                        currentScale = (lm11[0] - lm12[0]) / 190
                        offset = int(44 * currentScale), int(48 * currentScale)

                        img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
                    except cv2.error as e:
                        print(f"Error resizing or overlaying image: {e}")
                else:
                    print("Error: Calculated dimensions are not positive.")
            else:
                print("Error: imgShirt is not valid or does not have 4 channels.")

    # Draw buttons
    cv2.rectangle(img, exitButtonPosition, (exitButtonPosition[0] + buttonSize[0], exitButtonPosition[1] + buttonSize[1]), (0, 0, 255), -1)
    cv2.putText(img, "Exit", (exitButtonPosition[0] + 40, exitButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.rectangle(img, nextButtonPosition, (nextButtonPosition[0] + buttonSize[0], nextButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
    cv2.putText(img, "Next", (nextButtonPosition[0] + 40, nextButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.rectangle(img, prevButtonPosition, (prevButtonPosition[0] + buttonSize[0], prevButtonPosition[1] + buttonSize[1]), (0, 255, 0), -1)
    cv2.putText(img, "Prev", (prevButtonPosition[0] + 40, prevButtonPosition[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Update shirt image number
    if next_clicked:
        imageNumber = (imageNumber + 1) % len(listShirts)
        next_clicked = False

    if prev_clicked:
        imageNumber = (imageNumber - 1) % len(listShirts)
        prev_clicked = False

    # Display the result
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q') or exit_clicked:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
