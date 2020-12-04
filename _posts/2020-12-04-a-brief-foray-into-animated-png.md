---
title: A brief foray into animated PNG
tag: image
date: 2020-12-04 08:37:58 -0800
---
I have done some stuff regarding the APNG format. No, I didn't learn the C language and in fact I didn't do any programming here.

What I did do is make this animated PNG image! (If it's not animating, your browser doesn't support Animated PNG)  
![A rotating view of the text "PNG" above shiny multicolored spheres in a grid with the text "Animated" flashing above](/assets/2020-a.png)  
I attempted to recreate [this image from the main page of the PNG website](http://www.libpng.org/pub/png/img_png/pnglogo--povray-3.7--black826--1600x1200.png), which happens to be also linked to in the Links portion of the sidebar, because they had a snazzy 88x31 button.

The website actually included the source 3D files for that image, but they were for a 3D software called POV-Ray, and there seemed to be no way to import the files into my 3D software of choice, [Blender](https://blender.org). (Still on 2.7 because 2.8 freezes completely on my system)  
Luckily, POV-Ray files are stored as plain text, that is at least somewhat human-readable, so I could at least get colors, sphere sizes, and light positions fairly accurate. The coordinate system was all different so I did a bunch of effective rotating though.

Why look, it's a higher resolution static version of frame 96! (Not a factorial)  
![A static view of the 3D text "Animated PNG" above shiny multicolored spheres in a grid.](/assets/2020-not-a.png)

And [here is the Blender file I made!](/assets/png.blend) (A Blender 2.7 file in Cycles Render mode. To make it render faster you can reduce the Render Samples in the Sampling section of the Render Properties.)
