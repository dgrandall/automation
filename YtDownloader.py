# -*- coding: utf-8 -*-
"""
python youtube  downloader
"""


# from the needed library import the needed function 
from pytube import YouTube 


#create a function that downloads the file 
def LocalDownload(url):
    #Build the YouTube module's object by supplying the URL as a parameter
    yt = YouTube(
           url, # the url of the video
           use_oauth=False, # set to False if you do not want Pytube to interact with your youtube account
           )
    # alter the object so it now contains the video at the highest resolution 
    yt = yt.streams.get_highest_resolution()
    #to get just an mp3 file use
    #ytObject = ytObject.streams.get_audio_only("inputsneeded")
    # try the download function 
    try: 
        # the fallowing function will download the video
        yt.download(output_path='/home/d/Downloads/VideoDownloader')
        print("Download successful")
    # if it does not work print an error message
    except: 
        print("Error")
        
url = input("paste the url to the Youtube Video: ")

#call the previously created function using the url
LocalDownload(url)
    
        