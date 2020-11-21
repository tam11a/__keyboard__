screen_helper = """
<ItemConfirm>
    on_release: root.set_icon(check)

    CheckboxLeftWidget:
        id: check
        group: "check"

ScreenManager:
    SplashScreen:
    InputScreen:
    QRScreen:

<SplashScreen>:
    name: 'splash'
    MDLabel:
        text: '__Keyboard__'
        font_name: 'fonts/Oxanium-Semibold'
        halign: 'center'

    MDFlatButton:
        text: 'Start'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        font_name: 'fonts/Oxanium-Semibold'
        increment_width: '164dp'
        text_color: 1, 1, 1, 1
        md_bg_color: 0, 0, 0, 1
        on_press: root.manager.current = 'input'
        
<InputScreen>:
    name: 'input'
    
    MDFlatButton:
        id: ip_showed
        text: 'Select IP Address *'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        font_name: 'fonts/Oxanium-Semibold'
        increment_width: '164dp'
        text_color: 1, 1, 1, 1
        md_bg_color: 0, 0, 0, 1
        on_press: root._getIP(), nav_drawer_ip.set_state("open")

    MDFlatButton:
        id: port_showed
        text: 'Port: 5000'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        font_name: 'fonts/Oxanium-Semibold'
        increment_width: '164dp'
        text_color: 1, 1, 1, 1
        md_bg_color: 0, 0, 0, 1
        on_press: root._portlist(), nav_drawer_port.set_state("open")

    MDFlatButton:
        text: 'Next'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        font_name: 'fonts/Oxanium-Semibold'
        increment_width: '164dp'
        text_color: 1, 1, 1, 1
        md_bg_color: 0, 0, 0, 1
        on_press: root.nextPage()
    

    MDNavigationDrawer:
        id: nav_drawer_ip
        ScrollView:    
            MDList:
                id: mdlist_0
                OneLineListItem:
                    MDLabel:
                        text: 'Available Connections:'
                        font_name: 'fonts/Oxanium-Semibold'
                        halign: 'center'
                        pos_hint: {'center_y':0.5}
                MDList:
                    id: mdlist
                OneLineListItem:
                    MDFlatButton:
                        text: 'Refresh'
                        pos_hint: {'center_x':0.5,'center_y':0.5}
                        font_name: 'fonts/Oxanium-Semibold'
                        increment_width: '164dp'
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0, 0, 0, 1
                        on_press: root.refresh_1()
    
    
    MDNavigationDrawer:
        id: nav_drawer_port
        ScrollView:    
            MDList:
                OneLineListItem:
                    MDLabel:
                        text: 'Suggested Ports:'
                        font_name: 'fonts/Oxanium-Semibold'
                        halign: 'center'
                        pos_hint: {'center_y':0.5}
                MDList:
                    id: port_list
    
    
<QRScreen>:
    name: 'qr'
    MDLabel:
        id: status
        text: ''
        font_name: 'fonts/Oxanium-Semibold'
        halign: 'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        id: QR_link
        text: ''
        font_name: 'fonts/Oxanium-Semibold'
        halign: 'center'
        pos_hint: {'center_y':0.83}
    Image:
        id: QR_img
        source: ''
        size: self.texture_size 
    MDFlatButton:
        id: run
        text: 'Upload Keyboard'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        font_name: 'fonts/Oxanium-Semibold'
        increment_width: '164dp'
        text_color: 1, 1, 1, 1
        md_bg_color: 0, 0, 0, 1
        on_press: root.start(), root.ex()

"""