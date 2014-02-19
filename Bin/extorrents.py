## Author: Dustin Hu
##Date: 13-02-2014
## To fetch Exhentai torrents easily

#Input
#http://exhentai.org/g/674034/0b89885c9f/ Exaple link

import exhentai

strExLink = raw_input("Exlink: ")

exhentai.grabTorrentPage(strExLink)
