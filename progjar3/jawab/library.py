import logging
import requests
import os
import time
import datetime


def get_url_list():
    urls = dict()
    urls['suzy']='https://asset-a.grid.id/crop/0x0:0x0/945x630/photo/2021/05/04/cover-foto-bae-suzy-cr-instagra-20210504065517.jpg'
    urls['naruto']='http://2.bp.blogspot.com/-BBr9_JumuTY/UMwx0J5OQwI/AAAAAAAAAdI/Yo4UY2MiQkE/s1600/animasi-naruto-gif.gif'
    urls['jihyo']='https://cdn.idntimes.com/content-images/community/2019/12/c015051e080acf9b7db402ccfa97cc011-d9be772ef78e358209975d786cd3c417_600x400.jpg'
    urls['video1']='https://filesamples.com/samples/video/mov/sample_960x540.mov'
    urls['video2']='https://filesamples.com/samples/video/mov/sample_640x360.mov'
    return urls


def download_gambar(url=None,tuliskefile=False):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/gif']='gif'
    tipe['image/jpeg']='jpg'
    tipe['application/zip']='jpg'
    tipe['video/quicktime']='mov'
    time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{namafile}.{ekstensi}","wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"writing {namafile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False

if __name__=='__main__':
    #check fungsi
    k = download_gambar('https://asset-a.grid.id/crop/0x0:0x0/945x630/photo/2021/05/04/cover-foto-bae-suzy-cr-instagra-20210504065517.jpg')
    print(k)