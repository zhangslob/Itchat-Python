import requests
print('你好，我是一枚萌萌哒的机器人！')
while 1:
    s=input()
    resp=requests.get("http://api.qingyunke.com/api.php",{
        'key':'free',
        'appid':0,
        'msg':s
    })
    resp.encoding='utf-8'
    resp=resp.json()
    print(resp['content'])
