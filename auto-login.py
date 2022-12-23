import time
import subprocess

w_user=subprocess.run(["pass","wifi-user"], capture_output=True).stdout.decode().strip()
w_pass=subprocess.run(["pass","wifi-pass"], capture_output=True).stdout.decode().strip()
cmd = "netstat -nr | sed -n '3p' | awk '{print $2}'"
pipedps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
gateway=pipedps.communicate()[0].decode().strip()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://"+gateway)

driver.find_element(by=By.XPATH,value="//*[@id='tf1_userName']").send_keys(w_user)
driver.find_element(by=By.XPATH,value="//*[@id='tf1_password']").send_keys(w_pass)
driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/div[2]/form/div/div[5]/button").click()
time.sleep(5)
if(driver.find_element(by=By.XPATH,value="//*[@id='lblLoggedinUser']").is_displayed()):
   print("Logged in successfully!")
else:
   print("Login failed")
driver.close()
