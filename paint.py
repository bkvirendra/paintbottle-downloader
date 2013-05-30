#!/usr/bin/python

__author__ = "Virendra Rajput (virendra.rajput567@gmail.com)"

import os
import sys
import gc
import urllib
import requests

from progressbar import Bar, ETA, FileTransferSpeed, Percentage, ProgressBar, RotatingMarker

directory = "paintbottlevideos/"

widgets = ['downloading..: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets)

def dlProgress(count, blockSize, totalSize):
    if pbar.maxval is None:
        pbar.maxval = totalSize
        pbar.start()
    pbar.update(min(count*blockSize, totalSize))

def main():
 		print "fetching video list from paintbottle.com.."
        data = requests.get("http://paintbottle.com/videos/straight.json").json
        count = 1
        if not os.path.exists(directory):
            print "paintbottlevideos directory created!"
            os.makedirs(directory)
        for item in data[0].get("videos"):
                if item.get("src"):
                        # download the item
                        if not os.path.isfile("paintbottlevideos/" + item.get("src") + ".mp4"):
                                url = "http://paintbottlevideos.com/" + item.get("src") + ".mp4"
                                print "Started downloading.. item " + str(count) + " of " + str(len(data[0].get("videos")))
                                try:
                                        urllib.urlretrieve(url, "paintbottlevideos/" + url.split("/")[-1], reporthook=dlProgress)
                                except Exception, e:
                                        main()
                                print "Finsished downloading item.. " + str(count)
                                gc.collect()
                        count += 1
        print "Downloading complete..\nEnjoy the show ;)"
        return

if __name__ == '__main__':
        main()
