from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QPainter,QPen,QColor,QIcon
from PyQt5.QtCore import QTimer, Qt, QTime
import sys

def color_hex(r,g,b):
    str_r = format(r, 'x')
    str_g = format(g, 'x')
    str_b = format(b, 'x')
    str_color = '#'+str_r+str_g+str_b
    return str_color

#程序图标路径
Icon_Path = './1.png'
# 蒂芙尼绿
str_tiffany_green = color_hex(129,216,206)
# 自定义红
str_indiv_red = color_hex(215,50,50)



class TrayModel(QSystemTrayIcon):
    def __init__(self, Window):
        super(TrayModel, self).__init__()
        self.window = Window
        self.init_ui()
        self.show()

    def init_ui(self):
        # 初始化菜单
        self.menu = QMenu()

        self.manage_action = QAction('下班时间设定', self, triggered=self.manage_reminder)
        self.quit_action = QAction('退出应用', self, triggered=self.quit_reminder)

        self.menu.addAction(self.manage_action)
        self.menu.addAction(self.quit_action)

        self.setContextMenu(self.menu)

        self.setIcon(QIcon(Icon_Path))
        self.icon = self.MessageIcon()

        self.activated.connect(self.app_click)
    #设置时间，功能开发中。。。
    def manage_reminder(self):
        pass
        # self.window.showNormal()
        # self.window.activateWindow()
    #退出程序  
    def quit_reminder(self):
        qApp.quit()

    def app_click(self, reason):
        pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 设置窗口背景色
        self.setStyleSheet(f'background-color:{str_tiffany_green};')
        # 设置窗口透明度
        self.setWindowOpacity(0.85)
        # 设置窗口 置顶，无边框，无状态栏 
        self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.FramelessWindowHint|Qt.Tool)
        # 设置窗口大小和位置
        #self.setGeometry(850, 450)


        # 创建文字标签
        self.label_txt = QLabel(self)
        # 设置标签属性 background-color: {str_tiffany_green};
        self.label_txt.setStyleSheet(f"  color: white; font-size: 30px; font-weight: bold; font-family: 黑体;")
        # 设置标签居中
        self.label_txt.setAlignment(Qt.AlignCenter)
        # 设置标签大小 这里同窗口大小
        self.label_txt.setFixedSize(200, 50)

        # 创建时间标签
        self.label_time = QLabel(self)
        # 设置标签属性 
        self.label_time.setStyleSheet(f"; color: white; font-size: 15px; font-weight: bold; font-family: 黑体;")
        # 设置标签居中
        self.label_time.setAlignment(Qt.AlignCenter)
        # 设置标签大小 这里同窗口大小
        self.label_time.setFixedSize(200, 15)

        # 设置布局
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_txt)
        layout.addWidget(self.label_time)
        self.setLayout(layout)
        
        # 设置定时器，1s刷新判断时间
        timer = QTimer(self)
        timer.timeout.connect(self.reminder_signin)
        timer.start(1000)


    # 提醒函数
    def reminder_signin(self):
        # 获取当前时间
        current_time = QTime.currentTime()
        time_str = current_time.toString("hh:mm:ss")
        # 获取时分，用于判断
        hour = current_time.hour()
        min = current_time.minute()
        sec = current_time.second()

        if(min == 0):#久坐提醒，显示一分钟
            # if(self.isVisible()): 
            #     pass
            # else:
            self.label_time.setText(time_str)
            self.label_txt.setText("请活动一下")         
            self.setStyleSheet(f'background-color:{str_indiv_red};')
            self.show()

        elif(min == 30):
            if(hour == 17):
                self.label_time.setText(time_str)
                self.label_txt.setText("下班啦 打卡先")
                #移到屏幕中央
                self.setGeometry(850, 450 ,0 ,0)
                self.show()
            
            else:
                self.label_time.setText(time_str)
                self.label_txt.setText("请活动一下")         
                self.setStyleSheet(f'background-color:{str_indiv_red};')
                self.show()

        #不在时间内操作
        else:
            self.label_time.setText(time_str)
            self.label_txt.setText("注意坐姿")
            self.setStyleSheet(f'background-color:{str_tiffany_green};')
            self.show()
            #self.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            new_position = event.globalPos() - self.drag_position
            self.move(new_position)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    #托盘类
    tp = TrayModel(window)
    sys.exit(app.exec_())

