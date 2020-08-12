# This is an example to run the graph in python.
import cv2

import graph_runner

cap = cv2.VideoCapture(4)

# runner = graph_runner.GraphRunner(
#         "mediapipe/graphs/hand_tracking/multi_hand_tracking_mobile.pbtxt",
#         ["channel2", "channel3"]
#         )

runner = graph_runner.GraphRunner(
        "graphs/hand_face_detection_no_gating.pbtxt", ["multi_hand_landmarks"])

frames = []

while(True):
    ret, frame = cap.read()
    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed_frame = runner.process_frame(gray)
    processed_frame = processed_frame.reshape((480, 640, 4))
    processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Frame", processed_frame)

    print(runner.get_normalized_landmark_lists("multi_hand_landmarks"))

    if cv2.waitKey(10) > 0:
        break