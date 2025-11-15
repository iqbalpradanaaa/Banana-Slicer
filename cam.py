import cv2 as cv
import run
import numpy as np
import pygame
from collections import deque
import mediapipe as mp

mpHands = mp.solutions.hands
tangan = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles

pts = deque(maxlen=10)

def get_frame(cap):
    success, frame = cap.read()
    # h, w, c = cap.shape
    frame = cv.resize(frame, (run.width, run.height))
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    hasil = tangan.process(frame)
    x1, y1 = 0, 0
    x2, y2 = 0, 0 
    if hasil.multi_hand_landmarks:
        hand_landmarks = hasil.multi_hand_landmarks[0].landmark
        telunjuk = hand_landmarks[8]
        for hand_landmarks in hasil.multi_hand_landmarks:
            x1, y1 = int(telunjuk.x * run.width), int(telunjuk.y * run.height)
            x2, y2 = run.width - int(telunjuk.x * run.width), int(telunjuk.y * run.height)
            center = x1, y1
            cv.circle(frame, (x1, y1), 15, (255, 0, 0), cv.FILLED)
            pts.appendleft(center)
            # mpDraw.draw_landmarks(
            #     frame,
            #     hand_landmarks,
            #     mpHands.HAND_CONNECTIONS,
            #     mp_draw_styles.get_default_hand_landmarks_style(),
            #     mp_draw_styles.get_default_hand_connections_style()
            # )
        for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore them
            if pts[i - 1] is None or pts[i] is None:
                continue
        # otherwise, compute the thickness of the line and
        # draw the connecting lines
            thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
            cv.line(frame, pts[i - 1], pts[i], (255, 0, 0), thickness)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    return frame, (x2, y2)