import sys
from tkinter import ttk
from userdb import *
from PIL import ImageTk, Image
import sqlite3
import requests
import json
import random
import gc
import tkinter as tk

food_child = {"อาหารคาว": {"แกง": {1: "แกงจืดหมูสับไข่น้ำ", 2: "แกงพะโล้", 3: "แกงจืดไข่ม้วนหมูห่อสาหร่าย", 4: "แกงจืดแตงกวายัดไส้วุ้นเส้นหมูสับ", 5: "แกงจืดดอกโสนหมูนุ่มเต้าหู้ไข่", 6: "ข้าวแกงกะหรี่", 7: "แกงส้มปลาแซวม่อน", 8: "แกงเขียวหวานไก่", 9: "แกงส้มชะอมกุ้ง", 10: "แกงเทโพ", 11: "แกงเลียง", 12: "แกงพะแนง", 13: "แกงอ่อมไก่", 14: "แกงขี้เหล็ก", 15: "แกงอ่อม", 16: "แกงหน่อไม้", 17: "แกงเหลืองสัปปะรด ไข่เจียว", 18: "แกงเหลืองมะละกอ", 19: "แกงไหล่เหลืองบัว", 20: "แกงปู"},
                           "ผัด": {1: "ผัดซีอิ๊ว", 2: "ผัดหมี่", 3: "ข้าวผัดหมูกระเทียม", 4: "ข้าวหอมควินัว ตับผัดกระเทียม", 5: "พาสต้าเครสเต้ริกาเต้ผัดไข่ใส่กุ้ง", 6: "ข้าวหมูสับผัดกระเทียม ไข่เจียวเนย", 7: "ข้าวผัดกุ้ง", 8: "ข้าวผัดกระเทียมไข่ข้นกุ้งสด", 9: "ผัดไทยกุ้งสด", 10: "ปูผัดผงกะหรี่", 11: "ข้าวผัดคะน้าหมูกรอบ", 12: "ผัดคั่วกลิ้ง", 13: "ผัดกะเพราไข่ดาว", 14: "ผัดกวางตุ้งหมูสับ", 15: "หมูกรอบผัดกุยช่าย", 16: "ข้าวผัดอเมริกัน", 17: "ไก่ผัดกะปิ", 18: "ไก่ผัดเต้าหู้อ่อน", 19: "ข้าวผัดปลาทูน้ำพริกกะปิ", 20: "ผัดเปรี้ยวหวานปลา"},
                           "ทอด": {1: "ปีกไก่ทอด", 2: "น่องไก่ทอดน้ำปลา", 3: "ไก่ทอดหาดใหญ่", 4: "ไก่ทอดวิงส์แซ่บ", 5: "หมูแดดเดียวทอด", 6: "หมูสามชั้นทอด", 7: "หมูทอดเชียงราย", 8: "ซี่โครงหมูทอด", 9: "เนื้อทอด", 10: "เอ็นข้อไก่ทอด", 11: "ปากเป็ดทอดกระเทียม", 12: "ข้าวโพดทอดหมูสับ", 13: "กุยช่ายทอด", 14: "เปาะเปี๊ยะทอด", 15: "ทอดมัน", 16: "กุ้งฝอยทอดกรอบ กุ้งแพ", 17: "กุ้งทอดกระเทียมราดข้าว", 18: "ผักชุบแป้งทอด", 19: "ปลาหมึกชุบแป้งทอด", 20: "ไก่ทอดดองเบลอ"},
                           "ต้ม นึ่ง หรือตุ๋น": {1: "ข้าวต้มกุ้งเต้าหู้สาหร่าย", 2: "ปีกไก่ตุ๋น ฮ่องกง", 3: "ต้มจับฉ่าย", 4: "ปลากระพงนึ่งมะนาว", 5: "ต้มซุปไก่มันฝรั่ง", 6: "เกี๊ยวปลา", 7: "ต้มซุปกิมจิ", 8: "กระเพาะปลา", 9: "ซุปมักกะโรนีแฮมเส้น", 10: "ไก่ตุ๋นฟัก", 11: "ซี่โครงหมูตุ๋นเยื่อไผ่", 12: "ต้มข่ากุ้ง", 13: "ซุปไข่มักกะโรนี", 14: "ต้มส้มปลากระบอก", 15: "ปลาเก๋าต้มเผือก", 16: "แกงจืดกะหล่ำปลียัดไส้หมูสับ", 17: "เกี๊ยวน้ำ", 18: "ต้มกะทิหมู", 19: "ต้มจิ๋วเนื้อ", 20: "ต้มผักกาดดองกระดูกอ่อนหมู"}},
              "อาหารหวาน": {"น้ำ": {1: "ไอศกรีมกะทิ", 2: "ลูกตาลเชื่อม", 3: "ถั่วเขียว เม็ดบัว ต้มน้ำลำไย", 4: "วุ้นพีชในน้ำมะม่วง", 5: "บัวลอยไข่หวาน", 6: "กล้วยบวชชี", 7: "ขนมครองแครงน้ำกระทิ", 8: "บิงซู", 9: "ขนมเปียกปูนกะทิสด", 10: "เฉาก๊วย", 11: "สาคูบัวลอยมะพร้าวอ่อนกะทิสด", 12: "ทับทิมกรอบกะทิสด", 13: "แกงบวดลูกตาลกะทิสด", 14: "แกงบวดถั่วดำ", 15: "ลาดช่องน้ำกระทิ"},
                            "แห้ง": {1: "เค้กเนยนมหน้ากรอบ", 2: "คุกกี้", 3: "บราวน์นี่โกโก้", 4: "แพนเค้ก", 5: "เค้กมะพร้าว", 6: "เค้กสติ๊ก", 7: "แพนเค้ก", 8: "ขนมโค", 9: "บราวนี่ไมโล", 10: "วุ้นเป็ด", 11: "เค้กกล้วยหอม", 12: "ขนมเข่งไส้เค็ม", 13: "เค้กไข่แซนด์วิชสตรอว์เบอร์รี่", 14: "ขนมชอล์ก", 15: "บ้าบิ่น"}}}

