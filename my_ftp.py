import os
import sys
import ftplib

HOST = '192.168.1.150'      #FTP服务器地址
HOST_NAME = 'lzh'           #账户名
PASSWORD = 'ts123456'       #密码
DOWNLOAD_FILE = 'D:\\360'   #设置文件下载到本地的目录
filelist = []               #定义存储FTP服务器获取的文件名，以列表的方式存储。
LOG_NAME = 'D:\\360\\log\\log.txt'
try:
    ftp = ftplib.FTP(HOST)
except ftplib.error_perm:
    print('无法连接到FTP服务器：%s'%HOST)
print('#########################################\n 已经连接到FTP服务器：%s \n#########################################'%HOST)

def login():
    
    '''登陆FTP'''
    try:
        ftp.login(HOST_NAME,PASSWORD)
        ftp.set_debuglevel(0)               #调试函数.0：不显示  1：显示  2：显示所有
    except ftplib.error_perm:
        print('登陆失败')
        logout()
        return
    print('\t\t登陆成功 \n#########################################\n')

def savelog():
    
    '''保存FTP服务器上的文件信息（文件名）'''

        
    print('当前登陆FTP的路径为：\n%s '%(ftp.pwd()))
          
    with open(LOG_NAME,'a') as filelog:     #a 代表以追加的方式打开文件，with open...可以不用close文件

        for suml in ftp.nlst():              #把FTP服务器的文件遍历并添加到filelog文件下
        
            filelog.write(suml +'\n')
            
    with open(LOG_NAME,'r') as filelog1:
        
        lines = len (filelog1.readlines()) 
        print('历史下载文件一共%d个，列表如下：\n'%lines)
        filelog1.seek(0)                    #读取文件前把指针指到文件开头
        for tmp in filelog1.readlines():    #打印文件列表
            print('%s'%tmp )
        
def download():
    
    '''下载文件'''
    
    print('\n当前电脑的路径为：%s \n自动切换到保存文件的目录：%s '%(os.getcwd(),DOWNLOAD_FILE))
    os.chdir(DOWNLOAD_FILE)
    print('\n下载的文件成功放在了当前电脑路径：\n %s'%(os.getcwd()))

    with open(LOG_NAME,'r') as filelog2:
        filelog2.seek(0)                    #读取文件前把指针指到文件开头
        for filein in filelog2.readlines():
            file = filein.replace('\n','')  #把换行符‘\n’替换成空  == file = filein.restip('\n')
            ftp.retrbinary('RETR %s'%file,open(file,'wb').write)
            print('文件“%s”下载成功'%file)

def logout():
    
    '''退出登陆FTP'''
    
    ftp.quit()

def main():

    login()
    savelog()
    download()
    logout()
   
if __name__ == '__main__':

    main()

