from optparse import Option
from ssl import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
from fake_useragent import UserAgent
from multiprocessing import Pool
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process,Event
import time
import undetected_chromedriver as uc
import keyboard

#опции
options = webdriver.ChromeOptions()

options.add_argument("--window-size=2560,1440")
options = uc.ChromeOptions()

#запуск драйвера 
driver = uc.Chrome(options=options, use_subprocess=True)
driver.set_window_size(2560, 1440)

#driver.get('https://temp.cab/ru')
#EMAIL=driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div[1]/div[1]/button")


def selen():
    driver.get('https://getnada.com/')
    time.sleep(1)
    first_tab_handle=driver.current_window_handle
    time.sleep(1)
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/div/div[1]/div/div/p/span[1]/a/button").click()
    time.sleep(1)
    driver.execute_script("window.open('about:blank','tab2');")
    time.sleep(1)
    driver.switch_to.window("tab2")
    time.sleep(2)
    driver.get('https://claim.overline.network?affiliateToken=wQ44w1HYVC1q')
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/div/div[1]/form/input")
    time.sleep(2)
    driver.switch_to.window(first_tab_handle)
    time.sleep(5212)

if __name__ == '__main__':
    for _ in range(15):
        Process(target=selen).start()
        time.sleep(2)
        

       
                
        