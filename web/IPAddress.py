import os
def getIPv4():
    list = []
    try:
        for line in os.popen('ipconfig').read().split('\n'):
            if 'IPv4 Address. . . . . . . . . . . :' in line:
                list.append(line.split('IPv4 Address. . . . . . . . . . . : ')[-1])
    except:
        pass
    return list