food_teen = {"อาหารคาว": {"แกง": {1: "ข้าวราดผัดพริกแกงถั่วฟักยาว ไข่ดาว", 2: "ข้าวราดแกงส้มหน่อไม้ดอง ไข่เจียว", 3: "ขนมจีนแกงเขียวหวาน ลูกชิ้นปลา", 4: "แกงพะโล้", 5: "ข้าวแกงกะหรี่ หมูทงคัตสึ", 6: "ห่อหมกทะเล", 7: "แกงเลียง ไข่เจียว", 8: "แกงเห็ด", 9: "ขนมจีนแกงใต้", 10: "น้ำพริกแกงไตปลา", 11: "ข้าวยำเกาหลี", 12: "ข้าวผัดกิมจิชีสลาวาโจ๊กหมูเด้งโคชูจัง", 13: "แกงจืดเต้าหู้หมูสับ", 14: "ขนมจีนแกงคั่วหมู", 15: "แกงคั่วหมูย่าง", 16: "แกงคั่วหัวตาลกุ้งสด", 17: "แกงคั่วสับปะรดหอยแมลงภู่", 18: "แกงคั่วหอยขม", 19: "แกงคั่วหน่อไม้", 20: "แกงคั่วซี่โครงหมูใส่หน่อเหรียง"},
                          "ผัด": {1: "คะน้าฮ่องกงผัดน้ำมันหอยเจ", 2: "ผัดบวบใส่ไข่และกุ้ง", 3: "ผัดหมี่กรอบ", 4: "ผัดกะเพราทะเลไข่ดาว", 5: "ดอกหอมผัดตับ", 6: "พาสต้าผัดขี้เมาทะเล", 7: "ผัดคะน้าปลากระป๋อง", 8: "ข้าวผัดกะเพราเนื้อตุ๋น ไข่เยี่ยวม้า", 9: "ผัดหมี่ซั่ว", 10: "ผัดไทยกุ้งสด ", 11: "ผัดวุ้นเส้น", 12: "ผัดผักรวมมิตรเจ", 13: "ไก่ผัดเม็ดมะม่วงหิมพานต์", 14: "ผัดพริกแกง", 15: "โปรตีนเกษตรผัดพริก(เจ)", 16: "ยากิโซบะผัดซอสมะเขือเทศ", 17: "มาม่าผัดขี้เมา", 18: "ข้าวผัด(เจ)", 19: "ข้าวผัดเต้าหู้(เจ)", 20: "ผัดซีอิ๊ว"},
                          "ทอด": {1: "ส้มตำทอด", 2: "หนวดปลาหมึกทอด", 3: "ปาท่องโก๋", 4: "หมูกรอบน้ำมันหอย", 5: "ทอดมันกุ้ง", 6: "เบอร์เกอร์ไก่กรอบ", 7: "กุยช่ายทอด", 8: "ปลากระป๋องทอดกระเทียม", 9: "ราดหน้าเกี๊ยวกรอบหมูเด้ง", 10: "ข้าวโพดทอดไส้นม", 11: "กุ้งคั่วพริกเกลือประทัดลม", 12: "ถุงทองกุ้ง", 13: "กุ้งกรอบซอสครีมเลมอน", 14: "ขลุ่ยกุ้ง", 15: "นักเก็ตไก่", 16: "ไก่ทอดขิงกรอบ", 17: "แซนวิชหอยจ๊อกุ้ง", 18: "ทอดมันข้าวโพดไข่เค็ม", 19: "เมี่ยงทอด", 20: "ทอดมันเห็ด"},
                          "ต้ม นึ่ง หรือตุ๋น": {1: "ไข่ตุ๋นหมูสับกุ้ง", 2: "ไก่พริกไทยดำตุ๋นเบียร์", 3: "ไก่ตุ๋นมะระ", 4: "ก๋วยเตี๋ยวเนื้อตุ๋น", 5: "ปีกไก่ตุ๋น", 6: "ต้มยำกุ้ง", 7: "ปลากระพงนึ่งมะนาว", 8: "ต้มข่าอ่อน", 9: "ข้าวต้มปลาอินทรีย์", 10: "ไก่ต้มฟักเขียว", 11: "หมูต้มเค็ม", 12: "หมูต้มหวาน", 13: "บ๊ะจ่าง", 14: "กระดูกหมูต้มจืด", 15: "หมูต้มซีอิ๊ว", 16: "กระดูกหมูต้มแซ่บ", 17: "กระดูกหมูตุ๋นรากบัว", 18: "ไก่ต้มน้ำปลา", 19: "ไก่ต้มใบมะขามอ่อน", 20: "ต้มซุปเปอร์ขาไก่"}},
             "อาหารหวาน": {"น้ำ": {1: "บิงซูเมล่อน", 2: "ลอดช่องน้ำกะทิ", 3: "เฉาก๊วย", 4: "ทับทิมกรอบ", 5: "ไอศกรีม", 6: "วุ้นกะทิ", 7: "หวานเย็น", 8: "ไอศกรีมทอด", 9: "เครปเย็น", 10: "ช็อกโกแลตสมูทตี", 11: "คุกกี้แอนด์ครีมมิลค์เชค", 12: "ยูนิคอร์นเฟรปเป้", 13: "โบ๊กเกี้ย", 14: "โอ้เอ๋ว", 15: "มะยงชิดลอยแก้ว"},
                           "แห้ง": {1: "แพนเค้ก", 2: "โตเกียว", 3: "โตเกียวเนยกรอบ", 4: "เครป", 5: "ปาท่องโก๋", 6: "ขนมไข่หงส์", 7: "ลูกชุป", 8: "ขนมควยลิง", 9: "ขนมครก", 10: "ขนมปังปิ้งสังขยา", 11: "ทองหยิบ", 12: "ทองหยอด", 13: "ฝอยทอง", 14: "ขนมเทียน", 15: "ดังโงะ"}}}

