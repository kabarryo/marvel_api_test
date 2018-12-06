import json
import re
import requests
import os
from multiprocessing.pool import Pool
import multiprocessing
import time
import random



with open('hero_dict_n.txt','r') as hero_f:
    hero_list = json.loads(hero_f.read())
no_img = 0
yes_img = 0
imgs_url = {}
for item in hero_list['heros_list']:
    hero_id = item['id']
    img = item['thumbnail']['path']+'.'+item['thumbnail']['extension']
    imgs_url[hero_id] = img

url_l = []
for ids in imgs_url.keys():
    url_l.append(ids+'|'+imgs_url[ids])



def make_dir(_path_name):
    print(f'Try to make dir: {_path_name}  ...',end='')
    if os.path.exists(_path_name):
        #pass
        print('Dir already exists.')
    else:    
        os.makedirs(_path_name)
        print('Success!')




def get_images(idurl):
    #time.sleep(random.choice([0,12,3,0,40,7,5,9]))
    _ids = idurl.split('|')[0]
    _url = idurl.split('|')[1]
    if re.search(r'.*not.*',_url):
        file_name = 'image_not_available.jpg'
        path_name = 'mg/b/40/'
    else:
        file_name = _url[-17:]
        path_name = _url[-25:-17]
    print(f'Hero:{_ids}')
    make_dir(path_name)
        
    #print(f'image fetching.')
    if os.path.exists(path_name+file_name):
        #pass
        print(f'File:{file_name} already exists! Skip...')
    else:
        print(f'Fetching {file_name}.....',end='')
        img_data = requests.get(_url)
        with open(path_name+file_name,'wb') as img_f:
            img_f.write(img_data.content)
        print('Done')
    
    

def main_def(url_l):
    t=time.time()
    pool = Pool(4)     
    pool.map(get_images,url_l)
    pool.close()
    pool.join()
    #print(len(res),'images got!')
    #print(len(res))
    print(str(time.time()-t),'sec spended.')
    


if __name__ == '__main__':
    main_def(url_l)    