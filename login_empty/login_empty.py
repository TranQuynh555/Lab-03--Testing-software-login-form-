from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "btnLogin").click()

time.sleep(1)
msg = driver.find_element(By.ID, "msg-error").text
print("Thông báo cảnh báo:", msg)
driver.save_screenshot(r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\login_empty.png")
driver.quit()