food_Adult = {"อาหารคาว": {"แกง": {1: "แกงคั่วหน่อไม้ซี่โครงหมู", 2: "แกงผักปังใส่แหนม", 3: "แกงจืดไข่ม้วน", 4: "แกงมะเขือเทศหมูสับ", 5: "แกงจืดสับปะรดกระดูกอ่อน", 6: "แกงจืดฟักซี่โครงหมู", 7: "ขนมจีนพริกแกงใต้", 8: "น้ำพริกกระปิ ปลาทูทอด ไข่เจียว", 9: "แกงรัญจวน", 10: "แกงเขียวหวานหมู ไข่เจียว", 11: "แกงคั่วหมูเทโพ", 12: "แกงขนุนใส่ซี่โครง", 13: "แกงโฮะ", 14: "แกงไตปลา", 15: "แกงฮังเล", 16: "แกงอ่อมหมู", 17: "คั่วพริกแกงหมูป่า", 18: "แกงป่าหมู", 19: "แกงเทโพหมู", 20: "แกงเผ็ดกล้วยดิบ"},
                           "ผัด": {1: "ราดหน้าฮ่องกง", 2: "ผัดกวางตุ้งหมูสับ", 3: "มะละกอผัดวุ้นเส้น", 4: "โชกะยากิ", 5: "หมูกรอบผัดกุยช่าย", 6: "ไข่ผัดเห็ดหอมเต้าหู้อ่อน", 7: "สปาเก็ตตี้ผัดขี้เมา", 8: "ตับผัดหน่อไม้ฝรั่ง", 9: "บะหมี่แห้งผัดกะเพราหมูสับ", 10: "ข้าวผัดหมูแดง", 11: "ผัดสะตอปลา", 12: "ผัดเผ็ดปลาดุก", 13: "แกงคั่วแห้งกุ้งมะพร้าวอ่อนใบชะพลู", 14: "ข้าวผัดปลาทูน้ำพริกกะปิ", 15: "ไก่ผัดขิง", 16: "ไก่ผัดเม็ดมะม่วงหิมพานต์", 17: "ผัดไทยกุ้งสด", 18: "ผัดผักบุ้ง", 19: "ไก่ผัดกะปิ", 20: "ไก่ผัดขิง"},
                           "ทอด": {1: "หมูทอดกะปิ", 2: "หมูทอด", 3: "หมูโสร่ง", 4: "พริกหยวกหมูสับ", 5: "ยำหมูกรอบ", 6: "หมูกรอบ", 7: "ข้าวหมูกรอบ", 8: "จ๋ายอ", 9: "ขนมปังหน้าหมู", 10: "ทอดมันปลากราย", 11: "ยำปลาดุกฟู", 12: "ปลาช่อนลุยสวน", 13: "ปลากระพงทอดน้ำปลา", 14: "ปลาเนื้ออ่อนราดพริก", 15: "ปลาอินทรีย์ทอดซีอิ๊ว", 16: "ปีกไก่ทอดน้ำแดง", 17: "ปีกไก่ทอดตะไคร้", 18: "ไก่ทอดเกาหลี", 19: "ไก่ทอดกระเทียมพริกไทย", 20: "ไก่บอนชอน"},
                           "ต้ม นึ่ง หรือตุ๋น": {1: "บะกุ๊ดเต๋", 2: "ขาหมูตุ๋นสมุนไพร", 3: "ต้มจืดมะระซี่โครงหมู", 4: "ต้มยำขาหมู", 5: "กระเพาะหมูตุ๋นพริกไทยดำ", 6: "ไข่พะโล้", 7: "ต้มแซ่บกระดูกอ่อน", 8: "ต้มเค็มฟักกับหมูสามชั้น", 9: "หมูต้มใบชะมวง", 10: "ขาหมูต้มผักกาดดอง", 11: "ก๋วยจั๊บน้ำข้น", 12: "ต้มแซ่บกระดูกอ่อน", 13: "ซุปรากบัวซี่โครงหมู", 14: "ซุปมะเขือเทศ", 15: "ไก่ตุ๋นโสมเกาหลี", 16: "ข้าวต้มปลามิโซะ", 17: "ต้มจับฉ่าย", 18: "ปลาเก๋าหนึ่งมะนาว", 19: "ซุปไข่", 20: "เนื้อตุ๋นหม้อดิน"}},
              "อาหารหวาน": {"น้ำ": {1: "ถั่วเขียวต้มน้ำตาล", 2: "ขนอมอินทนิล", 3: "สาคู", 4: "บัวลอย", 5: "ทับทิมกรอบ", 6: "ลาดช่องน้ำกะทิ", 7: "ซ่าหริ่ม", 8: "บิงซูทับทิมกรอบ", 9: "ลูกตาลลอยแก้ว", 10: "ไอศกรีมกะทิ", 11: "สละลอยแก้ว", 12: "เต้าฮวยมะพร้าวอ่อน", 13: "ไอศกรีม ข้าวเหนียวมะม่วง", 14: "ไอศกรีม โอริโอ้", 15: "เฉาก๊วยนมสด คาราเมล"},
                            "แห้ง": {1: "คุกกี้ช็อกโกแลตชิพ", 2: "ขนมโค", 3: "บราวนี่", 4: "แพนเค้ก", 5: "เค้กกล้วยหอม", 6: "ขนมเข่ง", 7: "ขนมงาอ่อนนมสด", 8: "บ้าบิ่น", 9: "Waffle", 10: "ขนมเปี๊ยะ", 11: "บลูเบอร์รี่ครัมเบิล", 12: "ขนมเปียกปูน", 13: "Custard cream ", 14: "ขนมครก", 15: "ขนมกล้วย"}}}

