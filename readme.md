預測整個dicom中肝臟的位置，並將上下五張dicom一起打包成nii.gz檔，用於liver_segmentation的input

使用darknet yolov4實作

    git clone https://github.com/AlexeyAB/darknet
    chmod -R 777 darknet/
    
建置方法可以參考這位大大寫的教學

https://hackmd.io/@neverleave0916/YOLOv4

再把這篇的程式加入darknet的根目錄

    環境需求:
    CMake >= 3.12
    CUDA >=10.0 (For GPU)
    OpenCV >= 2.4 (For CPU and GPU)
    cuDNN >= 7.0 for CUDA 10.0 (for GPU)
    OpenMP (for CPU)
    Other Dependencies: make, git, g++

## 訓練預處理:
### prepare_data_jpg.py:

將dicom由nii.gz轉成jpg

input:

(x,512,512) dicom的nii.gz壓縮檔

output:
    
input資料的jpg檔

補充:將第8行input_file路徑改成自己的，如果是windows os的話20行split內容改成'\\'

    python prepare_data_jpg.py 

### prepare_data_txt.py
    
製作mask的bounding box並寫成txt

input:
    
(x,512,512) dicom的nii.gz壓縮檔,(x,512,512) mask的nii.gz壓縮檔

output:

mask的txt資料，train_data test_data的path寫成txt

補充:將第8,11,14行input_file路徑改成自己的，如果是windows os的話39,53,56行split內容改成'\\'

    python prepare_data_txt.py 

## 訓練:

    cd darknet
    make
    ./darknet detector train data/obj.data yolo-obj.cfg yolov4.weights -dont_show -mjpeg_port 8090 -map

## 預測:

### predict.py:

input:

(x,512,512)dicom的nii.gz檔

output:

dicom中有liver的部分nii.gz檔，存在new_nii.gz這個資料夾

補充:

第7行raw_niigz_path改成自己的input data path，若需查看個別一張dicom的預測結果可以使用下方指令

./darknet detector test data/obj.data yolo-obj.cfg backup/yolo-obj_best.weights [測試資料路徑] -dont_show

    python predict.py

