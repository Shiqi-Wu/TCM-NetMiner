# 网络药理学—基于网络爬虫获取复方中药活性小分子及其对应靶点

## 概述
在中药复方的网络药理学分析中，第一步就是获取复方中药活性小分子及其对应靶点，常规做法是在TCMSP搜索相关中药，再根据（OB>30，DL>0.18）筛选出符合条件的小分子，再获取对应的小分子靶点。本软件基于
https://cloud.tencent.com/developer/article/2466039 中的源代码进行修改，提供了筛选和整合靶点的实用工具。

## 文件说明
当前项目的文件结构如下：
```
├── README.md        # 项目的说明文档，包含使用方法和详细信息
├── codes/           # 原始代码和相关资源
├── macOS/           # macOS 平台的可执行文件及相关资源
├── win/             # Windows 平台的可执行文件及相关资源
```
1. README.md
## 使用说明
### MacOS
1. 下载仓库：
`git clone`

2. 下载操作系统（macOS/win）对应的chrome浏览器和chromedriver，下载地址可以在以下地址获取：https://googlechromelabs.github.io/chrome-for-testing/
    
    注意， chrome浏览器和chromedriver的版本号需要一致，例如，我们安装了
    `https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chrome-win64.zip`
    文件对应的chrome浏览器，这里的版本号就是`131.0.6778.85`,则需要下载对应版本的chromedriver，也就是

### Windows
1. 下载仓库：
`git clone`

2. 下载操作系统（macOS/win）对应的chrome浏览器和chromedriver，下载地址可以在以下地址获取：https://googlechromelabs.github.io/chrome-for-testing/
    
    注意， chrome浏览器和chromedriver的版本号需要一致，例如，我们安装了
    `https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.85/win64/chrome-win64.zip`
    文件对应的chrome浏览器，这里的版本号就是`131.0.6778.85`,则需要下载对应版本的chromedriver，也就是