food_Old = {"อาหารคาว": {"แกง": {1: "แกงคั่วหน่อไม้ซี่โครงหมู", 2: "บะกุ๊ดเต๋", 3: "แกงจืดไข่ม้วน", 4: "แกงผักปั๋งใส่แหนม", 5: "ต้มยำขาหมู", 6: "แกงจืดสับปะรด", 7: "แกงจืดฟักซี่โครงหมู", 8: "แกงรัญจวน", 9: "แกงเขียวหวานหมู", 10: "ขนมจีนน้ำเงี้ยว", 11: "แกงคั่วหมูเทโพ", 12: "แกงฮังเล", 13: "แกงขนุนใส่ซี่โครงหมูตุ๋น", 14: "แกงอ่อมหมู", 15: "ซุปรากบัวซี่โครงหมู", 16: "แกงแกงกะทิสายบัวปลาทู", 17: "แกงส้มปลาโจก", 18: "แกงผักหวานป่าใส่ไข่มดแดง", 19: "แกงเหลืองมะละกอกุ้ง", 20: "แกงส้มชะอมไข่"},
                         "ผัด": {1: "ราดหน้า", 2: "หมูกรอบผัดกุนช่าย", 3: "ไข่ผัดเห็ดหอมเต้าหู้อ่อน", 4: "ผัดถั่วงอกเต้าหู้หมูสับ", 5: "หมูสับผัดต้นหอม", 6: "ผัดซีอิ๊ว", 7: "ตับผัดพริกไทยดำ", 8: "ผัดเปรี้ยวหวานหมู", 9: "ตับผัดหน่อไม้ฝรั่ง", 10: "ผัดเต้าหู้หมูสับ", 11: "น้ำพริกปลาร้าทรงเครื่อง", 12: "ปลาแซลม่อนผัดพะโล้", 13: "ผัดสะตอปลา", 14: "น้ำพริกผัดทูน่า", 15: "ปลาช่อนผัดคื่นฉ่าย", 16: "ปลาช่อนจู่ขิง", 17: "ไก่ผัดเม็ดมะม่วงหิมพานต์", 18: "ข้าวผัดอเมริกัน", 19: "กุ้งกระจก", 20: "มะระผัดไข่เค็ม"},
                         "ทอด": {1: "เต้าหู้ไข่ทอดราดซอส", 2: "ไข่ลูกเขย", 3: "ออส่วน", 4: "หอยทอด", 5: "เต้าหู้ทอด", 6: "ยำชะอมทอดกรอบ", 7: "ยอดตำลึงชุปแป้งทอดทรงเครื่อง", 8: "เกี้ยวปูทอด", 9: "ซี่โครงหมูสามรส", 10: "จ๋ายอ", 11: "พะโล้ขาหมู", 12: "น้ำพริกหมูกรอบ", 13: "พริกหยวกทรงเครื่องชุบแป้งทอด", 14: "ล่าเตียง", 15: "ยำปลาดุกฟู", 16: "ปลากระพงทอดน้ำปลา", 17: "ปลาช่อนทอดน้ำปลา", 18: "ปลากระพงทอดคั่วพริกเกลือ", 19: "สะเดาทรงเครื่อง", 20: "เมี่ยงทอดปลาทู"},
                         "ต้ม นึ่ง หรือตุ๋น": {1: "เคาหยก", 2: "หัวปลาหม้อดิน", 3: "ปลากระพงนึ่งซีอิ๊ว", 4: "ไก่แป๊ะซะ", 5: "ไข่ตุ๋น", 6: "ไก่แช่เหล้า", 7: "นึ่งไก่อีสาน", 8: "ซาลาเปา", 9: "", 10: "ก๋วยเตี๋ยวหลอดกุ้ง", 11: "ปากหม้อญวน", 12: "บ๊ะจ่าง", 13: "หมูยอ", 14: "ข้าวเกรียบปากหม้อ", 15: "ปลาดอลลี่นึ่งมะนาว", 16: "บั๋นจึง", 17: "ห่อหมกมะพร้าวอ่อน", 18: "หมกปลาซิว", 19: "ข้าวมันไก่สิงคโปร์", 20: "กุ้งนึ่งกระเทียมโทน"}},
            "อาหารหวาน": {"น้ำ": {1: "เต้าฮวยนมสด", 2: "แกงบวดมันม่วง", 3: "แกงบวดมันม่วง", 4: "แกงบวดฟักทอง", 5: "บัวลอยแก้ว", 6: "เต้าฮวยน้ำขิง", 7: "ทับทิมกรอบ", 8: "บัวลอยน้ำขิง", 9: "ใบเตยสังขยา", 10: "บัวลอยมันส้ม", 11: "เต่าส่วน", 12: "มันเทศต้มขิง", 13: "ไอติม sorbet อะโวคาโดนมอัลมอนด์", 14: "เงาะลอยแก้ว", 15: "ลอดช่องน้ำกะทิ"},
                          "แห้ง": {1: "ขนมถั่วทอง", 2: "ทองเอก", 3: "ขนมเผือกกวน", 4: "ขนมศิลาอ่อน", 5: "ตะโก้เผือก", 6: "ขขนมถ้วย", 7: "ข้าวเหนียวสังขยา", 8: "ขนมตาล", 9: "ข้าวต้มมัด", 10: "ฟักทองสังขยา", 11: "ขนมกล้วย", 12: "ขนมหัวมันหน้ากะทิ", 13: "ผลไม้", 14: "กล้วยทอด", 15: "แพนเค้กหน้าไข่"}}}

