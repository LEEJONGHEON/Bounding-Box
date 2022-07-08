def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    # center x,y
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    # normalization
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


## 사진 wide, height 가져오기
# img=Image.open(img_path)
# w= int(img.size[0])
# h= int(img.size[1])
# example
w,h = 2000, 2000
# VOC 방식
xmin,xmax,ymin,ymax = 200,700,300,900


print(xmin, xmax, ymin, ymax)
b = (xmin, xmax, ymin, ymax)
bb = convert((w,h), b) # YOLO로 변환

print(bb)
