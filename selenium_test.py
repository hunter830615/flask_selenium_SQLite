from selenium import webdriver
import threading
import random
import os
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

conn   = sqlite3.connect('aishopping.db')
cursor = conn.cursor()
sql    = "PRAGMA table_info(product_clothing)"
cursor.execute(sql)
data   = cursor.fetchall()
if  not data :
    sql = "CREATE TABLE product_clothing ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'product_number' TEXT, 'product_name' TEXT, 'introduce' TEXT, 'price' INT, 'category_1' TEXT, 'category_2' TEXT, 'img_1' TEXT, 'img_2' TEXT)"
    cursor.execute(sql)
    conn.commit()
sql = "PRAGMA table_info(stock)"
cursor.execute(sql)
data = cursor.fetchall()
if  not data :
    sql = "CREATE TABLE stock ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'product_number' TEXT, 'size' TEXT, 'product_name' TEXT, 'price' INT, 'category_1' TEXT, 'category_2' TEXT, 'img_1' TEXT, 'count' TEXT)"
    cursor.execute(sql)
    conn.commit()
def page1():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/MEN/tops/short_graphic_tee")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'M' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\men"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'men'
        c2 = 'jacket'
        i1 = 'static/men/' + product_number + '-1.jpg'
        i2 = 'static/men/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()


def page2():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/MEN/outerwear/uv_outer")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'M' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\men"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'men'
        c2 = 'coat'
        i1 = 'static/men/' + product_number + '-1.jpg'
        i2 = 'static/men/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()

def page3():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/MEN/bottoms/pants")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'M' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\men"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'men'
        c2 = 'pants'
        i1 = 'static/men/' + product_number + '-1.jpg'
        i2 = 'static/men/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page4():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/WOMEN/tops/short_graphic_tee")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'W' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\wom"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'wom'
        c2 = 'jacket'
        i1 = 'static/wom/' + product_number + '-1.jpg'
        i2 = 'static/wom/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page5():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/WOMEN/outerwear/uv_outer")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'W' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\wom"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'wom'
        c2 = 'coat'
        i1 = 'static/wom/' + product_number + '-1.jpg'
        i2 = 'static/wom/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page6():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/WOMEN/bottoms/pants")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'W' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\wom"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'wom'
        c2 = 'pants'
        i1 = 'static/wom/' + product_number + '-1.jpg'
        i2 = 'static/wom/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page7():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/KIDS/tops/short_graphic_tee")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'K' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\kid"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'kid'
        c2 = 'jacket'
        i1 = 'static/kid/' + product_number + '-1.jpg'
        i2 = 'static/kid/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page8():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/KIDS/outerwear/casual_outer")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'K' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\kid"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'kid'
        c2 = 'coat'
        i1 = 'static/kid/' + product_number + '-1.jpg'
        i2 = 'static/kid/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()
    
def page9():
    driver = webdriver.Chrome()
    driver.get("https://www.lativ.com.tw/KIDS/bottoms/pants")
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'pdListModelWrap')))
    data = driver.page_source
    soup = BeautifulSoup(data, 'html.parser')
     
    links = soup.find('td').find_all('li')
    titals = soup.find('td').find_all('div', class_ = 'productname')
    for tital, link in zip(titals, links):
        while True:
            product_number = 'K' + str(random.randint(10000, 99999))
            sql = "SELECT product_number FROM product_clothing WHERE product_number = ?"
            cursor.execute(sql, (product_number,))
            data = cursor.fetchone()
            if data != None:
                continue
            else:
                break
        url = 'https://www.lativ.com.tw' + link.find('a').get('href')
        name = tital.text
        img = link.find('a', class_= "imgd").find('img').get('data-original')
        
        save_folder = r"C:\Users\root\Desktop\static\kid"
        print(name)
        print(img)
        w = requests.get(img)
        with open(os.path.join(save_folder, product_number) + '-1.jpg', 'wb') as obj:
            for x in w:
                obj.write(x)
        driver.get(url)
        driver.implicitly_wait(3)
        data = driver.page_source
        soup = BeautifulSoup(data, 'html.parser')
        price = soup.find('span', class_= "price").text
        img2 = soup.find('div', class_="product_image").find('img').get('src')
        w2 = requests.get(img2)
        with open(os.path.join(save_folder, product_number) + '-2.jpg', 'wb') as obj:
            for x in w2:
                obj.write(x)
        c1 = 'kid'
        c2 = 'pants'
        i1 = 'static/kid/' + product_number + '-1.jpg'
        i2 = 'static/kid/' + product_number + '-2.jpg'
        sql = "INSERT INTO product_clothing (product_number, product_name, introduce, price, category_1, category_2, img_1, img_2) VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(sql, (product_number, name, name, price, c1, c2, i1, i2))
        conn.commit()
        data = [{'id_number':product_number , 'size': 'S' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'M' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'L' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50},
                {'id_number':product_number , 'size': 'XL' , 'name':name , 'price':price, 'category1':c1, 'category2':c2, 'img_url':i1, 'count':50}]
        for item in data:
            sql = "INSERT INTO stock (product_number, size, product_name, price, category_1, category_2, img_1, count) VALUES (?,?,?,?,?,?,?,?)"
            cursor.execute(sql, (item['id_number'], item['size'], item['name'], item['price'], item['category1'], item['category2'], item['img_url'], item['count']))
            conn.commit()
    # conn.close()    
    driver.quit()

page1()
page2()
page3()
page4() 
page5()
page6()
page7()
page8()
page9()
conn.close() 
print('Done')