def RandKawpro(typefoodkaw):
    def Back():
        w10.destroy()
        w10.quit()
        gc.collect()
        RandKawform()
      
    #w10=หน้าสุ่มของคาว  
    w10 = tk.Tk()
    w10.title("minx")
    w10.geometry(f'600x650+{w10.winfo_screenwidth()//2-(600//2)}+{w10.winfo_screenheight()//2-(650//2)}')
    w10.resizable(0, 0)
    w10.configure(background='white')

    frame2=tk.Frame(w10
                    ,bg='white')
    frame2.place(width='1500',height='1000')

    frame1 = tk.Frame(w10,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w10,bg='#33A1C9')
    frame.place(width='1500', height='150')
    image1=Image.open('ภาพ/bgforforrandom.png')
    my_img=ImageTk.PhotoImage(image1, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    name = name1.get()
    label1 = tk.Label(master=w10,font=('Luckiest Guy', 20),text='Meat Dish',
                   fg='white', bg='#33A1C9').pack(pady=(30,5))
    label2 = tk.Label(
        master=w10,font=('Mali Regular', 15),text="อาหารคาว", fg='white', bg='#33A1C9').pack(pady=5)

    name = name1.get()
    age = selectage(name)
    lbfrk=tk.Label(master=w10,bg='white',fg='black',font=('Mali Regular',25),text='')
    lbfrk.pack(pady=(100,50))
    def process():
        if age >= 5 and age <= 13:
            x = random.randint(1, 20)
            foodresult = food_child["อาหารคาว"][typefoodkaw][x]
            lbfrk.configure(text=foodresult)
        elif age >= 14 and age <= 19:
            x = random.randint(1, 20)
            foodresult = food_teen["อาหารคาว"][typefoodkaw][x]
            lbfrk.configure(text=foodresult)
        elif age >= 20 and age <= 60:
            x = random.randint(1, 20)
            foodresult = food_Adult["อาหารคาว"][typefoodkaw][x]
            lbfrk.configure(text=foodresult)
        elif age >= 61:
            x = random.randint(1, 20)
            foodresult = food_Old["อาหารคาว"][typefoodkaw][x]
            lbfrk.configure(text=foodresult)
    
    process()

    btr = tk.Button(master=w10, text="สุ่มใหม่", fg='white', bg='#33A1C9',highlightbackground='#33A1C9', font=(
        'Mali Regular', 14), command=process).pack(pady=(30,15))
    btk = tk.Button(master=w10, text="Back", fg='white', bg='#33A1C9',highlightbackground='#33A1C9', font=(
        'Luckiest Guy', 14), command=Back).pack(pady=5)
    
    w10.mainloop()

def RandKawform():
    def Back():
        w9.destroy()
        w9.quit()
        gc.collect()
        Random_food()

    def RandKawf(typefoodkaw):
        w9.destroy()
        w9.quit()
        gc.collect()
        RandKawpro(typefoodkaw)

    #w9=หน้าเลือกชนิดของคาว
    w9 = tk.Tk()
    w9.title("minx")
    w9.geometry(f'600x650+{w9.winfo_screenwidth()//2-(600//2)}+{w9.winfo_screenheight()//2-(650//2)}')
    w9.resizable(0, 0)
    w9.configure(background='white')

    frame2=tk.Frame(w9,bg='white')
    frame2.place(width='1500',height='1000')
    frame1 = tk.Frame(w9,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w9,bg='#33A1C9')
    frame.place(width='1500', height='150')

    
    image=Image.open('ภาพ/bgfood5.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    labeli=tk.Label(frame2, image=my_img).place(x=0,y=0)
    
    label1 = tk.Label(master=w9,font=('Luckiest Guy', 20),text='Type of food',
                   fg='white', bg='#33A1C9').pack(pady=25)
    label2 = tk.Label(
        master=w9,font=('Mali Regular', 15),text="เลือกประเภทของอาหารที่คุณต้องการ", fg='white', bg='#33A1C9').pack()

    bttk1 = tk.Button(master=w9, text="แกง", fg='white',bd=1, bg='#33A1C9', font=(
        'Mali Regular', 12),width=15,highlightbackground='black', command=lambda: RandKawf("แกง")).pack(pady=(45,10))
    bttk2 = tk.Button(master=w9, text="ผัด",fg='white',bd=1, bg='#33A1C9', font=(
        'Mali Regular', 12),width=15, highlightbackground='black',command=lambda: RandKawf("ผัด")).pack(pady=10)
    bttk3 = tk.Button(master=w9, text="ทอด", fg='white',bd=1,bg='#33A1C9', font=(
        'Mali Regular', 12),width=15,highlightbackground='black',command=lambda: RandKawf("ทอด")).pack(pady=10)
    bttk4 = tk.Button(master=w9, text="ต้ม นึ่ง หรือตุ๋น",bd=1,fg='white', bg='#33A1C9', font=(
        'Mali Regular', 12),width=15,highlightbackground='black',command=lambda: RandKawf("ต้ม นึ่ง หรือตุ๋น")).pack(pady=10)

    btk = tk.Button(master=w9, text="Back", fg='black',highlightbackground='#33A1C9', bg='#33A1C9', font=(
        'Luckiest Guy', 12), command=Back).pack(pady=30)
    
    w9.mainloop()

def RandWanpro(typefoodwan):
    def Back():
        w8.destroy()
        w8.quit()
        gc.collect()
        RandWanform()
      
    #w8=หน้าสุ่มของหวาน  
    w8 = tk.Tk()
    w8.title("minx")
    w8.geometry(f'600x650+{w8.winfo_screenwidth()//2-(600//2)}+{w8.winfo_screenheight()//2-(650//2)}')
    w8.resizable(0, 0)
    w8.configure(background='white')
    frame2=tk.Frame(w8
                    ,bg='white')
    frame2.place(width='1500',height='1000')
    image1=Image.open('ภาพ/bgforforrandom.png')
    my_img=ImageTk.PhotoImage(image1, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    frame1 = tk.Frame(w8,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w8,bg='#33A1C9')
    frame.place(width='1500', height='150')

    label1 = tk.Label(master=w8,font=('Luckiest Guy', 20),text='Dessert',
                   fg='white', bg='#33A1C9').pack(pady=(30,5))
    label2 = tk.Label(
        master=w8,font=('Mali Regular', 15),text="ของหวาน", fg='white', bg='#33A1C9').pack()

    name = name1.get()
    age = selectage(name)
    lbfrw=tk.Label(master=w8,bg='white',fg='black',font=('Mali Regular',25),text='')
    lbfrw.pack(pady=(100,50))
    def process():
        if age >= 5 and age <= 13:
            x = random.randint(1, 15)
            foodresult = food_child["อาหารหวาน"][typefoodwan][x]
            lbfrw.configure(text=foodresult)
        elif age >= 14 and age <= 19:
            x = random.randint(1, 15)
            foodresult = food_teen["อาหารหวาน"][typefoodwan][x]
            lbfrw.configure(text=foodresult)
        elif age >= 20 and age <= 60:
            x = random.randint(1, 15)
            foodresult = food_Adult["อาหารหวาน"][typefoodwan][x]
            lbfrw.configure(text=foodresult)
        elif age >= 61:
            x = random.randint(1, 15)
            foodresult = food_Old["อาหารหวาน"][typefoodwan][x]
            lbfrw.configure(text=foodresult)
            
    process()
    
    btr = tk.Button(master=w8, text="สุ่มใหม่",highlightbackground='#33A1C9', fg='white', bg='#33A1C9', font=(
        'Mali Regular', 14), command=process).pack(pady=(30,15))
    btk = tk.Button(master=w8, text="Back",highlightbackground='#33A1C9', fg='white', bg='#33A1C9', font=(
        'Luckiest Guy', 14), command=Back).pack(pady=5)
    
    w8.mainloop()

def RandWanform():
    def Back():
        w7.destroy()
        w7.quit()
        gc.collect()
        Random_food()
        
    def RandWanf(typefoodwan):
        w7.destroy()
        w7.quit()
        gc.collect()
        RandWanpro(typefoodwan)    
      
    #w7=หน้าเลือกชนิดของหวาน  
    w7 = tk.Tk()
    w7.title("minx")
    w7.geometry(f'600x650+{w7.winfo_screenwidth()//2-(600//2)}+{w7.winfo_screenheight()//2-(650//2)}')
    w7.resizable(0, 0)
    w7.configure(background='white')
    frame2=tk.Frame(w7, bg='white')
    frame2.place(width='1500',height='1000')
    image1=Image.open('ภาพ/bgfood5.png')
    my_img=ImageTk.PhotoImage(image1, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    frame1 = tk.Frame(w7,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w7,bg='#33A1C9')
    frame.place(width='1500', height='150')

    label1 = tk.Label(master=w7,font=('Luckiest Guy', 20),text='Type of food',
                   fg='white', bg='#33A1C9').pack(pady=(30,5))
    label2 = tk.Label(
        master=w7,font=('Mali', 15),text="เลือกประเภทของอาหารที่คุณต้องการ", fg='white', bg='#33A1C9').pack()
    
    bttw1 = tk.Button(master=w7,width=15,text="แบบนำ้", fg='white',highlightbackground='black', bg='#33A1C9',bd=1, font=(
        'Mali', 14), command=lambda: RandWanf("น้ำ")).pack(pady=(150,10))
    bttw2 = tk.Button(master=w7,width=15,text="แบบแห้ง", fg='white',highlightbackground='black', bg='#33A1C9', bd=1,font=(
        'Mali', 14), command=lambda: RandWanf("แห้ง")).pack(pady=10)

    btk = tk.Button(master=w7, text="Back",highlightbackground='#33A1C9', fg='black', bg='#33A1C9', font=(
        'Luckiest Guy', 14), command=Back).pack(pady=25)
    
    w7.mainloop()

def Random_food():
    global select_menu
    def Back():
        global select_menu
        select_menu = 0
        image.close()
        w6.destroy()
        w6.quit()
        gc.collect()
    
    def RandKaw():
        image.close()
        w6.destroy()
        w6.quit()
        gc.collect()
        RandKawform()

    def RandWan():
        image.close()
        w6.destroy()
        w6.quit()
        gc.collect()
        RandWanform()
        
    #w6=หน้าสุ่มอาหาร(เลือกของคาวกับของหวาน)
    w6 = tk.Tk()
    w6.title("random food generator")
    w6.geometry(f'600x650+{w6.winfo_screenwidth()//2-(600//2)}+{w6.winfo_screenheight()//2-(650//2)}')
    w6.resizable(0, 0)
    w6.configure(background='white')

    frame2=tk.Frame(w6,bg='white')
    frame2.place(width='1500',height='1000')
    frame1 = tk.Frame(w6,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w6,bg='#33A1C9')
    frame.place(width='1500', height='150')

    image=Image.open('ภาพ/cowfoodbg.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    
    label1 = tk.Label(master=w6,font=('Luckiest Guy', 20),text='Random food generator',
                   fg='white', bg='#33A1C9').pack(pady=15)
    label2 = tk.Label(master=w6,font=('Neucha', 15),text="let me help you decide what to eat for today !", fg='white', bg='#33A1C9').pack(pady=(5,55))

    btk1 = tk.Button(master=w6, text="อาหารคาว", fg='white', bg='#33A1C9',width=20,font=(
        'Mali Regular', 14), command=RandKaw).pack(pady=(50,10))
    btk2 = tk.Button(master=w6, text="อาหารหวาน", fg='white', bg='#33A1C9',width=20,highlightbackground='black',font=(
        'Mali Regular', 14), command=RandWan).pack()

    btbk=tk.Button(master=w6, text="Back",fg='black',font=('Luckiest Guy', 14), command=Back).pack(pady=35)
    w6.mainloop()
    print("ออกจากหน้าสุ่มอาหาร")

def Calform():
    global select_menu
    def Back():
        global select_menu
        select_menu = 0
        w5.destroy()
        w5.quit()
        gc.collect()
       
    #w5=หน้าแคลอรี่ 
    w5 = tk.Tk()
    w5.title("calories")
    w5.geometry(f'600x650+{w5.winfo_screenwidth()//2-(600//2)}+{w5.winfo_screenheight()//2-(650//2)}')
    w5.resizable(0, 0)
    w5.configure(background='white')
    frame2=tk.Frame(w5,bg='white')
    frame2.place(width='1000',height='1000')
    frame1 = tk.Frame(w5,bg='black')
    frame1.place(width='1500', height='151')
    frame = tk.Frame(w5,bg='#33A1C9')
    frame.place(width='1500', height='150')

    label1 = tk.Label(master=w5,font=('Luckiest Guy', 18),text='How many calories should you eat in a day?',
                   fg='white', bg='#33A1C9').pack(pady=(30,5))
    label2 = tk.Label(
        master=w5,font=('Mali Regular', 13),text="พลังงานแคลอรี่ที่คุณต้องการ", fg='white', bg='#33A1C9').pack()
    
    lbfr1=tk.Label(master=w5,font=('Mali Regular',17),text='แคลอรี่ที่ควรได้รับต่อวัน',fg='black',bg='white').pack(pady=(150,25))
    image=Image.open('ภาพ/newcal1.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    name = name1.get()
    gender, age = selectgender(name), selectage(name)
    if gender == 'หญิง':
        if age >= 4 and age <= 8:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='1400 - 1600 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 9 and age <= 13:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='1600 - 2000 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 14 and age <= 18:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2000 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 19 and age <= 30:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2000 - 2200 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 31 and age <= 50:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2000 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 51:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='1800 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
    elif gender == 'ชาย':
        if age >= 4 and age <= 8:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='1400 - 1600 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 9 and age <= 13:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='1800 - 2200 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 14 and age <= 18:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2400 - 2800 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 19 and age <= 30:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2600 - 2800 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 31 and age <= 50:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2400 - 2600 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
        elif age >= 51:
            lbfr2=tk.Label(master=w5,font=('Mali Regular',12),text='2200 - 2400 กิโลแคลอรี่',fg='black',bg='white').pack(pady=5)
            
    btbk=tk.Button(master=w5, text="Back",fg='black',bg='#33A1C9',font=('Luckiest Guy', 14), highlightbackground='#33A1C9', command=Back).pack(pady=55)
    w5.mainloop()
    print("ออกจากหน้าแคลอรี่")

def forecastform():
    global select_menu
    import datetime
    def backbt():
        global select_menu
        select_menu = 0
        image.close()
        image1.close()
        w4.destroy()
        w4.quit()
        gc.collect()

    #w4=หน้าสภาพอากาศ
    w4 = tk.Tk()
    w4.title("weather forecast")
    w4.geometry(f'600x650+{w4.winfo_screenwidth()//2-(600//2)}+{w4.winfo_screenheight()//2-(650//2)}')
    w4.resizable(0,0)
    w4.configure(background='white')

    frame2=tk.Frame(w4,bg='white')
    frame2.place(width='1500',height='1000')
    frame3=tk.Frame(w4,bg='white')
    frame3.place(width='1500',height='110')    
    date=datetime.datetime.now()
    datetime=tk.Label(w4, text=(date.strftime('%d'))+' '+( date.strftime('%A'))+' '+( date.strftime('%B'))+' '+( date.strftime('%Y')), bg='white', fg='black',font=('Mali',10)).pack(pady=(25,5))
    hour=tk.Label(w4, text=(date.strftime('%H'))+' '+':'+' '+(date.strftime('%M')), bg='white', fg='black',font=('Mali',10)).pack(pady=5)
    gmt=tk.Label(w4, text='(GMT +7)',  bg='white', fg='black',font=('Mali',8)) .pack(pady=5)
    place=tk.Label(w4, text='Bangkok, Thailand',  bg='white', fg='black',font=('Anton-Regular',15)) .pack(pady=5)

    image=Image.open('ภาพ/bgfood5.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    labeli=tk.Label(frame2, image=my_img).place(x=0,y=0)
    
    image1=Image.open('ภาพ/bgfoodblue1.png')
    img1=image1.resize((600, 150))
    my_img1=ImageTk.PhotoImage(img1, master=frame3)
    labeli1=tk.Label(frame3, image=my_img1).place(x=0,y=0)
    api_key='96fe8ff2b8ca014baa63db755b7a6cc2'

    weather_data=requests.get('https://api.openweathermap.org/data/2.5/weather?lat=13.736717&lon=100.523186&appid=96fe8ff2b8ca014baa63db755b7a6cc2')
    x=weather_data.json()
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    #print(" Temperature (in kelvin unit) = " +str(current_temperature) +"\n atmospheric pressure (in hPa unit) = " + str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidity) +"\n description = " + str(weather_description))

    label1=tk.Label(w4, text='temperature',bg='white', fg='black', font=('Mali',10)).pack(pady=5)
    temp_field = tk.Label(w4, text="...", width=0, bg='white',font=("Mali", 35), fg='black')
    temp_field.pack()
    label2=tk.Label(w4, text='Atmosperic Pressure :'+' '+str(current_pressure),bg='white', fg='black', font=('Mali',13)).pack(pady=(5,5))
    label4=tk.Label(w4, text='Humidity :'+' '+str(current_humidity),bg='white', fg='black', font=('Mali',13)).pack(pady=5)
    label5=tk.Label(w4, text='Description :'+' '+str(weather_description),bg='white', fg='black', font=('Mali',13)).pack(pady=5)

    #lable_temp = Label(root, text="...", width=0, bg='white',font=("Mali Regular", 20), fg='black')
    current_temperature=int(current_temperature)-273.15
    current_temperature=int(current_temperature)
    temp_field.configure(text=current_temperature)

    bt1=tk.Button(master=w4, text=' BACK! ',fg='black',highlightbackground='#33A1C9',font=('Luckiest Guy', 14), command=backbt).pack(pady=25)
    w4.mainloop()
    print("ออกจากหน้าสภาพอากาศ")

def bmiform():
    global select_menu
    def backtomenubt():
        global select_menu
        select_menu = 0
        w3.destroy()
        w3.quit()
        gc.collect()
    
    #w3=หน้าBMI
    w3=tk.Tk()
    w3.title("BMI")
    w3.geometry(f'600x650+{w3.winfo_screenwidth()//2-(600//2)}+{w3.winfo_screenheight()//2-(650//2)}')
    w3.resizable(0,0)
    w3.configure(background='white')
 
    frame2=tk.Frame(w3,bg='white')
    frame2.place(width='1000',height='1000')
    frame1=tk.Frame(w3,bg='black')
    frame1.place(width='1500',height='151')
    frame=tk.Frame(w3,bg='#33A1C9')
    frame.place(width='1500',height='150')
    
    image=Image.open('ภาพ/newbmi1.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    label=tk.Label(frame2, image=my_img).place(x=0,y=0)
    
    label1=tk.Label(master=w3,font=('Luckiest Guy',20),text='Body Mass Index : BMI',fg='white',bg='#33A1C9').pack(pady=(20,5))
    label2=tk.Label(master=w3,font=('Mali',10),text='BMI คือ ตัวชี้วัดมาตรฐานเพื่อประเมินสภาวะของร่างกายว่า\nมีความสมดุลของน้ำหนักตัวต่อส่วนสูงอยู่ในเกณฑ์ที่เหมาะสมหรือไม่',fg='white',bg='#33A1C9').pack(pady=5)
    
    name = name1.get()
    height = selectheight(name)
    lbh=tk.Label(master=w3,font=('Chonburi',10),text='ส่วนสูงของคุณ คือ',fg='black',bg='white').pack(pady=(35,5))
    lbh1=tk.Label(master=w3,font=('Mali',7),text=str(height)+' cm',fg='black',bg='white').pack(pady=5)
    
    weight = selectweight(name)
    lbw=tk.Label(master=w3,font=('Chonburi',10),text='น้ำหนักของคุณ คือ',fg='black',bg='white').pack(pady=5)
    lbw1=tk.Label(master=w3,font=('Mali',7),text=str(weight)+' kg',fg='black',bg='white').pack(pady=5)
    
    lbr=tk.Label(master=w3,font=('Chonburi',10),text='BMI ของคุณ คือ',fg='black',bg='white').pack(pady=5)
        
    result = weight/((height/100)**2)
    lbr1=tk.Label(master=w3,font=('Mali',7),text='{:.2f}'.format(result),fg='black',bg='white').pack(pady=15)
    if result >= 30:
        lbr2=tk.Label(master=w3,font=('Mali Regular',9),text="คุณอ้วนมาก ค่อนข้างอันตราย\nเสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน \nต้องปรับพฤติกรรมการทานอาหาร และควรเริ่มออกกำลังกาย \nและหากค่า BMI ยิ่งสูงกว่า 40.0 ยิ่งแสดงถึงความอ้วนที่มากขึ้น \nควรไปตรวจสุขภาพ และปรึกษาแพทย์"
                   .format(result),fg='black', bg='white').pack()
    elif (result >= 25.0) and (result <= 29.9):
        lbr2=tk.Label(master=w3,font=('Mali Regular',9),text="คุณอ้วนในระดับหนึ่ง ถึงแม้ว่าจะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมากๆ\nแต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน \nทั้งโรคเบาหวาน และความดันโลหิตสูง \nควรปรับพฤติกรรมการทานอาหาร ออกกำลังกาย และตรวจสุขภาพ"
                   .format(result),fg='black', bg='white').pack()
    elif (result >= 18.6) and (result <= 24.0):
        lbr2=tk.Label(master=w3,font=('Mali Regular',9),text="คุณน้ำหนักปกติ จัดอยู่ในเกณฑ์ปกติ \nห่างไกลโรคที่เกิดจากความอ้วน \nและมีความเสี่ยงต่อการเกิดโรคต่างๆ น้อยที่สุด \nควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับยี้ให้นานที่สุด \nและควรตรวจสุขภาพทุกปี"
                   .format(result),fg='black', bg='white').pack()
    else:
        lbr2=tk.Label(master=w3,font=('Mali Regular',9),text="คุณผอมเกินไป น้ำหนักน้อยกว่าคนปกติ \nอาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ \nส่งผลให้ร่างกายอ่อนเพลียง่าย การรับประทานอาหารให้เพียงพอ \nและออกกำลังกายเพื่อเสริมสร้างกล้ามเนื้อ\nสามารถช่วยเพิ่มค่า BMI ให้อยู่ในเกณฑ์ปกติได้"
                   .format(result),fg='black', bg='white').pack()
    
    btok=tk.Button(master=w3, text="OK!",fg='black',highlightbackground='#33A1C9',font=('Luckiest Guy', 14), command=backtomenubt).pack(pady=20)
    w3.mainloop()
    print("ออกจากหน้าBMI")

def menuform():
    global select_menu
    def bmiwindow():
        global select_menu
        select_menu = 1
        image.close()
        w2.destroy()
        w2.quit()
        gc.collect()
    def forecastwindow():
        global select_menu
        select_menu = 2
        image.close()
        w2.destroy()
        w2.quit()
        gc.collect()
    def randomfoodwindow():
        global select_menu
        select_menu = 3
        image.close()
        w2.destroy()
        w2.quit()
        gc.collect()
    def calwindow():
        global select_menu
        select_menu = 4
        image.close()
        w2.destroy()
        w2.quit()
        gc.collect()
        
    #w2=หน้าเลือกเมนู
    w2=tk.Tk()
    w2.title('Menu')
    w2.geometry(f'600x650+{w2.winfo_screenwidth()//2-(600//2)}+{w2.winfo_screenheight()//2-(650//2)}')
    w2.resizable(0,0)
    w2.configure(background='white')

    frame2=tk.Frame(w2,bg='white')
    frame2.place(width='1500',height='1000')
    frame1=tk.Frame(w2,bg='black')
    frame1.place(width='1500',height='151')
    frame=tk.Frame(w2,bg='#33A1C9')
    frame.place(width='1500',height='150')

    image=Image.open('ภาพ/bgfood5.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    label=tk.Label(frame2, image=my_img).grid(padx=0,pady=0)
    
    label1=tk.Label(master=w2,font=('Luckiest Guy',30),text='Menu',fg='white',bg='#33A1C9').pack(pady=(15,15))
    label2=tk.Label(master=w2,font=('Neucha',15),text='What do you wanna do today?',fg='white',bg='#33A1C9').pack(pady=(5,5))

    btch1=tk.Button(master=w2,text='ตรวจสอบดัชนีมวลกาย',font=('Mali Regular',10),command=bmiwindow).pack(pady=(45,10))
    btch2=tk.Button(master=w2,text='พยากรณ์อากาศวันนี้',font=('Mali Regular',10),command=forecastwindow).pack(pady=(5,10))
    btch3=tk.Button(master=w2,text='วันนี้กินอะไรดี',font=('Mali Regular',10),command=randomfoodwindow).pack(pady=(5,10))
    btch4=tk.Button(master=w2,text='ปริมาณแคลอรี่ที่ควรได้รับ',font=('Mali Regular',10),command=calwindow).pack(pady=(5,10))
    
    btm=tk.Button(master=w2,text='EXIT!',font=('Luckiest Guy',15),fg='black',highlightbackground='#33A1C9',command=sys.exit).pack(pady=(25))
    w2.mainloop()
    print('ออกจาก w2')
    
def mainwindow():
    def insert(params):
        with sqlite3.connect("userinfo.sqlite") as con:
            sql_cmd = "insert into medal values(?,?,?,?,?)"
            con.execute(sql_cmd, params)
        w1.destroy()
        w1.quit()
        gc.collect()
    
    #w1=หน้ากรอกข้อมูล
    w1=tk.Tk()
    w1.title("minx")
    w1.geometry(f'600x650+{w1.winfo_screenwidth()//2-(600//2)}+{w1.winfo_screenheight()//2-(650//2)}')
    w1.resizable(0,0)
    w1.configure(background='white')

    frame1=tk.Frame(w1,bg='black')
    frame1.place(width='1500',height='151')
    frame=tk.Frame(w1,bg='#33A1C9')
    frame.place(width='1500',height='150')

    label1=tk.Label(master=w1,font=('Luckiest Guy',20),text='Welcome to Minx!',fg='white',bg='#33A1C9').pack(pady=(40,5))
    label2=tk.Label(master=w1,font=('Neucha',15),text="the manager who's gonna help you decide what to eat for each meal",fg='white',bg='#33A1C9').pack(pady=(5,5))
    label3=tk.Label(master=w1,font=('Alegreya Sans SC Regular', 13),text='Name',fg='black',bg='white').pack(pady=(60,5))
    name=tk.StringVar()
    et1=tk.Entry(w1,textvariable=name).pack()
    label4=tk.Label(master=w1,font=('Alegreya Sans SC Regular', 13),text='Age',fg='black',bg='white').pack(pady=(5))
    age=tk.StringVar()
    et2=tk.Entry(w1,textvariable=age).pack()
    label5=tk.Label(master=w1,font=('Alegreya Sans SC Regular', 13),text='Gender',fg='black',bg='white').pack(pady=(5))
    gender = tk.StringVar()
    gdb1=ttk.Combobox(textvariable=gender)
    gdb1.pack(pady=(5))
    gdb1["values"]=('ชาย','หญิง')
    label6=tk.Label(master=w1,font=('Alegreya Sans SC Regular', 13),text='Height(cm)',fg='black',bg='white').pack(pady=(5))
    height=tk.StringVar()
    et3=tk.Entry(w1,textvariable=height).pack()
    label7=tk.Label(master=w1,font=('Alegreya Sans SC Regular', 13),text='Weight(kg)',fg='black',bg='white').pack(pady=(5))
    weight=tk.StringVar()
    et4=tk.Entry(w1,textvariable=weight).pack()
    
    def insert2():
        Name = name.get()
        Age = int(age.get())
        Gender = gender.get()
        Height = int(height.get())
        Weight = float(weight.get())
        insert((Name,Age,Gender,Height,Weight))
        
    bt1=tk.Button(master=w1, text='  OK!  ',fg='black',highlightbackground='#33A1C9',font=('Luckiest Guy', 14), command=insert2).pack(pady=(25,5))
    w1.mainloop()

def Checknamewindow():
    global count,name1, root
    root=tk.Tk()
    root.title("minx")
    root.geometry(f'600x650+{root.winfo_screenwidth()//2-(600//2)}+{root.winfo_screenheight()//2-(650//2)}')
    root.resizable(0,0)
    root.configure(background='white')

    frame2=tk.Frame(root,bg='white')
    frame2.place(width='1500',height='1000')
    #frame1=tk.Frame(root,bg='black')
    #frame1.place(width='1500',height='151')
    #frame=tk.Frame(root,bg='#33A1C9')
    #frame.place(width='1500',height='50')
    
    image=Image.open('ภาพ/bgfood5.png')
    img=image.resize((600, 650))
    my_img=ImageTk.PhotoImage(img, master=frame2)
    label=tk.Label(frame2, image=my_img).grid(padx=0,pady=0)

    label1=tk.Label(master=root,font=('Luckiest Guy',20),text='Welcome to Minx!',fg='black',bg='white').pack(pady=(35,5))
    label2=tk.Label(master=root,font=('Neucha',15),text="the manager who's gonna help you decide what to eat for each meal",fg='black',bg='white').pack(pady=(5))
    label3=tk.Label(master=root,font=('Alegreya Sans SC Regular', 13),text='Name',fg='black',bg='white').pack(pady=(50, 5))

    name1=tk.StringVar()
    et1=tk.Entry(root,textvariable=name1).pack(pady=5)
        
    def checkname():
        global count
        name = name1.get()
        username = select(name) 
        if username:
            image.close()
            root.destroy()
            root.quit()
            gc.collect()
        else:
            count = 1
            image.close()
            root.destroy()
            root.quit()
            gc.collect()
                        
    bt1=tk.Button(master=root, text='  OK!  ',fg='black',highlightbackground='#33A1C9',font=('Luckiest Guy', 14), command=checkname).pack(pady=35)
    root.mainloop()
    print("ออกจาก root")

select_menu = 0
count = 0
Checknamewindow()
if count == 1:
    mainwindow()

while True:
    if select_menu == 1:
        bmiform()
    elif select_menu == 2:
        forecastform()
    elif select_menu == 3:
        Random_food()
    elif select_menu == 4:
        Calform()
    else:
        menuform()
