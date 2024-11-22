import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import json
import os

# 配置文件路径
goods_file = 'goods.csv'
config_file = 'config.json'

# 检查必要文件是否存在
if not os.path.exists(goods_file):
    raise FileNotFoundError(f"[ERROR] Goods file '{goods_file}' not found. Please create it.")
if not os.path.exists(config_file):
    raise FileNotFoundError(f"[ERROR] Config file '{config_file}' not found. Please create it.")

# 读取药材列表
print("[INFO] Reading goods list from 'goods.csv'...")
goods_df = pd.read_csv(goods_file)
goods = goods_df['goods'].tolist()
print(f"[INFO] Successfully loaded {len(goods)} goods.")

# 从 JSON 文件读取配置
print("[INFO] Reading configuration from 'config.json'...")
with open(config_file, 'r') as f:
    config = json.load(f)

gecko_driver_path = config['gecko_driver_path']
output_dir = config.get('output_dir', 'table')  # 默认为 "table"

# 检查 WebDriver 路径是否正确
if not os.path.exists(gecko_driver_path):
    raise FileNotFoundError(f"[ERROR] WebDriver path '{gecko_driver_path}' not found. Please check your configuration.")

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)
print(f"[INFO] Output directory set to '{output_dir}'.")

# WebDriver 服务配置
service = Service(executable_path=gecko_driver_path)

# 主爬取逻辑
for index, good in enumerate(goods, 1):
    try:
        print(f"\n[INFO] Processing {index}/{len(goods)}: {good}...")
        option = webdriver.ChromeOptions()
        # option.add_argument('headless')  # 如果需要无头浏览器，可以取消注释
        
        # 打开浏览器
        driver = webdriver.Chrome(service=service, options=option)
        driver.maximize_window()
        print(f"[INFO] Navigating to website for '{good}'...")
        driver.get('https://old.tcmsp-e.com/tcmsp.php')
        
        # 执行输入和点击操作
        el1 = driver.find_element(By.XPATH, '//*[@id="inputVarTcm"]').send_keys(good, Keys.ENTER)
        time.sleep(2)
        el2 = driver.find_element(By.XPATH, '//*[@id="grid"]/div[2]/table/tbody/tr/td[3]/a')
        driver.execute_script('arguments[0].click();', el2)
        time.sleep(2)
        
        # 抓取页面数据
        print(f"[INFO] Extracting data for '{good}'...")
        data0 = driver.page_source
        pattern = re.compile(r'^\s*data:.*', re.MULTILINE)
        matches = pattern.findall(data0)
        
        if len(matches) < 2:
            print(f"[WARNING] Data format for '{good}' might be incorrect. Skipping...")
            driver.quit()
            continue
        
        # 转换数据为 DataFrame
        df1 = pd.DataFrame(json.loads(matches[0][22:-1]))
        df2 = pd.DataFrame(json.loads(matches[1][22:-1]))
        print(f"[INFO] Successfully extracted {len(df1)} records for molecules and {len(df2)} for targets.")

        # 保存数据
        df1.to_csv(os.path.join(output_dir, f'mol_{good}.csv'), index=False)
        df2.to_csv(os.path.join(output_dir, f"mol_target_{good}.csv"), index=False)
        print(f"[INFO] Data for '{good}' saved successfully.")
        
    except Exception as e:
        print(f"[ERROR] An error occurred while processing '{good}': {e}")
    finally:
        # 关闭浏览器
        if 'driver' in locals():
            driver.quit()
        print(f"[INFO] Finished processing '{good}'.")