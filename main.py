from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(r'E:\Github\Report_Extraction_Automation\chromedriver.exe')
driver.get('https://hosted.reckon.com/RAHV2/ReckonAccountsLogon.aspx')
driver.maximize_window()
time.sleep(5)

username_ = driver.find_element('id','Body_ctrlLogin_txtUsername')
username_.send_keys('bcsdwh')
username_.send_keys(Keys.RETURN)
time.sleep(4)

password_ = driver.find_element('id','Body_ctrlLogin_txtEPassword')
with open(r'E:\Github\Report_Extraction_Automation\password.txt', 'r') as pw:
    password = pw.read()
password_.send_keys(password)
password_.send_keys(Keys.RETURN)
print('You are logged in!')
time.sleep(10)

launch_btn = driver.find_element('id','Body_Launch0')
launch_btn.click()
time.sleep(10)

import sub
sub.Report_Finder('Reports')
time.sleep(10)
sub.Report_Finder('Sales')
time.sleep(10)
sub.Report_Finder('Sales by Item Summary')
time.sleep(10)
sub.Report_Finder('Export')

time.sleep(300)

