"""
Copyright © 2024 Shiqi Wu

This work is part of the TCM-NetMiner project, a tool for network pharmacology analysis.
GitHub Repository: https://github.com/Shiqi-Wu/TCM-NetMiner

This project is based on the code from the following article:
https://cloud.tencent.com/developer/article/2466039

Permission is hereby granted to use, modify, and distribute this code for non-commercial purposes, 
provided that proper credit is given to the original author and the derivative work's authors. 
For any inquiries, please contact the repository owner through GitHub.
"""

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