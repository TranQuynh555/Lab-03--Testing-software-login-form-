from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///D:/2025/thang8/nhap_mon_cong_nghe_phan_mem/lab03/login.html")

driver.find_element(By.ID, "username").send_keys("sv1@ptit.edu.vn")
driver.find_element(By.ID, "password").send_keys("sai_mat_khau")
driver.find_element(By.ID, "btnLogin").click()

time.sleep(1)
msg = driver.find_element(By.ID, "msg-error").text
print("Thông báo lỗi:", msg)

# Đường dẫn tuyệt đối
screenshot_path = r"D:\2025\thang8\nhap_mon_cong_nghe_phan_mem\lab03\login_fail.png"
driver.save_screenshot(screenshot_path)
print("Đã chụp màn hình:", screenshot_path)

driver.quit()
