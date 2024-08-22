import time
import subprocess
import netifaces

w_user=subprocess.run(["pass","wifi-user"], capture_output=True).stdout.decode().strip()
w_pass=subprocess.run(["pass","wifi-pass"], capture_output=True).stdout.decode().strip()
#Using netifaces to get gateway
gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]


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
time.sleep(15)
if(driver.find_element(by=By.XPATH,value="//*[@id='btnLogout']").is_displayed()):
    print("Logged in successfully!")
elif(driver.find_element(by=By.XPATH,value="/html/body/table/tbody/tr/td/form/input").is_displayed()):
    print("Logged in successfully!")
else:
    print("Login failed")
driver.close()
