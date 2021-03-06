import cv2
import numpy as np

class VideoCaptureYUV:
    def __init__(self, filename, size):
        self.height, self.width = size
        self.frame_len = int(self.width * self.height * 3/2)
        self.f = open(filename, 'rb')
        self.shape = (int(self.height*1.5), self.width)

    def read_raw(self):
        try:
            raw = self.f.read(self.frame_len)
            yuv = np.frombuffer(raw, dtype=np.uint8)
            yuv = yuv.reshape(self.shape)
        except Exception as e:
            print(str(e))
            return False, None
        return True, yuv

    def read(self):
        ret, yuv = self.read_raw()
        if not ret:
            return ret, yuv
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420, 3)
        return ret, bgr


if __name__ == "__main__":
    #filename = "tennis_qcif.yuv"
    i = 0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('sang.mp4', fourcc, 20.0, (176,144))
    filename = "foreman_qcif_15.yuv"
    size = (144,176)
    cap = VideoCaptureYUV(filename, size)

    while 1:
        i +=1
        ret, frame = cap.read()
        out.write(frame)
        if ret:
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
        else:
            break
    print(i)
    out.release()
