import pandas as pd
import os
import json

# 配置文件路径
goods_file = 'goods.csv'
config_file = 'config.json'

# 检查必要文件是否存在
if not os.path.exists(goods_file):
    raise FileNotFoundError(f"[ERROR] Goods file '{goods_file}' not found. Please create it.")
if not os.path.exists(config_file):
    raise FileNotFoundError(f"[ERROR] Config file '{config_file}' not found. Please create it.")

# 从 CSV 文件读取药材列表
print("[INFO] Reading goods list from 'goods.csv'...")
goods_df = pd.read_csv(goods_file)
goods = goods_df['goods'].tolist()
print(f"[INFO] Successfully loaded {len(goods)} goods.")

# 从配置文件读取过滤条件
print("[INFO] Reading configuration from 'config.json'...")
with open(config_file, 'r') as f:
    config = json.load(f)

filter_conditions = config.get('filter_conditions', {"ob_threshold": 30, "dl_threshold": 0.18})
ob_threshold = filter_conditions['ob_threshold']
dl_threshold = filter_conditions['dl_threshold']
print(f"[INFO] Using filter conditions: OB >= {ob_threshold}, DL >= {dl_threshold}.")

# 初始化 DataFrame
df3 = pd.DataFrame()
df4 = pd.DataFrame()

# 处理每个药材的数据
for good in goods:
    try:
        print(f"\n[INFO] Processing data for '{good}'...")

        # 读取数据文件
        mol_file = f"table/mol_{good}.csv"
        target_file = f"table/mol_target_{good}.csv"

        if not os.path.exists(mol_file):
            print(f"[WARNING] File '{mol_file}' not found. Skipping '{good}'.")
            continue
        if not os.path.exists(target_file):
            print(f"[WARNING] File '{target_file}' not found. Skipping '{good}'.")
            continue

        df1 = pd.read_csv(mol_file)
        df2 = pd.read_csv(target_file)

        # 筛选符合条件的数据
        df1 = df1[(df1["ob"] >= ob_threshold) & (df1["dl"] >= dl_threshold)]
        drugs = df1['molecule_name'].values.tolist()
        df2 = df2[df2["molecule_name"].isin(drugs)]

        # 添加药材来源列
        df1['drug'] = good
        df2['drug'] = good

        # 合并数据
        df3 = pd.concat([df3, df1], ignore_index=True)
        df4 = pd.concat([df4, df2], ignore_index=True)

        print(f"[INFO] '{good}' processed successfully: {len(df1)} molecules, {len(df2)} targets retained.")

    except Exception as e:
        print(f"[ERROR] An error occurred while processing '{good}': {e}")

# 保存合并后的结果
output_dir = config.get('output_dir', 'table')
os.makedirs(output_dir, exist_ok=True)

df3.to_csv(os.path.join(output_dir, 'molecule.csv'), index=False)
df4.to_csv(os.path.join(output_dir, 'target.csv'), index=False)

print("\n[INFO] Processing complete. Results saved to:")
print(f" - Molecule file: {os.path.join(output_dir, 'molecule.csv')}")
print(f" - Target file: {os.path.join(output_dir, 'target.csv')}")