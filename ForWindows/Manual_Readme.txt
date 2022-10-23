-- วิธีเปิด Project --
1. เปิด cmd ที่โฟร์เดอร์นี้!! (สำคัญมาก)
	path ของ cmd ต้องตรงกับโฟร์เดอร์โปรเจคเท่านั้น
2. จากนั้นพิมคำสั่ง 
	2.1 Envforwindows\scripts\activate (เพื่อใช้งาน Vitual Environment)
	2.2 py mainformfinal.py

-- วิธีที่ 1.1 เปิด Virtual Environment --
  เปิด cmd ที่ folder โปรเจค
  แล้วพิมพ์ Envforwindows\scripts\activate.bat (ใช้ได้กับ Windows เท่านั้น)
  แล้วพิมพ์ py mainformfinal.py หรือ python mainformfinal.py

  (สำหรับ MacOS)
  เปิด terminal ที่ folder โปรเจค
  แล้วพิมพ์ source Env/bin/activate (ใช้ได้กับ MacOS เท่านั้น)
  *หากไม่ได้ให้ cd ไปที่ Env แล้วก็ bin โดยพิมพ์
   cd Env
   cd bin
   source activate*
  แล้วพิมพ์ py mainformfinal.py หรือ python mainformfinal.py
  
(แนะนำ) -- วิธีที่ 1.2 ใช้ Virtual Environment ผ่าน VScode(Visual Studio code) --
  เปิด folder โปรเจคไปที่ VScode
  แล้วเลือก Interpreter เป็น "Python 3.10.6 ('env': venv)"

(แนะนำ) -- วิธีที่ 1.3 ติดตั้ง Libary --
  โดยเปิด cmd ที่ folder โปรเจค
  แล้วพิมพ์ pip install -r requirements.txt


หากรันไม่ได้
ให้ลองเปลี่ยนคำสั่งที่ 2.2 เป็น python mainformfinal.py