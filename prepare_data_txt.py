from cv2 import split
import numpy as np
import nibabel as nib
import glob
import os
import matplotlib.pyplot as plt

input_mask=''
mask_file=glob.glob(input_mask+'*')

input_dicom=''
dicom_file=glob.glob(input_dicom+'*')

output_file='darknet/data/obj/'
if not os.path.isdir(output_file):
    os.mkdir(output_file)

train_path='darknet/data/train.txt'
train_file=open(train_path,'w')
test_path='darknet/data/test.txt'
test_file=open(test_path,'w')

split_number=len(dicom_file)*0.8

###印txt from mask
def mask_txt():
    for mask_f in mask_file:
        print(mask_f)
        mask=nib.load(mask_f).get_data()
        for i,m in enumerate(mask):
            bbox_list=np.argwhere(m==1)
            if len(bbox_list)>0:
                yx_max=np.amax(bbox_list,axis=0)
                yx_min=np.amin(bbox_list,axis=0)
                y_mean=(yx_max[0]+yx_min[0])/2.0
                x_mean=(yx_max[1]+yx_min[1])/2.0
                width=(yx_max[1]-yx_min[1])/1.0
                height=(yx_max[0]-yx_min[0])/1.0
            txt_file=open(output_file+mask_f.split('/')[-1].replace('.nii.gz','_'+str(i)+'.txt'),'w')

            if not len(bbox_list)==0:
                txt_file.write('0'+' '+str(x_mean/512)+' '+str(y_mean/512)+' '+str(width/512)+' '+str(height/512))


#for train.txt and test.txt
def train_test_txt():
    for i,dicom_f in enumerate(dicom_file):
        print(dicom_f)
        dicom=nib.load(dicom_f).get_data()
        for j,d in enumerate(dicom):
            #for train.txt
            if i < split_number:
                train_file.write(output_file+dicom_f.split('/')[-1].replace('.nii.gz','_'+str(j)+'.jpg\n'))
            #for test.txt
            if i > split_number:
                test_file.write(output_file+dicom_f.split('/')[-1].replace('.nii.gz','_'+str(j)+'.jpg\n'))    
        

if __name__=='__main__':
    mask_txt()
    train_test_txt()
