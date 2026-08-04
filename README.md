# 💊 Pill Vision - 알약 분류 및 개수 카운팅 시스템

## 📖 프로젝트 소개

Pill Vision은 **YOLO 기반 객체 탐지 기술**을 활용하여 웹캠 영상에서 알약을 실시간으로 분류하고 개수를 카운팅하는 프로그램입니다.

사용자가 하루 복용량을 입력하면 현재 검출된 알약 개수를 바탕으로 **남은 복용 가능 일수**를 계산하여 제공합니다.

본 프로젝트는 **PySide6 GUI**, **OpenCV**, **YOLO**를 활용하여 실제 약국 및 병원에서 사용할 수 있는 프로그램을 목표로 개발하였습니다.

---

## ✨ 주요 기능

* 실시간 웹캠 영상 출력
* YOLO 기반 알약 객체 탐지
* 알약 종류(A/B/C) 자동 분류
* 클래스별 개수 카운팅
* 하루 복용량 입력
* 남은 복용 가능 일수 자동 계산
* 클래스별 Bounding Box 표시
* 실시간 객체 탐지 결과 표시

---

## 🖥️ 프로그램 화면


```
![picture](/assets/demo.png)
```

---

## ⚙️ 기술 스택

### Language

* Python

### Deep Learning

* YOLO (Ultralytics)

### Computer Vision

* OpenCV

### GUI

* PySide6 (Qt)

### Development Environment

* Visual Studio Code

---

## 📂 프로젝트 구조

```text
pill_vision/
│
├── main.py                 # 프로그램 실행
├── ui.py                   # GUI
├── camera.py               # 웹캠 제어
├── yolo.py                 # YOLO 추론
├── pill.py                 # 복약 계산
├── pill_retrain.pt         # 학습 모델
└── README.md
```

---

## 🔍 동작 과정

1. 웹캠을 실행합니다.
2. OpenCV로 프레임을 읽습니다.
3. 이미지 전처리를 수행합니다.
4. YOLO 모델이 알약을 탐지합니다.
5. 알약 종류를 분류합니다.
6. 클래스별 개수를 계산합니다.
7. Bounding Box를 출력합니다.
8. 사용자가 하루 복용량을 입력합니다.
9. 버튼 클릭시 남은 복용 가능 일수를 계산하여 출력합니다.

---

## 🧠 이미지 전처리

YOLO 추론 전 다음과 같은 전처리를 수행합니다.

* 밝기 보정
* Grayscale 변환

이를 통해 학습 데이터와 동일한 입력 환경을 유지하여 탐지 성능을 높였습니다.

---

## 📊 객체 탐지

YOLO 모델을 이용하여

* A Type
* B Type
* C Type

총 3개의 알약 클래스를 실시간으로 탐지합니다.

각 객체는

* Bounding Box
* Class Name
* Confidence Score

를 함께 출력합니다.

---

## 💡 복약 계산 기능

사용자가 하루 복용량을 입력하면

```
남은 복용일 = 현재 알약 개수 ÷ 하루 복용량
```

을 계산하여 화면에 표시합니다.

---

## 🖼️ GUI

PySide6를 이용하여 병원 및 약국 프로그램 스타일의 UI를 구성했습니다.

* 카드형 정보 패널
* 실시간 웹캠 화면
* 직관적인 입력창
* 복약 정보 출력
* 반응형 레이아웃

---

## 🚀 실행 방법

### 1. 저장소 다운로드

```bash
git clone https://github.com/your-id/pill-vision.git
```

### 2. 라이브러리 설치

```bash
pip install -r requirements.txt
```

또는

```bash
pip install PySide6 opencv-python ultralytics
```

### 3. 모델 준비

프로젝트 폴더에

```
pill_retrain.pt
```

파일을 위치시킵니다.

### 4. 실행

```bash
python main.py
```

---

## 📌 개발 환경

* Python 3.9.23
* PySide6
* OpenCV 4.10
* Ultralytics YOLO

---

## 📈 향후 개선 사항

* 다양한 알약 클래스 지원
* ONNX/TensorRT 최적화
* Embedded AI 환경 지원

---

## 👨‍💻 개발자

개인 프로젝트로 개발한 **YOLO 기반 실시간 알약 분류 및 개수 카운팅 시스템**입니다.
