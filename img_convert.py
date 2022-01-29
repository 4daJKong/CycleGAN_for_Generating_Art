import cv2
import os
folder = "./Joensuu_ori"
savepath = "./Joensuu_imgs"
if not os.path.exists(savepath):
    os.mkdir(savepath)
idx = 1
for filename in os.listdir(folder):

    #if (filename == "20220127235420.jpg"): #test
    
    img = cv2.imread(os.path.join(folder, filename))
    resize_img_ori = cv2.resize(img, (256, 256),interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(savepath, str(idx)+'-0.jpg'), resize_img_ori)
    img_h = img.shape[0]
    img_w = img.shape[1]
    if (img_h < img_w):
        img_c = int(img_w / 5) #divide into 4 sub-imgs    
        for j in range(1, 5):
            crop_img = img[ 0:img_h, img_c*(j-1): img_c*(j+1)]
            resize_img = cv2.resize(crop_img, (256, 256))
            cv2.imwrite(os.path.join(savepath, str(idx)+'-'+str(j)+'.jpg'), resize_img)  
    else:          
        img_c = int(img_h / 5)
        for j in range(1, 5):
            crop_img = img[img_c*(j-1): img_c*(j+1), 0:img_w]   
            resize_img = cv2.resize(crop_img, (256, 256))
            cv2.imwrite(os.path.join(savepath, str(idx)+'-'+str(j)+'.jpg'), resize_img)
    idx = idx + 1