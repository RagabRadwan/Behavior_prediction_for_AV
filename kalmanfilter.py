#https://pysource.com/2021/10/29/kalman-filter-predict-the-trajectory-of-an-object/
import cv2
import numpy as np


class KalmanFilter:
    kf = cv2.KalmanFilter(4, 2) #position x,y and velocity x,y
    kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)
    kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kf.processNoiseCov =1*np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
    kf.measurementNoiseCov = 1*np.array([[1, 0], [0, 1]], np.float32)


    def predict(self, coordX, coordY):
        ''' This function estimates the position of the object''' 
        predicted = self.kf.predict()
        measured = np.array([[np.float32(coordX)], [np.float32(coordY)]])
        estimate=self.kf.correct(measured)
        predicted = self.kf.predict()
        x, y = int(predicted[0]), int(predicted[1])
        return x, y


