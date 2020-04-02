import bs4
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import re
def calculate_attendance():
    path="D:\\Whats app script\\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.get("https://www.icloudemserp.com/tpct/")
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input").send_keys("tu3f1718103")
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input").send_keys("He he,you will not get it easily..")
    select = Select(driver.find_element_by_id('selectbrid'))
    select.select_by_visible_text("TEC")

    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/button").click()

    driver.get("https://www.icloudemserp.com/corecampus/student/attendance/subwise_attendace_new.php")
    total = driver.find_element_by_xpath("//*[@id='searchfrom']/table[2]/tbody/tr[13]/td[3]/b").text
    driver.close()
    driver.quit()
    return total

def show_assignment():
    path="D:\\Whats app script\\chromedriver.exe"
    driver=webdriver.Chrome(path)
    driver.get("https://www.icloudemserp.com/tpct/")
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input").send_keys("tu3f1718103")
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input").send_keys("He he,you will not get it easily..")
    select = Select(driver.find_element_by_id('selectbrid'))
    select.select_by_visible_text("TEC")
    driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr[5]/td/table/tbody/tr[2]/td/table/tbody/tr[5]/td/button").click()
    driver.get("https://www.icloudemserp.com/corecampus/student/assignments/myassignments.php")
    return driver

# ass_list = driver.find_elements_by_link_text("View")

# for i in range(0,len(ass_list)):
#     ass_list[i].click()
#     print(driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]").text)
#     # driver.execute_script("window.history.go(-1)")
#     # driver.implicitly_wait(60)
#     driver.back()
#     ass_list = driver.find_elements_by_link_text("View")

# ass_list.click()
# # print(driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td/font/b"))


# try:
#     elem = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td/font/b")
# except NoSuchElementException:  #spelling error making this code not work as expected
#     print('no elemnet')


# driver.forward()
# driver.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td/div/table/tbody/tr[5]/td[2]/ul/li/a").click()
# driver.close()
# driver.quit()
