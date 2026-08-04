import cv2



class Camera:


    def __init__(self):

        self.cap = None




    def open(
        self,
        camera_id=0
    ):

        """
        카메라 연결
        """


        self.cap = cv2.VideoCapture(
            camera_id
        )


        return self.cap.isOpened()





    def read(self):

        """
        현재 프레임 읽기
        """


        if self.cap and self.cap.isOpened():

            ret, frame = self.cap.read()

            return ret, frame



        return False, None





    def release(self):

        """
        카메라 해제
        """


        if self.cap and self.cap.isOpened():

            self.cap.release()