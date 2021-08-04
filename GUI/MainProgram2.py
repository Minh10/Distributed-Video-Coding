# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 10:52:02 2018
@author: xuanm
"""
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QGraphicsRectItem, QGraphicsScene, QMessageBox, QMainWindow
import cv2
import sys,os
import MainWindow
import VideoDialog
import time
import serial
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import cv2
import socket
import pickle
import numpy as np
import time
import tqdm

class VideoCaptureYUV:
    def __init__(self, filename, size):
        self.height, self.width = size
        self.frame_len = int(self.width * self.height)
        self.f = open(filename, 'rb')
        self.shape = (int(self.height), self.width)
        self.f_ori = open("/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/akiyo_cif.yuv", 'rb')
        self.frame_len_ori = int(self.width * self.height * 3/2)
        self.shape_ori = (int(self.height*1.5), self.width)


    def read_raw(self):
        try:
            raw = self.f.read(self.frame_len)
            buf = self.f_ori.read(self.frame_len)
            raw += self.f_ori.read(self.frame_len_ori - self.frame_len)
            #raw_ori[0:self.frame_len] = raw
            yuv = np.frombuffer(raw, dtype=np.uint8)
            yuv = yuv.reshape(self.shape_ori)
            
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
class MainProgram(QWidget):
    def __init__(self): 
        app = 0
        app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        MainProgram = QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(MainProgram)
        self.timer = QTimer()
        self.timer.timeout.connect(self.Button_camera1_clicked)

        self.camera1_flag = 0
        self.camera2_flag = 0
        self.savepath = ""
        self.filename_camera1 = ""
        self.filename_camera2 = ""
        self.timer_serial = QtCore.QTimer()
        self.action_connect()
        MainProgram.show()
        sys.exit(app.exec_())
        
    def action_connect(self):
        #self.ui.Button_camera1.clicked.connect(self.Button_camera1_clicked) 
        self.ui.Button_camera1.clicked.connect(self.controlTimer)

        self.ui.Button_camera2.clicked.connect(self.Button_camera2_clicked)
        self.ui.Button_filename.clicked.connect(self.Button_filename_clicked)
        self.ui.Button_savepath.clicked.connect(self.Button_savepath_clicked)
        self.ui.Button_recording.clicked.connect(self.Button_recording_clicked)
        self.ui.Button_endrecording.clicked.connect(self.Button_endrecording_clicked)
        self.ui.Button_trigger.clicked.connect(self.Button_trigger_clicked)
        self.ui.Button_canceltrigger.clicked.connect(self.Button_canceltrigger_clicked)
        self.timer_serial.timeout.connect(self.serial_timer_trigger)

    def Button_camera1_clicked(self):
       # receive 4096 bytes each time
      BUFFER_SIZE = 4096
      SEPARATOR = "<SEPARATOR>"
      #socket1 --------------------------------------------------------------------------------------
      client_socket_1, address_1 = self.s1.accept() 
      # receive the file infos
      # receive using client socket, not server socket
      received = client_socket_1.recv(BUFFER_SIZE).decode()
      filename, filesize = received.split(SEPARATOR)
      # remove absolute path if there is
      filename = os.path.basename(filename)
      # convert to integer
      filesize = int(filesize)
      # start receiving the file from the socket
      # and writing to the file stream
      progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
      filename = "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/" + filename
      with open(filename, "wb") as f:
         while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket_1.recv(BUFFER_SIZE)
            if not bytes_read:    
                  # nothing is received
                  # file transmitting is done
                  break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
      # close the client socket
      client_socket_1.close()
      # close the server socket
      self.s1.close()
      #socket2 --------------------------------------------------------------------------------------
      client_socket_2, address_2 = self.s2.accept() 
      # receive the file infos
      # receive using client socket, not server socket
      received = client_socket_2.recv(BUFFER_SIZE).decode()
      filename, filesize = received.split(SEPARATOR)
      # remove absolute path if there is
      filename = os.path.basename(filename)
      # convert to integer
      filesize = int(filesize)
      # start receiving the file from the socket
      # and writing to the file stream
      progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
      filename_2 = "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/" + filename
      with open(filename_2, "wb") as f:
         while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket_2.recv(BUFFER_SIZE)
            if not bytes_read:    
                  # nothing is received
                  # file transmitting is done
                  break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
      # close the client socket
      client_socket_2.close()
      # close the server socket
      self.s2.close()
      #socket3 --------------------------------------------------------------------------------------
      client_socket_3, address_3 = self.s3.accept() 
      # receive the file infos
      # receive using client socket, not server socket
      received = client_socket_3.recv(BUFFER_SIZE).decode()
      filename, filesize = received.split(SEPARATOR)
      # remove absolute path if there is
      filename = os.path.basename(filename)
      # convert to integer
      filesize = int(filesize)
      # start receiving the file from the socket
      # and writing to the file stream
      progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
      filename = "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/" + filename
      with open(filename, "wb") as f:
         while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = client_socket_3.recv(BUFFER_SIZE)
            if not bytes_read:    
                  # nothing is received
                  # file transmitting is done
                  break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
      # close the client socket
      client_socket_3.close()
      # close the server socket
      self.s3.close()
      #decode keyframe from h264
      cmd = "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/ffmpeg-h264-dec/h264dec " + filename_2 + " " + "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/akiyo_infoQ1.yuv"
      os.system(cmd)
      os.system("cd /home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder;wine ./discoverdec.exe recv_decoder.cfg")
      i = 0
      
      #fourcc = cv2.VideoWriter_fourcc(*'mp4v')
      #out = cv2.VideoWriter('receiveVideo.mp4', fourcc, 15.0, (176,144))
      filename = "/home/nanhtrang/AI/DVC/code/client2/discovercodec/decoder/receiveVideo01.yuv"
      size = (288,352)
      cap = VideoCaptureYUV(filename, size)
      while 1:
         i +=1
         ret, frame = cap.read()
         frame = cv2.flip(frame, 1)
         #out.write(frame)
         if ret:
            if frame is not None and type(frame) == np.ndarray:
               cv2.imshow("frame", frame)
               cv2.waitKey(1)
            #print(frame)
               rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
               convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888)
               convertToQtFormat = QtGui.QPixmap.fromImage(convertToQtFormat)
               pixmap = QPixmap(convertToQtFormat)
               resizeImage = pixmap.scaled(640, 480, QtCore.Qt.KeepAspectRatio)
               self.ui.video1.setPixmap(QPixmap(resizeImage))
               time.sleep(1/30)
            else:
               break
      #out.release()

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            SERVER_HOST = "127.0.0.1"
            #socket1 -------------------------------------------------------------            
            # device's IP address
            
            SERVER_PORT = 12008
            
            # create the server socket
            # TCP socket
            self.s1 = socket.socket()
            # bind the socket to our local address
            self.s1.bind((SERVER_HOST, SERVER_PORT))
            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            self.s1.listen(5)
            print(f"[*] Socket1 Listening as {SERVER_HOST}:{SERVER_PORT}")
            print("-> waiting for connection to socket1")
            #socket2 ------------------------------------------------------------------
            SERVER_PORT_2 = SERVER_PORT + 1
            
            # create the server socket
            # TCP socket
            self.s2 = socket.socket()
            # bind the socket to our local address
            self.s2.bind((SERVER_HOST, SERVER_PORT_2))
            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            self.s2.listen(5)
            print(f"[*] Socket2 Listening as {SERVER_HOST}:{SERVER_PORT_2}")
            print("-> waiting for connection to socket2")
            #Socket3 --------------------------------------------------------------------
            SERVER_PORT_3 = SERVER_PORT + 2
            
            # create the server socket
            # TCP socket
            self.s3 = socket.socket()
            # bind the socket to our local address
            self.s3.bind((SERVER_HOST, SERVER_PORT_3))
            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            self.s3.listen(5)
            print(f"[*] Socket3 Listening as {SERVER_HOST}:{SERVER_PORT_3}")
            print("-> waiting for connection to socket3")
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.Button_camera1.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            #self.cap.release()
            self.sock.close()
            # update control_bt text
            self.ui.Button_camera1.setText("Camera 1")

    def Button_camera2_clicked(self):
        if self.camera2_flag == 0:
            self.cap2 = cv2.VideoCapture(1)
            if self.cap2.isOpened() == True:
                self.sub_ui2 = VideoDialog.Ui_VideoDialog()
                self.Dialog2 = QtWidgets.QDialog()
                
                self.sub_ui2.setupUi(self.Dialog2, 1, self.cap2)
                
                self.Dialog2.show()
                self.camera2_flag = 1
                self.Dialog2.exec_()
                if self.sub_ui2.cap.isOpened():
                   self.sub_ui2.cap.release()
                if self.sub_ui2.timer_camera.isActive():
                   self.sub_ui2.timer_camera.stop()
                   self.camera2_flag = 0
            else:
                self.cap2.release()
                QMessageBox.information(self, "Info", "Camera 2 is Null", QMessageBox.Yes | QMessageBox.No)
        
    def Button_filename_clicked(self):
        base_filename = self.ui.Edit_filename.text()
        if base_filename == "":
           base_filename = "Video"
        self.filename_camera1 = ''.join((base_filename, "_camera1_"))
        self.filename_camera2 = ''.join((base_filename, "_camera2_"))
        print(self.filename_camera1)

    def Button_savepath_clicked(self):
        self.savepath = QFileDialog.getExistingDirectory(self, "Choose the path", './')
        self.savepath = ''.join((self.savepath, "/"))
        self.ui.Label_savepath.setText(self.savepath)
        self.filename_camera1 = ''.join((self.savepath, self.filename_camera1))
        self.filename_camera2 = ''.join((self.savepath, self.filename_camera2))

    def Button_recording_clicked(self):
        if self.filename_camera1 == "":
           self.filename_camera1 = ''.join(("Video", "_camera1_"))
        if self.filename_camera2 == "":
           self.filename_camera2 = ''.join(("Video", "_camera2_"))
        if self.savepath == "":
           self.savepath = "C:/"
           self.filename_camera1 = ''.join((self.savepath, self.filename_camera1))
           self.filename_camera2 = ''.join((self.savepath, self.filename_camera2))
        t=list(time.localtime()[3:7])
        t_str = [str(i) for i in t]
        t_str = ''.join(t_str)
        if hasattr(self, 'sub_ui1'):
           savename_camera1 = ''.join((self.filename_camera1, t_str, '.avi'))
           fourcc = cv2.VideoWriter_fourcc(*'XVID')
           self.sub_ui1.out = cv2.VideoWriter(savename_camera1,fourcc, 30.0, (640,480))
           self.sub_ui1.record_flag = 1
           self.ui.Label_mrecordingtime.setText("Recording")
           print(time.clock())
        if hasattr(self, 'sub_ui2'):
           savename_camera2 = ''.join((self.filename_camera2, t_str, '.avi'))
           fourcc = cv2.VideoWriter_fourcc(*'XVID')
           self.sub_ui2.out = cv2.VideoWriter(savename_camera2,fourcc, 30.0, (640,480))
           self.sub_ui2.record_flag = 1
        self.ui.Button_recording.setEnabled(False)
        print(self.filename_camera1)
        print(savename_camera1)
           
    def Button_endrecording_clicked(self):
        self.ui.Label_mrecordingtime.setText("")
        if hasattr(self, 'sub_ui1'):
           if self.sub_ui1.record_flag == 1:
              self.sub_ui1.record_flag = 0
              self.sub_ui1.out.release()
              print(time.clock())
        if hasattr(self, 'sub_ui2'):
           if self.sub_ui2.record_flag == 1:
              self.sub_ui2.record_flag = 0
              self.sub_ui2.out.release()
        self.ui.Button_recording.setEnabled(True)
        
    def Button_trigger_clicked(self):
        if self.filename_camera1 == "":
           self.filename_camera1 = ''.join(("Video", "_camera1_"))
        if self.filename_camera2 == "":
           self.filename_camera2 = ''.join(("Video", "_camera2_"))
        if self.savepath == "":
           self.savepath = "C:/"
           self.filename_camera1 = ''.join((self.savepath, self.filename_camera1))
           self.filename_camera2 = ''.join((self.savepath, self.filename_camera2))
        try:
           self.my_serial = serial.Serial('COM3', 9600, timeout=0.5)
        except:
           print('e')
        else:
           print("Waiting for triggering signal")
           self.timer_serial.start(5)
           self.ui.Button_trigger.setEnabled(False)
           
    def serial_timer_trigger(self):
        data = self.my_serial.read_all()
        if data != b'' :
           if data == b"STR":
              t=list(time.localtime()[3:7])
              t_str = [str(i) for i in t]
              t_str = ''.join(t_str)
              if hasattr(self, 'sub_ui1'):
                 savename_camera1 = ''.join((self.filename_camera1, t_str, '.avi'))
                 fourcc = cv2.VideoWriter_fourcc(*'XVID')
                 self.sub_ui1.out = cv2.VideoWriter(savename_camera1,fourcc, 30.0, (640,480))
                 self.sub_ui1.record_flag = 1
                 self.ui.Label_trecordingtime.setText("Recording")
                 print(time.clock())
              if hasattr(self, 'sub_ui2'):
                 savename_camera2 = ''.join((self.filename_camera2, t_str, '.avi'))
                 fourcc = cv2.VideoWriter_fourcc(*'XVID')
                 self.sub_ui2.out = cv2.VideoWriter(savename_camera2,fourcc, 30.0, (640,480))
                 self.sub_ui2.record_flag = 1
                 self.ui.Label_trecordingtime.setText("Recording")
              print("receive : ",data)
           if data == b"END":
              if hasattr(self, 'sub_ui1'):
                 if self.sub_ui1.record_flag == 1:
                    self.sub_ui1.record_flag = 0
                    self.sub_ui1.out.release()
                    print(time.clock())
                 self.ui.Label_trecordingtime.setText("")
              if hasattr(self, 'sub_ui2'):
                 if self.sub_ui2.record_flag == 1:
                    self.sub_ui2.record_flag = 0
                    self.sub_ui2.out.release()
                 self.ui.Label_trecordingtime.setText("")
              print("receive : ",data)
              print("***********Recording End***********")
        
    def Button_canceltrigger_clicked(self):
        if hasattr(self, 'my_serial'):
           if self.my_serial.isOpen():
              self.timer_serial.stop()
              self.my_serial.close()
              self.ui.Button_trigger.setEnabled(True)
              print("***********The serial port is closed*****************")

if __name__ == "__main__":
    MainProgram()
