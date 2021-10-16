# 食用说明
1.访问 (http://iyuu.cn/) ，使用微信扫码获取Token的api链接.

![pt](https://github.com/aLuvletter/pt_res/blob/main/images/2021101616404050.png)

2.往下拉动页面复制包含token的api链接.

![pt](https://github.com/aLuvletter/pt_res/blob/main/images/2021101616424205.png)

3.上传项目文件至服务器</br></br>

![pt](https://github.com/aLuvletter/pt_res/blob/main/images/2021101617141426.png)

4.在pt.py文件中把api链接填充进去后保存.
```
api = ''
```
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/2021101617161603.png)

5.在终端处安装requests库
```
python3 -m pip install requests
```
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705181335.png)
6.根据需求选择执行周期，脚本内容根据项目上传路径自行修改:
```
cd /xxxxx/pt
python3 pt.py
```
![pt](https://github.com/aLuvletter/pt_res/blob/main/images/QQ%E6%88%AA%E5%9B%BE20210705181505.png)

<h2>微信推送效果<h2>

![pt](https://github.com/aLuvletter/pt_res/blob/main/images/042D032D23E73FD19B0F818993EF3E91.png)

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

# Updata log
<h2>2021-10-16</h2>

1. 新增爱语飞飞微信通知推送;

2. 删除使用Python项目管理器运行方式
