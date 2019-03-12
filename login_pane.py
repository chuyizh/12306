from PyQt5.Qt import *
from resource.login_ui import Ui_Form
from API.API_Tool import APITool

class LoginPane(QWidget,Ui_Form):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.refresh_yzm()

    def refresh_yzm(self):
        print('刷新验证码')
        url=APITool.download_yzm()
        print(url)
        pixmap=QPixmap(url)
        self.yzm_label.setPixmap(pixmap)




    def auto_dm(self):
        print('自动打码')


    def check_login(self):
        print('验证登录')
        result=self.yzm_label.get_result()
        #x=APITool.check_yzm(result)
        #print(x)
        if len(result)==0:
            print('请填写验证码')
            return None
        if APITool.check_yzm(result):
            print('验证码正确')
            account = self.account_le.text()
            pwd = self.pwd_le.text()
            APITool.check_login(account,pwd,result)

        else:
            print('验证码错误')
            self.yzm_label.clear_points()
            self.refresh_yzm()


    def auto_enable_login_btn(self):
        account=self.account_le.text()
        pwd=self.pwd_le.text()
        if len(account)==0 or len(pwd)==0:
            self.login_btn.setEnabled(False)
        else:
            self.login_btn.setEnabled(True)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    login = LoginPane()
    login.show()

    sys.exit(app.exec_())