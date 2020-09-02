# -*- coding: utf-8 -*-

# opencv 라이브러리가 설치되지 않아 구동이 안되면 커맨드에서 아래의 명령어를 입력해 opencv 라이브러리를 먼저 설치해야 함.  
# pip install opencv-python

import cv2

# OpenCV를 이용해 캠으로 들어오는 영상을 cap 변수에 넣음, '0'은 컴퓨터가 인식한 첫번째 카메라를 의미함
cap = cv2.VideoCapture(0)

print('Press "q", if you want to quit')

# while문 안의 내용을 계속 반복시킴. 캠에서 영상 프레임이 들어올 때마다 아래 프로그램을 실행함
while(True):
    # cap 변수에 비디오 프레임이 들어올 때마다 읽어서 frame 변수에 넣음, 제대로 프레임이 읽어지면 ret값이 True, 실패하면 False가 나타남
    ret, frame = cap.read()

    # 들어온 이미지 플립, 이미지 좌우반전(1은 좌우반전, 0은 상하반전)
    flip_frame = cv2.flip(frame, 1)

    # 이미지 높이, 폭 추출
    h = flip_frame.shape[0]
    w = flip_frame.shape[1]

    # 이미지를 teachable machine이 학습할 때 사용하는 이미지 비율로 크롭
    crop_image = flip_frame[0:h, int((w-h)/2):int(w-((w-h)/2))]

    # 원본이미지, 플립이미지, 크롭이미지
    cv2.imshow('frame',frame)
    # cv2.imshow('flip_frame',flip_frame)
    # cv2.imshow('crop_image',crop_image)


    # 키 입력을 기다림
    key = cv2.waitKey(1) & 0xFF

    # q 키를 눌렀다면 반복실행에서 종료함
    if key == ord("q"):
        print('Quit')
        break

# 동작이 종료되면 비디오 프레임 캡쳐를 중단함
cap.release()
# 모든 창을 닫음
cv2.destroyAllWindows()
