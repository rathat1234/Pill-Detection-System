import cv2


from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QFormLayout,
    QLineEdit
)


from PySide6.QtCore import (
    QTimer,
    Qt
)


from PySide6.QtGui import (
    QImage,
    QPixmap
)



from camera import Camera

from yolo import PillDetector

from pill import PillManager





class My_App(QWidget):


    def __init__(self):

        super().__init__()



        # =====================
        # 모듈 연결
        # =====================


        self.camera = Camera()

        self.detector = PillDetector()

        self.pill_manager = PillManager()



        # =====================
        # 타이머
        # =====================


        self.timer = QTimer(self)


        self.timer.timeout.connect(
            self.update_frame
        )



        # =====================
        # 데이터
        # =====================


        self.pill_class = [
            0,
            0,
            0
        ]



        self.pill_type = [
            "A",
            "B",
            "C"
        ]



        self.edtPdaily = []

        self.lbTotalCount = []

        self.lbLeftDay = []



        self.init_UI()



        # 카메라 자동 시작

        self.start_camera()






    def init_UI(self):


        self.setWindowTitle(
            "Pill Vision Management System"
        )


        self.resize(
            1280,
            700
        )



        self.setStyleSheet("""


        QWidget {

            background:#f7faff;

            font-family:"Malgun Gothic";

        }



        QGroupBox {


            background:white;

            border:2px solid #bbdefb;

            border-radius:15px;

            margin-top:15px;

            padding:15px;

            color:#1565c0;

            font-weight:bold;

        }



        QLineEdit {


            border:1px solid #90caf9;

            border-radius:8px;

            padding:8px;

            background:white;

        }



        QPushButton {


            background:#1976d2;

            color:white;

            border-radius:10px;

            height:45px;

            font-weight:bold;

        }



        QPushButton:hover {


            background:#1565c0;

        }


        """)



        # =====================
        # 영상 출력
        # =====================


        self.image_label = QLabel()


        self.image_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )


        self.image_label.setMinimumSize(
            700,
            520
        )


        self.image_label.setStyleSheet("""


        QLabel {


            background:#111827;

            border-radius:20px;

            border:4px solid #90caf9;

        }


        """)




        self.btn_start = QPushButton(
            "복약 데이터 분석"
        )


        self.btn_start.clicked.connect(
            self.start_webcam
        )




        # =====================
        # 약 카드
        # =====================


        right_layout = QVBoxLayout()



        for pill in self.pill_type:


            group = QGroupBox(
                pill + " Type"
            )



            form = QFormLayout()



            edit = QLineEdit()


            edit.setPlaceholderText(
                "하루 복용량"
            )


            self.edtPdaily.append(
                edit
            )


            form.addRow(
                "하루 섭취량",
                edit
            )



            total = QLabel(
                "0 개"
            )


            total.setStyleSheet(
                """
                QLabel{
                    color:#1565c0;
                    font-size:18px;
                    font-weight:bold;
                }
                """
            )


            self.lbTotalCount.append(
                total
            )



            form.addRow(
                "현재 개수",
                total
            )



            days = QLabel(
                "0 일"
            )



            days.setStyleSheet(
                """
                QLabel{
                    color:#1565c0;
                    font-size:18px;
                    font-weight:bold;
                }
                """
            )


            self.lbLeftDay.append(
                days
            )



            form.addRow(
                "예상 복용일",
                days
            )



            group.setLayout(
                form
            )


            right_layout.addWidget(
                group
            )




        left_layout = QVBoxLayout()


        left_layout.addWidget(
            self.image_label
        )


        left_layout.addWidget(
            self.btn_start
        )



        main_layout = QHBoxLayout()


        main_layout.addLayout(
            left_layout,
            3
        )


        main_layout.addLayout(
            right_layout,
            1
        )



        self.setLayout(
            main_layout
        )
    def start_camera(self):
        

        """
        웹캠 시작
        """


        if self.camera.open():

            self.timer.start(
                30
            )





    def start_webcam(self):

        """
        현재 검출된 약 개수 기준
        복용 가능 일수 계산
        """


        temp = self.pill_class.copy()



        for i in range(3):


            # 현재 개수 표시

            self.lbTotalCount[i].setText(
                f"{temp[i]} 개"
            )



            try:

                daily = int(
                    self.edtPdaily[i].text()
                )


            except ValueError:

                daily = 0




            days = self.pill_manager.calculate_days(
                temp[i],
                daily
            )



            self.lbLeftDay[i].setText(
                self.pill_manager.format_days(
                    days
                )
            )






    def update_frame(self):

        """
        카메라 프레임 업데이트
        YOLO 결과 표시
        """



        ret, frame = self.camera.read()



        if ret:



            # YOLO 추론

            self.pill_class, frame = self.detector.detect(
                frame
            )



            # BGR -> RGB

            rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )



            h, w, ch = rgb.shape


            bytes_per_line = ch * w



            q_image = QImage(
                rgb.data,
                w,
                h,
                bytes_per_line,
                QImage.Format.Format_RGB888
            )



            pixmap = QPixmap.fromImage(
                q_image
            )



            scaled = pixmap.scaled(
                self.image_label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )



            self.image_label.setPixmap(
                scaled
            )







    def closeEvent(
        self,
        event
    ):

        """
        종료 처리
        """



        self.timer.stop()



        self.camera.release()



        event.accept()