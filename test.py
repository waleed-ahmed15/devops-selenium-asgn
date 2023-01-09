from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

# PATH = r"C:\Users\waleed\Downloads\chromedriver.exe"
# driver=webdriver.Chrome(PATH)
driver = webdriver.Chrome(options=options)
# driver(options=options)
try:
    print('testing the web app launching the localhost')
    driver.get("http://localhost:3000")
    print("test 1-------login ")

    try:
        password = driver.find_element("xpath" ,'/html/body/div/div/div/form/input')
        password.send_keys("abc")
        loginpress=driver.find_element('xpath','/html/body/div/div/div/form/button')
        loginpress.click()
        # pagetitle=driver.find_element('xpath','/html/body/div/div/div/h1')
        # print(pagetitle)
        print('login test successfull')
    except:
        print("test of login failed")

    print("test 2-----------create task ")
    try:
        inputfortask= driver.find_element("xpath" ,'//*[@id="root"]/div/div/form/input')
        inputfortask.send_keys("task1")
        time.sleep(4)
        create = driver.find_element("xpath" ,'//*[@id="root"]/div/div/form/button')
        create.click()
        time.sleep(2)
        print('create task  test passed')
    except:
        print("create task failed")
    
    print('test 3----------- for delete task ')
        
    try:
        delete = driver.find_element("xpath" ,'//*[@id="root"]/div/div/div[1]/button')
        delete.click()
        try:
            if driver.find_element('xpath','//*[@id="root"]/div/div/div[1]/button').is_displayed():
                print(' delete task test failed')

        except:
            print('delete test passed')

    except:
        print('delete test failed')
    
    print('test 4---------------logout')

    try:
        logoutButton=driver.find_element('xpath','//*[@id="root"]/div/div/button')
        logoutButton.click()
        try:
            loginh=driver.find_element('xpath','/html/body/div/div/div/h1')
            print('logout test passed')

        except:
            print('logout failed')
    except:
        print('logout test failed')


except:
    print('Kindly run the application on local host first')


print("end")
