from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

link_forgot = driver.find_element(By.LINK_TEXT, "Forgot password?")
print("Link tồn tại:", link_forgot.is_displayed())
link_forgot.click()

time.sleep(1)
print("URL sau khi click:", driver.current_url)
driver.save_screenshot(r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\forgot_password.png")
driver.quit()
