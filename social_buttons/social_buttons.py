from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

social_buttons = driver.find_elements(By.CSS_SELECTOR, ".social-login a, .social-login button, .fa-facebook, .fa-twitter, .fa-google")
print("Số nút social login tìm thấy:", len(social_buttons))
for btn in social_buttons:
    print("Nút:", btn.get_attribute("outerHTML"))

driver.save_screenshot(r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\social_buttons.png")
driver.quit()
