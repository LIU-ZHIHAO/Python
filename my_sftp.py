import paramiko
import os
#SFTP 上传下载脚本
#https://github.com/lzhtls/Python/edit/master/my_sftp.py
def sftp_upload(host,port,username,password,local,remote):
    '''完成文件上传功能'''
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    
    os.chdir(local)             #切换到本地目录
    files = os.listdir(local)   #轮询目录中的文件
    for f in files:
        sftp.put(os.path.join(local,f),os.path.join(remote,f))  #上传文件                              #上传文件
    sf.close()

        
def sftp_download(host,port,username,password,local,remote):
    '''完成文件下载功能'''
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    
    files = sftp.listdir(remote)
    for f in files:
        sftp.get(os.path.join(local,f),os.path.join(remote,f))  #下载文件
    sf.close()

if __name__ == '__main__':
    host = '192.168.1.150'  #主机
    port = 22               #端口
    username = 'lzh'        #用户名
    password = 'ts123456'   #密码
    local = 'E:\\upahccb'                                   #本地目录
    remote = '/'                                            #远程目录
    sftp_upload(host,port,username,password,local,remote)   #上传
    #sftp_download(host,port,username,password,local,remote)#下载
