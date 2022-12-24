# Auto-Captive-Portal-Login
A small python script which allows you to automatically login to a captive portal with Selenium using XPath values.


## Pre-Requisites:
[Selenium Webdriver](https://www.selenium.dev/documentation/webdriver/) for Python (install using `pip install selenium` or `pip install -r requirements.txt`)  
[GNU pass](https://www.passwordstore.org/) for storing login-credentials (One can store their credentials in the script as plaintext aswell)  
geckodriver for Firefox in PATH (optional if not already included in selenium webdriver)
([Download link](https://github.com/mozilla/geckodriver/releases)) 

## Brief Look:
[![auto-login](https://draconyan.xyz/pix/auto-login.gif)](https://draconyan.xyz/pix/auto-login.mp4)

## Usage:
```
 $ git clone https://github.com/justsaumit/auto-captive-portal-login
 $ cd auto-captive-portal-login/
```
If not using pass, edit autologin.py.
Replace the values of **w_user** and **w_pass**
When done Save and exit.
```
 $ (text editor/IDE of choice) autologin.py
```

Replace "/path/to/" to the path of the python script(auto-login.py) 
When done Save and exit.
```
$ (text editor/IDE of choice) autologin
```

Make the 'auto-login' shell script executable:
```
 $ chmod +x auto-login
```
Now whenever you wish to login, use `./auto-login`.  

If you want to add the script to your PATH:
For system-wide
```
 $ sudo cp auto-login /usr/local/bin
```
or
For individual user
```
 $ cp auto-login ~/.local/bin
```
And execute it from anywhere as:
```
 $ auto-login
```

## Intentions:
I originally wished to create a shellscript to log into my College wifi-portal just using the terminal.  
I later set up [this makeshift script](https://github.com/justsaumit/.dotfiles/blob/main/.scripts/wifi-captive-login)  
which just finds out the gateway IP and uses st's -e flag that allows st to open the captive-portal in a webbrowser on a new temporary terminal window.  
Issue was I still had to type in my login credentials _everytime_ :/  
With this it is the same except I get to automate it using [gnu pass](https://www.passwordstore.org/)  
and that using XPath(XML Path) to find elements is really convenient.

## Future additions:
Update the script upon reaching college as the Xpath values would differ.  
Make the python-script platform independent  
or just Make a separate shellscript to log in via CLI using curl.
