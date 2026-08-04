import cv2

from ultralytics import YOLO




class PillDetector:


    def __init__(self):


        self.model = YOLO(
            "pill_retrain.pt"
        )



        self.colors = {

            0: (0,255,0),     # 초록

            1: (0,0,255),     # 빨강

            2: (255,0,0)      # 파랑

        }





    def detect(
        self,
        frame
    ):

        """
        YOLO 추론 실행

        return:
            count  -> [A,B,C 개수]
            frame  -> 박스 표시된 이미지
        """



        pill_count = [
            0,
            0,
            0
        ]



        # 기존 전처리 유지

        dark = cv2.convertScaleAbs(
            frame,
            alpha=0.9,
            beta=-40
        )


        gray_frame = cv2.cvtColor(
            dark,
            cv2.COLOR_BGR2GRAY
        )



        # YOLO 추론

        results = self.model(
            gray_frame,
            conf=0.7,
            verbose=False
        )



        for result in results:


            for box in result.boxes:



                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )



                conf = float(
                    box.conf[0]
                )



                cls = int(
                    box.cls[0]
                )



                # 클래스 카운트

                if 0 <= cls <= 2:

                    pill_count[cls] += 1



                name = self.model.names[cls]


                color = self.colors.get(
                    cls,
                    (255,255,255)
                )



                # 검출 박스

                cv2.rectangle(
                    frame,
                    (x1,y1),
                    (x2,y2),
                    color,
                    2
                )



                # 텍스트 표시

                cv2.putText(
                    frame,
                    f"{name} {conf:.2f}",
                    (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )



        return pill_count, frame