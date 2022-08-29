import numpy as np
import nibabel as nib
import glob
import imageio
import os
from PIL import Image  
import matplotlib.pyplot as plt
input_file='D:\\Rai_Thran\\liver_seg_full\\dicom_for_liver_seg\\'
glob_file=glob.glob(input_file+'*')

output_file='darknet/data/obj/'
if not os.path.isdir(output_file):
    os.mkdir(output_file)

for glob_f in glob_file:
    print(glob_f)
    mask=nib.load(glob_f).get_data()
    for i,m in enumerate(mask):
        im = Image.fromarray((m*255).astype(np.uint8))
        imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_'+str(i)+'.jpg'),im)
        # im_r90=im.rotate(90)
        # imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_r90_'+str(i)+'.jpg'),im)
        # im_r180=im.rotate(180)
        # imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_r180_'+str(i)+'.jpg'),im)
        # im_r270=im.rotate(270)
        # imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_r270_'+str(i)+'.jpg'),im)
        # im_frl=im.transpose(method=Image.FLIP_LEFT_RIGHT)
        # imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_frl_'+str(i)+'.jpg'),im)
        # im_ftd=im.transpose(method=Image.FLIP_TOP_BOTTOM)
        # imageio.imwrite(output_file+glob_f.split('\\')[-1].replace('.nii.gz','_ftd_'+str(i)+'.jpg'),im)



        