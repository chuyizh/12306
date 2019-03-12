from PyQt5.Qt import *
import requests
import base64
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class API(object):
    #验证码地址
    yzmurl='https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand'
    #验证验证码
    yzmcheck='https://kyfw.12306.cn/passport/captcha/captcha-check?'
    #输入账号密码
    login='https://kyfw.12306.cn/passport/web/login'

class APITool(QObject):
    session=requests.session()


    @classmethod
    def download_yzm(cls):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        heards = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
        request=cls.session.get(API.yzmurl,headers=heards,verify=False)
        cls.session.cookies
        jpg_json=request.json()
        image=jpg_json['image']
        imagedata = base64.b64decode(image)
        with open('API/yzm.jpg','wb') as f:
            f.write(imagedata)
        #jpg='data:image/jpg;base64,'+image
        #print(jpg)
        return 'API/yzm.jpg'
    @classmethod
    def check_yzm(cls,yzm):

        data={
            'callback': 'jQuery19107827576139100736_1552354156380',
            'answer': yzm,
            'rand': 'sjrand',
            'login_site': 'E',
        }
        n=cls.session.get(API.yzmcheck,params=data)
        #dic=n.json()
        #return dic['result_code'] == '4'
        #print(n.url)
        print(n.text)
        res='result_code":"(.*?)"'
        x=re.compile(res,re.S).findall(n.text)
        print(x)
        return x[0]=='4'
    @classmethod
    def check_login(cls,account,pwd,yzm):
        data={
        'username': account,
        'password': pwd,
        'appid': 'otn',
        'answer': yzm,
        }
        n=cls.session.post(API.login,data=data)
        dic=n.json()
        print(dic)
        #return dic['result_code'] == '4'
        #print(n.url)
        #print(n.text)
        res='result_code":"(.*?)"'
        #x=re.compile(res,re.S).findall(n.text)
        #print(x)
        #return x[0]=='4'


if __name__ == '__main__':
    APITool.download_yzm()
