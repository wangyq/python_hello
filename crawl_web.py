#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a crawl demo
"""
__author__ = 'yinqingwang@163.com'
__version__ = '0.10'
__license__ = 'MIT'

import os, urllib2,urllib,re


class  GirlTaoBaoMM(object): 
    def __init__(self,picLocalPath,page_num=50): 
        self.page_num = page_num
        self.picLocalPath = picLocalPath
        self.mmurl= "http://mm.taobao.com/json/request_top_list.htm?type=0&page="
    def  download(self): 
        i = 1
        page_num = self.page_num
        picLocalPath = self.picLocalPath

        temp  ='''<img src="'''
        while i<page_num: 
            url = self.mmurl + str(i) 
            up =  urllib2.urlopen(url) 
            cont = up.read() 
            pa = j = 0
            while True: 
                ahref = '''<a href="http'''
                target = "target"
                pa = cont.find(ahref)
                pt = cont.find(target, pa) 
                if pa == -1:
                    break
                modelurl = cont[pa+len(ahref)-4: pt-2] 
                mup=  urllib2.urlopen(modelurl) 
                mcont = mup.read() 
    
                header = "<img style"
                tail = ".jpg"
                iph = k = 0
                while True: 
                    iph = mcont.find(header) 
                    ipj  =  mcont.find(tail,  iph) 
                    if iph == -1:
                        break      
                    mpic = mcont[iph : ipj + len(tail)] 
                    ips = mpic.find("src") 
                    urlpic =  mpic[ips +len("src ="):]
                    try: 
                        print ">>>downloading : lady_p"+str(i)+"_no_"+str(j)+"_pic_"+str(k)+".jpg......"
                        #urllib.urlretrieve(urlpic,  "lady_p"+str(i)+"_no_"+str(j)+"_pic_"+str(k)+".jpg") 
                        urllib.urlretrieve(urlpic,  os.path.join(picLocalPath,"lady_p"+str(i)+"_no_"+str(j)+"_pic_"+str(k)+".jpg")) 
                    except KeyboardInterrupt: 
                        print "SIGINT, exit..."
                        sys.exit(0) 
                    except: 
                        pass
                    mcont = mcont[ipj+1:]
                    k+=1
                cont = cont[pt+1:]
                j+=1
            i += 1
        print ">>>download completed"



def crawl_tuigirl(storageDir, count = 50):
    tmmurl ="http://www.rouruan.com/models/mdown/"

    i = 3
    while i<count:
        url = tmmurl + str(i)
        up = urllib2.urlopen(url)
        cont = up.read()
        cont = cont.decode('UTF-8')
        reg = r'src="(.uploads.+?\.jpg)" class'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, cont)
        mdnh="""xjt_p4">"""
        mdnt="</h1>"
        mnh = cont.find(mdnh)
        mnt = cont.find(mdnt, mnh)
        mn = cont[mnh:mnt+len(mdnt)]
        md_nh="<h1>"
        md_nt="</h1>"
        m_nh = mn.find(md_nh)
        m_nt = mn.find(md_nt, m_nh)
        m_n = mn[m_nh+len(md_nh):m_nt]
        numreg = r'href="#">TuiGirl.+?(\d+).+?/a'
        numre = re.compile(numreg)
        numlist = re.findall(numre, cont)
        if len(numlist)!=0:
            number = numlist[0]
        else:
            number = 1
        x=0
        for imgurl in imglist:
            #urllib.urlretrieve("http://www.rouruan.com"+imgurl,"F:\\tuigirl\\"+str(number)+"-"+m_n+str(x)+".jpg")
            urllib.urlretrieve("http://www.rouruan.com"+imgurl,os.path.join(storageDir ,str(number)+"-"+m_n+str(x)+".jpg"))
            x+=1
        i +=1


#
#  main():
#
if __name__ == '__main__':
    #crawl_tuigirl("/home/wang/data/pci/tuigirl")
    mm = GirlTaoBaoMM(50,"/home/wang/data/pic/taobaomm")
    mm.download()
    pass
