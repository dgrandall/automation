# -*- coding: utf-8 -*-
"""
python youtube  downloader
"""
from pytube import Playlist # from the needed library import the needed class (Playlist) 
url = input("paste the url to the Youtube Video: ") # show instructions gather input and store it with url
p = Playlist(url) # create a object which stores the Playlist class using the url variable

for video in p.videos:
        try: 
            # the fallowing function will download the video
            video.streams.get_highest_resolution().download(output_path='/home/d/Downloads/VideoDownloader')
            print('Downloaded: '+p.title)# if successful print which video downloaded
        except: 
            print('Download failed for: '+p.title) # if it does not work print which video failed to download

    
        