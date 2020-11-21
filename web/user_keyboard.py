from pynput.keyboard import Key, Controller
keyboard = Controller()

jsonlist = {
    'ctrl': Key.ctrl,
    'alt' : Key.alt,
    'shift': Key.shift,
}
jsonlist_1 = {
    'caps': Key.caps_lock,
    'scroll': Key.scroll_lock,
    'num': Key.num_lock
}  

special_key = {
    'return': Key.enter,
    'backspace': Key.backspace,
    'tab': Key.tab,
    'space': Key.space,
    'esc': Key.esc,
    'f1': Key.f1,
    'f2': Key.f2,
    'f3': Key.f3,
    'f4': Key.f4,
    'f5': Key.f5,
    'f6': Key.f6,
    'f7': Key.f7,
    'f8': Key.f8,
    'f9': Key.f9,
    'f10': Key.f10,
    'f11': Key.f11,
    'f12': Key.f12,
    'prtscr': Key.print_screen,
    'pause': Key.pause,
    'insert': Key.insert,
    'home': Key.home,
    'page up': Key.page_up,
    'delete': Key.delete,
    'end': Key.end,
    'page down': Key.page_down,
    'up': Key.up,
    'right': Key.right,
    'down': Key.down,
    'left': Key.left,
    'cmd': Key.cmd,
    'menu': Key.menu
}

def press(key=None, hold=None):
    hold1 = []
    hold_release = []
    for i in hold:
        try:
            hold1.append(jsonlist[i])
        except:
            try:
                hold_release.append(jsonlist_1[i])
            except:
                pass
    
    #print("Pressed: "+key)
    #print("Hold: ",end='')
    #print(hold)
    
    for i in hold1:
        #print(i, end="")
        #print(" holded!")
        keyboard.press(i)
    
    for i in hold_release:
        keyboard.press(i)
        keyboard.release(i)

    try:
        keyboard.press(key)
        keyboard.release(key)
    except:
        try:
            keyboard.press(special_key[key])
            keyboard.release(special_key[key])
        except:
            #print(key)
            pass
    
    for i in hold1:
        #print(i, end="")
        #print(" released!")
        keyboard.release(i)

    for i in hold_release:
        keyboard.press(i)
        keyboard.release(i)
