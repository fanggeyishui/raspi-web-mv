from django.shortcuts import render
from django.http import HttpResponse
import time
import os


import requests
import re

mvtime=0
#mvflag=false

s = requests.Session()

def login_get_csrf():
    response=s.get(url='https://overleaf.icsr.wiki/login',verify=False).text
    logdata={'email':'guanyi27@zju.edu.cn','password':'nnnnnnn'}
    logdata['_csrf']=re.findall(r'window.csrfToken = "(.*?)"',response)
    result = s.post(url='https://overleaf.icsr.wiki/login', data=logdata,verify=False).text
    print(result)
    #logdata['_csrf']=re.findall(r'window.csrfToken = "(.*?)"',result)
    return logdata['_csrf']
    
def register(email=''):
    #首先要登陆获取cookie
    regdata={}
    regdata['_csrf']=login_get_csrf()
    regdata['email']=email
    regback = s.post(url='https://overleaf.icsr.wiki/admin/register', data=regdata,verify=False).text
    return regback
    


# Create your views here.
def regi(request):
    ifgo=''
    if request.method=='POST':
        email=request.POST.get('email')
        ifgo=register(email=email)
        ifgo=ifgo[:40]+'详细激活地址通过邮箱查看'+'*'*20+'}'
    return render(request, 'regi/index.html',{'ifgo':ifgo})





def test(request):
    #return HttpResponse('n1um')
    global mvtime
    nowtime=time.time()
    if nowtime-mvtime>=5:
         os.system('./cmd.sh&')
         #if mvflag take.sh()
         mvtime=int(nowtime)
   
    #return HttpResponse('n2um')
    #mvdir='/home/pi/Pictures/mvdir'
    url=request.build_absolute_uri()
    if 'mp4' not in url:
         return render(request, 'regi/mp4.html')
    #return HttpResponse('n1um')
    mvdir='/home/pi/Pictures/mvdir'
    mvname=os.listdir(mvdir)
    mvname.sort()
    if len(mvname)>10:
         for i in range(5):
              os.remove(mvdir+'/'+mvname[i])
    #return HttpResponse(mvname[-1])

    mv=[]
    with open(mvdir+'/'+mvname[-1],'rb') as f:
         mv=f.read()
    #    f.write(﻿﻿﻿﻿'aaa')
    return HttpResponse(mv,content_type='video/mpeg4')

    url=request.build_absolute_uri()
    #return HttpResponse(url) 
    header={
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
 'Accept': '''text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8''',
 'Accept-Language': '''zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2''',
 'Accept-Encoding': 'gzip, deflate, br',
 'Connection': 'keep-alive',
 'Upgrade-Insecure-Requests': '0'}

#s.auth = ('user', 'pass')
    s.headers.update(header)
    #arl='http://www.baidu.com'
    if 'https' in url:
        url = url.replace("https","http")
    #if 'hdlsb' in url:
         #url=url.replace("http","https")
    #if 'jpg' in url or 'png' in url:
         
         #a=s.get(url)
         #return HttpResponse(a.content,content_type="image/png")
         #with open('regi/templates/regi/bili.html','wb') as f:
         #f.write(url)

# both 'x-test' and 'x-test2' are sent
    #if 'https' not in url:
         #url=url.replace('http','https')
    if request.method == 'GET':
        a=s.get(url)
    if request.method == 'OPTIONS':
        a=s.options(url)
    
    if 'text/html' in a.headers['Content-Type']:
        b=a.text.replace("https","http")
        return HttpResponse(b,content_type=a.headers['Content-Type'])
    #with open('regi/templates/regi/bili.html','w') as f:
         #f.write(a.text)
    #    f.write(﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿'aaa')
    return HttpResponse(a.content,content_type=a.headers['Content-Type'])
    return render(request, 'regi/bili.html')

