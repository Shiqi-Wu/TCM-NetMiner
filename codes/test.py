from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

config_file = 'config.json'

with open(config_file, 'r') as f:
    config = json.load(f)

gecko_driver_path = config['gecko_driver_path']
# 手动指定 ChromeDriver 的路径
# driver_path = r"chromedriver-mac-x64/chromedriver"  # 替换为你的路径
service = Service(gecko_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.baidu.com")
print("Browser launched successfully!")
driver.quit()