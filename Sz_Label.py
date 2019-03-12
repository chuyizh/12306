from PyQt5.Qt import *




class SzLabel(QLabel):

    def clear_points(self):
        [child.deleteLater() for child in self.children() if child.inherits('QPushButton')]

    def get_result(self):

        result=','.join(['{},{}'.format(child.x()+10,child.y()-20) for child in self.children() if child.inherits('QPushButton')])
        print(result)
        return result
        #for child in self.children():
        #    if child.inherits('QPushButton'):
        #        print(child.pos())


    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        print(evt.pos())


        #加图片点击样式
        point=QPushButton(self)
        #大小
        point.resize(20,20)
        point.move(evt.pos()-QPoint(10,10))
        #颜色，样式
        point.setStyleSheet('background-color:red;border-radius:10px;')
        point.show()


        point.clicked.connect(lambda _,btn=point:btn.deleteLater())