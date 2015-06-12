# -*- coding: utf-8 -*-
import os
import sys

root = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(root, 'site-packages'))

import werobot
from werobot.session.saekvstorage import SaeKVDBStorage
session_storage = SaeKVDBStorage()


robot = werobot.WeRoBot(token='xxx',enable_session=True,session_storage=session_storage)
#robot = werobot.WeRoBot(token='gzxyjctoken',enable_session=True,session_storage=saekvstorage.SaeKVDBStorage())

#robot = werobot.WeRoBot(token='gzxyjctoken')

@robot.handler
def hello(message, session):
    count = session.get("count", 0) + 1
    session["count"] = count
    
    #return "Hello! You have sent %s messages to me" % count
    #return "Hello! \nHomePage: \nhttp://gzxyjc.sinaapp.com\nTel : (+86) 139 0855 2003"
    #return TextReply(message=message, content='Any question Please call Tel : (+86) 139 0855 2003')
    return "欢迎垂询凯里祥源建材!\n主页:http://gzxyjc.sinaapp.com\n电话:(+86) 139 0855 2003"

@robot.handler
def echo(message):
    return 'Hello World!'

#robot.run()
