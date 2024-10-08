1.Python: ตรวจสอบให้แน่ใจว่าคุณติดตั้ง Python (แนะนำให้ใช้เวอร์ชัน 3.6 หรือสูงกว่า).

2.Virtual Environment: สร้าง virtual environment เพื่อให้แยกแพ็กเกจและการตั้งค่าจากโปรเจคอื่น ๆ:
python -m venv myenv
myenv\Scripts\activate  # สำหรับ Windows

3.ติดตั้งไลบรารี:

OpenCV: ใช้สำหรับการประมวลผลภาพ:
    pip install opencv-python

MediaPipe: สำหรับการตรวจจับมือ:
    pip install mediapipe

NumPy: ใช้สำหรับการคำนวณ:
    pip install numpy