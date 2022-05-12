import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import datetime


def myntra_login():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--user-data-dir=/home/harshitsingh/.config/google-chrome/default')

    # driver = webdriver.Chrome(service=Service(executable_path = "/home/harshitsingh/selenium-project/chromedriver_v95"), options=options)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

    # driver.get("https://www.myntra.com/")
    driver.get("https://www.myntra.com/my/address")

    # mobile_number_textbox = driver.find_element_by_css_selector(".editableTextField[name='mobileNumberPlacholder']")
    # mobile_number_textbox = driver.find_elements_by_class_name('find_elements_by_class_name')
    # mobile_number_textbox = driver.find_elements(by=By.CLASS_NAME, value="submitBottomOption")

    # mob = driver.find_elements(by=By.XPATH, value="//input[@type='tel']")[0]
    # mob.send_keys("mob_number_here")
    
    # driver.find_elements(by=By.CLASS_NAME, value="submitBottomOption")[0].click()
    # time.sleep(35)
    # button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(., "Download bounding boxes")]')))
    # driver.switch_to.frame(driver.find_elements_by_class_name('desktop-userActions'))
    # driver.find_element_by_link_text('Saved Addresses').click()

    # time.sleep(2)
    ##### below for old version
    # name = driver.find_elements(by=By.CLASS_NAME, value='addressAccordian-name')
    addresses = driver.find_elements(by=By.CLASS_NAME, value='addressAccordian-address')

    adds = []
    for add in addresses:
        adds.append(add.text)
        # print(add.text)

    driver.close()
    return adds



def save_add():
    adds = myntra_login()
    # print(adds)
    adds_dict_list = []
    for add in adds:
        temp = add.split('\n')
        rem = ''
        for i in range(2,len(temp)):
            rem += str(temp[i] +' ')
        d = {'name':temp[0], 'type':temp[1], 'address':temp[2]+' '+temp[3]}
        adds_dict_list.append(d)
    dt = str(datetime.datetime.now())[:-7]
    filename = ('address_' + str(dt))
    df = pd.DataFrame(adds_dict_list)
    # print(df)
    df.to_csv(filename, index = False)
    return


save_add()


