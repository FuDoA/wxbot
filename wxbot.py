from wxpy import *
import time
bot=Bot(console_qr=1, cache_path=True)
bot.enable_puid(path='wxpy_puid.pkl')
tuling = Tuling(api_key='c99836bb85ef4c84a3d12ed70cc21075')
lggroup=bot.groups().search('澳宋荣光长久存')[0]
me=bot.self

now=time.localtime( time.time()) 
'''
lggroup.send_msg(msg=f'现在已经是{now[3]}点{now[4]}分了,这群还没挂')
'''
songjiang = bot.friends().search('朔月')[0]



@bot.register(songjiang)
def reply_my_friend(msg):
    tuling.do_reply(msg)

@bot.register(lggroup)
def reply_lg(msg):
    if msg.is_at==True:
        lggroup.send_msg(msg=f'现在已经是{now[3]}点{now[4]}分了,这群还没挂')
@bot.register(me)
def reply_self(msg):
    '''tuling.do_reply(msg)'''
    me.send_msg(msg=f'现在已经是{now[3]}点{now[4]}分了')
embed()