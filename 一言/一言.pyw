import requests, json, win10toast, pyperclip
html = requests.get('https://v1.hitokoto.cn/').content.decode()
html_dict = json.loads(html)
show_txt = '%s\n -- %s'%(html_dict['hitokoto'],html_dict['from'])
pyperclip.copy(show_txt)
Tn = win10toast.ToastNotifier()
while Tn.notification_active(): sleep(2)
Tn.show_toast('一言', show_txt, duration=10)
