#----------------------------------- Built in Modules
import os
import threading
os.environ["KIVY_NO_CONSOLELOG"] = "1"

#----------------------------------- kivy modules
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem
from kivymd.uix.snackbar import Snackbar
from kivy.uix.image import Image
#---------------------------------- Window
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.write()
#---------------------------------- Customised modules
from web.IPAddress import getIPv4
from web.QR import makeQR
from web.app import app

#---------------------------------- UI
from _screen import screen_helper

#_--------------------------------- Global Variables
notChecked = True
notChecked1 = True
_link_F = None
_ip_F = None
_port_F = '5000'
filename = None
keyboardOff = True

#---------------------------------- Screens
class SplashScreen(Screen):
    pass

class InputScreen(Screen):
    def nextPage(self):
        global _ip_F
        global _port_F
        if _ip_F:
            self.manager.current = 'qr'
            temp = makeQR(_ip_F, _port_F)
            global filename
            filename = temp['filename']
            global _link_F
            _link_F = temp['link']
        else:
            Snackbar(text="Select IP Address!").show()

    def port_pressed(self, port):
        global _port_F
        _port_F = port
        self.ids.port_showed.text = 'Port: '+port
        self.ids.nav_drawer_port.set_state("close")

    def ipPressed(self, ip):
        global _ip_F
        _ip_F = ip
        self.ids.ip_showed.text = "IP: "+ip
        self.ids.nav_drawer_ip.set_state("close")

    def refresh_1(self):
        global notChecked
        notChecked = True
        self.ids.mdlist.clear_widgets()
        self._getIP()

    def _getIP(self):
        global notChecked
        if notChecked:
            for ip in getIPv4():
                self.ids.mdlist.add_widget(OneLineListItem(text=ip, font_style='Body1', on_press = lambda x:self.ipPressed(x.text)))
            notChecked = False

    def _portlist(self):
        global notChecked1
        if notChecked1:
            for port_ in ['5000', '5050', '8000', '1234', '8080', '1000']:
                self.ids.port_list.add_widget(OneLineListItem(text=port_, font_style='Body1', on_press = lambda x:self.port_pressed(x.text)))
            notChecked1 = False


class QRScreen(Screen):
    def start(self):
        self.ids.status.text = 'Keyboard Link:'
        global _link_F
        self.ids.QR_link.text = _link_F
        global filename
        self.ids.QR_img.source = filename
        self.ids.run.text = 'Keyboard is Online'
    
    def ex(self):
        global keyboardOff
        if keyboardOff:
            if os.environ.get("WERKZEUG_RUN_MAIN") != 'true':
                board = threading.Thread(target=self.final)
                board.daemon = True
                board.start()
                global filename
                os.remove(filename)
                keyboardOff = False
        else:
            Snackbar(text="Keyboard is Online!").show()
        
    def final(self):
        global _port_F
        #import ctypes
        #cytypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        import sys
        sys.stdout = sys.stderr = open(os.devnull, 'w')
        app.run(host='0.0.0.0', port=_port_F, debug=False)

#--------------------------------------- Screen Manager
sm = ScreenManager()
sm.add_widget(SplashScreen(name='splash'))
sm.add_widget(InputScreen(name='input'))
sm.add_widget(QRScreen(name='qr'))

#---------------------------------------- Main Class
class main(MDApp):
    
    def build(self):
        self.title = '__Keyboard__'
        self.icon = 'web/static/keyboard.png'
        screen = Builder.load_string(screen_helper)
        return screen
    
if __name__ == "__main__":
    main().run()
    