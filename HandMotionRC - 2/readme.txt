1.Python: ກວດສອບໃຫ້ແນ່ໃຈວ່າຕິດຕັ້ງ Python.

2.Virtual Environment: ສ້າງ virtual environment ເພື່ອໃຫ້ຍົກແພັກເກຈແລະການຕັ້ງຄ່າຈາກໂປເຈັກອື່ນໆ:

# ສຳລັບ Windows
python -m venv myenv
myenv\Scripts\activate

#ສຳລັບ Mac
python -m venv myenv
source myenv/bin/activate 

3.ຕິດຕັ້ງໄລບາຣີ້:

- OpenCV: :
    pip install opencv-python

- MediaPipe: :
    pip install mediapipe

- NumPy: :
        pip install numpy<2.0 
        (ພິມໃນ command in  vs code)

    - ອັບເດໂມດູນທີ່ໄດ້ຮັບຜົນກະທົບ
        pip install --upgrade mediapipe tensorflow pybind11 ml_dtypes
        (ພິມໃນ command in  vs code)

        python -m venv myenv
        (ພິມໃນ command in  vs code)

        myenv\Scripts\activate  # ສຳລັບ Windows
        (ພິມໃນ command in  vs code)

        pip install numpy<2.0 mediapipe tensorflow
        (ພິມໃນ command in  vs code)

        pip freeze
        (ພິມໃນ command in  vs code)


    
