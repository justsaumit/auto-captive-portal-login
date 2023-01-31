import time
import subprocess

w_user=subprocess.run(["pass","wifi-user"], capture_output=True).stdout.decode().strip()
w_pass=subprocess.run(["pass","wifi-pass"], capture_output=True).stdout.decode().strip()
cmd = "netstat -nr | sed -n '3p' | awk '{print $2}'"
pipedps=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
gateway=pipedps.communicate()[0].decode().strip()

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.set_capability("acceptInsecureCerts", True)
options.set_capability("assume_untrusted_cert_issuer", True)


driver = webdriver.Firefox(options=options)
driver.get("http://"+gateway)
driver.find_element(by=By.XPATH,value="//*[@id='cpusername']").send_keys(w_user)
driver.find_element(by=By.XPATH,value="//*[@id='cppassword']").send_keys(w_pass)
driver.find_element(by=By.XPATH,value="//*[@id='btnLogin']").click()
time.sleep(9)
if(driver.find_element(by=By.XPATH,value="//*[@id='btnLogout']").is_displayed()):
    print("Logged in successfully!")
elif(driver.find_element(by=By.XPATH,value="/html/body/table/tbody/tr/td/form/input").is_displayed()):
    print("Logged in successfully!")
else:
    print("Login failed")
driver.close()
