import cv2
from mtcnn.mtcnn import MTCNN

def mtcnn_pic(detector, pic_path):
    image = cv2.imread(pic_path)
    result = detector.detect_faces(image)
    
    if result != []:
            print('result\nn: ')
            print(len(result))
            for person in result:
                bounding_box = person['box']
                keypoints = person['keypoints']
        
                cv2.rectangle(image,
                              (bounding_box[0], bounding_box[1]),
                              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                              (0,155,255),
                              2)
        
                cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
                cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
                cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
                cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
                cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)  
    
    cv2.imwrite("mtcnn_drawn.png", image)
    cv2.namedWindow("image")
    cv2.imshow("image",image)
    cv2.waitKey(0)

def mtcnn_cam(detector, video_path=False):
    
    if video_path:  # video 입력 받을 때
        cap = cv2.VideoCapture(video_path)
    else:   #아니면 webcam input
        cap = cv2.VideoCapture(0)
    
    while True: 
        #Capture frame-by-frame
        __, frame = cap.read()
        
        #Use MTCNN to detect faces
        result = detector.detect_faces(frame)
        
        
        if result != []:
            print('result\nn: ')
            print(len(result))
            for person in result:
                bounding_box = person['box']
                keypoints = person['keypoints']
        
                cv2.rectangle(frame,
                              (bounding_box[0], bounding_box[1]),
                              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                              (0,155,255),
                              2)
        
                cv2.circle(frame,(keypoints['left_eye']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['right_eye']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['nose']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['mouth_left']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['mouth_right']), 2, (0,155,255), 2)
        #display resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    #When everything's done, release capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    pic_path = 'happy.png'
    video_path ='/0Library/My video/00영상 강의/Deep learning _15일 트랙3 세션1.mp4'
    detector = MTCNN()
    #mtcnn_pic(detector,pic_path )
    mtcnn_cam(detector)
    