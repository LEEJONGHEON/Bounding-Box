# Bounding-Box

## COCO DataSet
- 바운딩 박스 좌표(x,y,w,h)
- 좌상단 (x,y) , 가로 세로
### ![image](https://user-images.githubusercontent.com/54635552/178009306-be313108-f687-4583-bb5e-95f8f8f1a1a9.png)
### Yolo TO COCO Reference
- https://github.com/Taeyoung96/Yolo-to-COCO-format-converter

- Example CODE : YOLO_TO_COCO.ipynb

- !python path_replacer.py --path_image_folder /content/Yolo-to-COCO-format-converter/tutorial/train --path_txt /content/Yolo-to-COCO-format-converter/tutorial/train.txt
- Image경로를 저장한 train.txt파일 생성
- train.txt 내용
### ![image](https://user-images.githubusercontent.com/54635552/178026394-61837e54-d9af-47bf-b0d2-8a1649454146.png)

- !python main.py --path /content/Yolo-to-COCO-format-converter/tutorial/train.txt --output train.json
- Image경로를 이용한 train.json파일 생성
- train.json 내용
- 이미지 정보
### ![image](https://user-images.githubusercontent.com/54635552/178026952-4ef66efb-e735-46c0-96fe-0cc5be284abf.png)
- Annotation 정보
### ![image](https://user-images.githubusercontent.com/54635552/178027017-24c207e9-5f65-4a13-8dea-29bb947598e9.png)

- !python main.py --path /content/Yolo-to-COCO-format-converter/tutorial/train.txt --output train --debug
- Bounding box debug 모드, GUI방식에서만가능
### ![image](https://user-images.githubusercontent.com/54635552/178028752-01d874e5-c027-4705-a1a8-eb4f0515fbf6.png)


## YOLO DataSet
- 바운딩 박스 좌표(x,y,w,h)
- 중심점 (x,y) , 가로 세로
### ![image](https://user-images.githubusercontent.com/54635552/178009327-939cdc01-9e40-4678-a493-e7c78a07faac.png)
### VOC_TO_YOLO.py
- KITTI,VOC 형식 YOLO로 바꾸고 Normalization까지 진행하는 코드

## KITTI , VOC DataSet
- 바운딩 박스 좌표(x,y,x,y)
- 좌상단 (x,y), 우하단 (x,y)
### ![image](https://user-images.githubusercontent.com/54635552/178009347-e9fc319d-aa20-4c9f-aac7-3f40d3142dc2.png)
