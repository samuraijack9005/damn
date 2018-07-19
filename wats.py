from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://web.whatsapp.com/")
name = input("enter the user:")
msg=input("enter the message")
