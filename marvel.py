# 哈哈哈模块化


from datetime import datetime
from hashlib import md5
#import sys
__version__ = '0.1'


#pbkey = 'b429b36ad9c859671f28487a8acdca22'
#pvkey = '10486b67a96262c7c4859f963ae11c36d94352e6'

#初始化为空值
pbkey = False
pvkey = False

#定义md5key生成函数

def hashkey():
    #print(pbkey,pvkey)
    if not(pbkey or pvkey) :
        raise Exception("Err : 'pbkey' or 'pvkey' has no value!")
        
    
    ts = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-2]   #timestamp ts
    key = ts + pvkey + pbkey
    _md5key = md5(key.encode('utf-8')).hexdigest()
    return _md5key,ts



