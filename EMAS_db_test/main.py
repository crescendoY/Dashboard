import random;
import psycopg2;
import schedule;
import json;
import time;
from datetime import datetime;
from PIL import Image, ImageFont, ImageDraw;
import os;


con = psycopg2.connect(
    database="lscm",
    user="lscm",
    password="lscm",
    host="192.168.3.76",
    port='15433'
)


cursor_obj = con.cursor()

def task_1(): 
    # \'{value_1}\'
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'temperature'
    monitoring_location_id = 12
    level = random.randint(1,3)
    if level == 1:
        data = {"temperature": random.uniform(25,28)}
        value_1 = json.dumps(data)
        created_at = datetime.now()
        updated_at = datetime.now()
        sensor_temperature =f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')" 
        cursor_obj.execute(sensor_temperature)
        cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
        result = cursor_obj.fetchall()
        print("Result:","\n",result)
    elif level == 2:
        data = {"temperature": random.uniform(28,31)}
        value_1 = json.dumps(data)
        created_at = datetime.now()
        updated_at = datetime.now()
        sensor_temperature =f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')" 
        cursor_obj.execute(sensor_temperature)
        cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
        result = cursor_obj.fetchall()
        print("Result:","\n",result)
    else:
        data = {"temperature": random.uniform(31,35)}
        value_1 = json.dumps(data)
        created_at = datetime.now()
        updated_at = datetime.now()
        sensor_temperature =f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')" 
        cursor_obj.execute(sensor_temperature)
        cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
        result = cursor_obj.fetchall()
        print("Result:","\n",result)
        
    # data = {"temperature": random.uniform(27,31)}
    # value_1 = json.dumps(data)
    # created_at = datetime.now()
    # updated_at = datetime.now()
    # sensor_temperature =f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')" 
    # cursor_obj.execute(sensor_temperature)
    # cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
    # result = cursor_obj.fetchall()
    # print("Result:","\n",result)
    

def task_2():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'water_level'
    monitoring_location_id = 13
    data = {"water_level": random.uniform(1,7)}
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_water_level = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_water_level)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 13")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)

def task_3():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'turbidity'
    monitoring_location_id = 12
    data = {"turbidity": random.uniform(30,60)}
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_turbidity = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_turbidity)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)

def task_4():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'dissolved_oxygen'
    monitoring_location_id = 12
    data = {"dissolved_oxygen": random.uniform(26,30)}
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_dissolved_oxygen = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_dissolved_oxygen)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 13")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)

def task_5():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'PH'
    monitoring_location_id = 12
    data = {"PH": random.uniform(6,7)}
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_PH = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_PH)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 14")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)

def task_6():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'camera'
    monitoring_location_id = 14
    index = datetime.now().strftime("%Y%m%d-%H%M%S")
    text = f"testing text, 4 birds, \n'{index}'"
    im = Image.new("RGB", (320,320), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 14)
    dr.text((10, 5), text, font=font, fill="#000000")
    #im.show()
    #current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"image_{index}.jpg"
    path = os.path.join(os.getcwd(), "images", file_name)
    im.save(path,'JPEG')
    
    data = {
        "img": "http://192.168.3.3200/images/image%.jpg" %index,
        "cameraId": "camera_1"
        }
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_camera = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_camera)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 14")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)

def task_7():
    device_id = '822c2084-ac20-402b-9272-58acc52ad169'
    monitoring_type = 'bird_detector'
    monitoring_location_id = 15
    index = datetime.now().strftime("%Y%m%d-%H%M%S")
    bird_number = random(1,10)
    text = f"testing text, '{bird_number}' birds, \n'{index}'"
    im = Image.new("RGB", (320,320), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 14)
    dr.text((10, 5), text, font=font, fill="#000000")
    #im.show()
    file_name = f"bird_{index}.jpg"
    path = os.path.join(os.getcwd(), "images", file_name)
    im.save(path,'JPEG')


    data = {
        "img": "http://192.168.3.3200/images/image%.jpg" %index,
        "cameraId": "bird_1",
        "LabelList": [],
        "ObjectList": [],
        "detectionId": "",
        "accuracyList": [],
        "detectionTime": index
        }
    value_1 = json.dumps(data)
    created_at = datetime.now()
    updated_at = datetime.now()
    sensor_bird_detector = f"INSERT INTO sensor_history (device_id, monitoring_type, monitoring_location_id, value, created_at, updated_at) VALUES (\'{device_id}\', \'{monitoring_type}\',\'{monitoring_location_id}\',\'{value_1}\',\'{created_at}\',\'{updated_at}\')"
    cursor_obj.execute(sensor_bird_detector)
    cursor_obj.execute("SELECT VALUE FROM sensor_history WHERE monitoring_location_id = 12")
    result = cursor_obj.fetchall()
    print("Result:","\n",result)


def func() :
    schedule.clear()
    schedule.every(3).seconds.do(task_1)
    schedule.every(10).seconds.do(task_2)
    schedule.every(10).seconds.do(task_3)
    schedule.every(10).seconds.do(task_4)
    schedule.every(10).seconds.do(task_5)
    schedule.every(10).seconds.do(task_6)
    schedule.every(1).to(10).minutes.do(task_7)
    while True:
        schedule.run_pending()

func()