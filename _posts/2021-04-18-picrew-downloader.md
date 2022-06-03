---
title: Picrew Downloader
tag: programming
date: 2021-04-18 18:39:08 -0700
last_modified_at: 2021-04-19 07:15 -0700
---
There exists [an image maker known as Picrew](https://picrew.me), in which one can create images using some premade makers.  
But it's kind of annoying if you want to change a part of the image just slightly and you don't have the tools available to do so.

Luckily for people who agree with that statement, I've made yet another Chromium/Firefox extension! This one just adds two buttons to the bottom left of a picrew image maker: one to download the currently visible image as an [OpenRaster](https://en.wikipedia.org/wiki/OpenRaster) file, and one to download _the entire image maker_ as an OpenRaster file. Attempting to download the entire image maker is very slow on my computer and I can't even open the downloaded entire image makers.

The extension is not very polished; for instance there's no progress indicator other than the large amount of console messages. This extension uses JSZip (not [my first time using JSZip](/2020/11/17/maybe-i-should-improve-the-ui-of-mcjar-font-getter), however this time instead of extracting a jar file I'm compressing an ora file.). The extension took me the entire day to make. Well I wasn't working the entire day, I slept some of the time, but it's surprisingly close to 24 hours since I started.

You can [download the extension](https://github.com/mincerafter42/picrew-downloader/archive/refs/heads/master.zip) here. No installation instructions this time. I'm too lazy to give installation instructions.

Update: An issue has been fixed in which the OpenRaster files were generated with the same filename as the image maker's name, which could contain characters that were invalid in filenames. Now they are instead generated with the unique numeric ID.  
Update: An issue has been fixed with coordinates when downloading current state. Unfortunately I can't tell if it's present when downloading the entire maker because I can't test that. If anyone knows whether OpenRaster coordinates are relative to the entire image or relative to the stack, please let me know.  
Update: The extension is now hosted on [its own repository](https://github.com/mincerafter42/picrew-downloader). No more updates on this page.
