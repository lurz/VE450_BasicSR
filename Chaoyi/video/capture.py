import​ ​cv2 

def​ ​FrameCapture​(path):
    vidObj = cv2.VideoCapture(path)     
    count = ​0     
    success = ​1     
    ​while​ success ​and​ count < ​2000​:         
        success, image = vidObj.read()         
        image = image         
    ​    if​ count % ​5​ == ​0​:
            blur_image = image/​5
        ​else​:
            ​if​ count % ​5​ == ​2​:
                clear_image = image
                blur_image = cv2.add(blur_image, image/​5​)         
        ​if​ count % ​5​ == ​4​:             
            cv2.imwrite(​"./fulldata_2/blurred/​%d​.png"​ % (count//​5​), blur_image)             
            cv2.imwrite(​"./fulldata_2/ground_truth/​%d​_true.png"​ % (count//​5​), clear_image) 
            blur_image = ​None             
            clear_image = ​None         
        count += ​1 
def​ ​main​():     
    FrameCapture(​"./HascoDataSet/2.h264"​) 
if​ __name__ == ​'__main__'​:     
    main()