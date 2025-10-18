from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
driver.find_element(By.ID, "btnLogin").click()

time.sleep(1)
print(driver.current_url) # dashboard.html
driver.save_screenshot(r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\login_success.png")
driver.quit()
