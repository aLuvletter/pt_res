# 食用说明
<del><h2>使用Python项目管理器部署[Python3.X版本]</h2>
1.上传本项目文件至服务器</br></br>

2.在Python项目管理器中添加项目并配置项目</br>
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705180355.png)
<h2>使用定时任务方式启动</h2>

1.上传本项目文件至服务器</br></br>
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705180447.png)
2.删除pt.py文件中
```
while True:
```
删除最后一行内容
```
time.sleep(43200)
```
3.在终端处安装requests库
```
python3 -m pip install requests
```
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705181335.png)
3.根据需求选择执行周期，脚本内容根据项目上传路径自行修改:
```
cd /xxxxx/pt
python3 pt.py
```
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705181505.png)</del>

# 添加站点及签到方式
在site.json文件中自行根据站点特性以及签到需求选择以下签到方式添加站点</br>
通用签到方式:
```
{
    "site": "站点名称",
    "url": "站点地址",
    "cookie": "站点cookie"
}
```
签到方式1:
```
{
    "site": "站点名称",
    "url": "域名/attendance.php",
    "referer": "域名/index.php",
    "cookie": "站点cookie"
}
```
签到方式例2:
```
{
    "site": "站点名称",
    "url": "域名/signin.php",
    "referer": "域名/index.php",
    "cookie": "站点cookie"
}
```
签到方式3:
```
{
    "site": "站点名称",
    "url": "域名/attendance.php",
    "cookie": "站点cookie"
}
```
签到方式4:
```
{
    "site": "站点名称",
    "url": "域名/sign_in.php",
    "referer": "域名/faq.php",
    "action": "sign_in",
    "cookie": "站点cookie"
}
```
签到方式5:
```
{
    "site": "站点名称",
    "url": "域名/attendance-ajax.php",
    "cookie": "站点cookie"
}
```
<h2>已知站点的签到方式</h2>
通用签到方式站点:KeepFrds、SouLvoice、HDAI、HDBD、PTMSG、HDFANS、CCF、DIC、U2、MTEAM、GPW、HUIJVTT[貌似已关闭站点]</br></br>
签到方式1站点:PTHOME</br></br>
签到方式2站点:HAIDAN</br></br>
签到方式3站点:Lemonhd、HDATMOS、HDZONE、HDTIME、3WMG</br></br>
签到方式4站点:HDAREA</br></br>
签到方式5站点:PterClub</br></br>
