# 网络药理学—基于网络爬虫获取复方中药活性小分子及其对应靶点

## 概述
在中药复方的网络药理学分析中，第一步就是获取复方中药活性小分子及其对应靶点，常规做法是在TCMSP搜索相关中药，再根据（OB>30，DL>0.18）筛选出符合条件的小分子，再获取对应的小分子靶点。本软件基于
https://cloud.tencent.com/developer/article/2466039 中的源代码，提供了筛选和整合靶点的实用工具。

## 文件说明
当前项目的文件结构如下：
```
├── README.md        # 项目的说明文档，包含使用方法和详细信息
├── codes/           # 原始代码和相关资源
├── macOS/           # macOS 平台的可执行文件及相关资源
├── win/             # Windows 平台的可执行文件及相关资源
```
1. README.md

    README.md 是项目的主要说明文档，内容包括：
    - 项目的功能概述。
    - 文件结构说明。
    - 配置文件（config.json）和输入文件（goods.csv）的格式要求。
    - 软件运行步骤。
    - 输出结果说明。
    - 常见问题和解决方案。

2. codes/

    codes/ 文件夹包含项目的源代码和脚本资源，主要用于开发或调试需求。
    **注意：如果您只需要运行软件，不需要直接使用 codes/ 文件夹内容。如果您是开发者，可以基于这些代码扩展内容。**

3. macOS/

    macOS/文件夹包含专为 macOS 平台打包的可执行文件。mac用户使用该文件夹下的文件。

4. win/

    win/文件夹包含专为 windows 平台打包的可执行文件。windows用户使用该文件夹下的文件。
## 使用说明
### MacOS
1. 下载仓库：
`git clone https://github.com/Shiqi-Wu/TCM-NetMiner`

2. 下载操作系统（macOS/win）对应的chrome浏览器和chromedriver，下载地址可以在以下地址获取：https://googlechromelabs.github.io/chrome-for-testing/
    
    注意， chrome浏览器和chromedriver的版本号需要一致，例如，我们安装了
    `https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/mac-x64/chrome-mac-x64.zip`
    文件对应的chrome浏览器，这里的版本号就是`131.0.6778.85`,则需要下载对应版本的chromedriver，也就是 `https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/mac-x64/chromedriver-mac-x64.zip`

### Windows
1. 下载仓库：
`git clone https://github.com/Shiqi-Wu/TCM-NetMiner`

2. 下载操作系统（macOS/win）对应的chrome浏览器和chromedriver，下载地址可以在以下地址获取：https://googlechromelabs.github.io/chrome-for-testing/
    
    注意， chrome浏览器和chromedriver的版本号需要一致，例如，我们安装了
    `https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chrome-win64.zip`
    文件对应的chrome浏览器，这里的版本号就是`131.0.6778.85`,则需要下载对应版本的chromedriver，也就是`https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chromedriver-win64.zip`