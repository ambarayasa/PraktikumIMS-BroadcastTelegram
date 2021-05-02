import requests

bot_token = '1774614643:AAGGeQwUvAFVp0pw4MdEKkLPHloXeob3RBA'

list_grup = ['-574259627', '-527872359', '-547237717', '621037038',]

bot_message = ("ini broadcast")

def bc_eng(list_grup, bot_message):
    for grup_id in list_grup:
        bot_msg = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + grup_id + '&parse_mode=MarkdownV2&text=' + bot_message
        resp = requests.get(bot_msg)
        
bc_eng(list_grup, bot_message)

print ("program selesai")