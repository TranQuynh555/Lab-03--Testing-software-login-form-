from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

link_signup = driver.find_element(By.LINK_TEXT, "SIGN UP")
print("Link SIGN UP hiển thị:", link_signup.is_displayed())
link_signup.click()

time.sleep(1)
print("URL sau khi click:", driver.current_url)
driver.save_screenshot(r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\signup.png")
driver.quit()
