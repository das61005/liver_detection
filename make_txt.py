
import nibabel as nib
import glob
import re
import matplotlib.pyplot as plt

def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text): 
    return [atoi(c) for c in re.split(r'(\d+)', text)]

dicom_path='D:\\Rai_Thran\\liver_seg_full\\test_jpg\\'
dicom_file=glob.glob(dicom_path+"*")
dicom_file.sort(key=natural_keys)

output_file=open('D:\\Rai_Thran\\liver_seg_full\\test2.txt','w')

def to_txt():
    for dicom_f in dicom_file:
        print(dicom_f)
        output_file.write('test_jpg/'+dicom_f.split('\\')[-1]+'\n')
           
if __name__=='__main__':
    to_txt()