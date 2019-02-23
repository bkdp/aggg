### aggg
aggg = A股公告

aggg项目，使用python爬取巨潮资讯网站里面沪深股市中某个指定股票的最新公告数据，然后将得到的公告数据以json格式保存到本地，交付后续的逻辑处理数据。

巨潮资讯官网：
http://www.cninfo.com.cn

### 测试环境：
- python3
- 依赖：request、json、re （均为内置模块）

### 如何测试：
- 终端底下直接执行：python3 aggg.py
- json数据默认保存到同级目录下
