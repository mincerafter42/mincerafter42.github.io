---
tag: Programming
date: 2022-01-15 15:20:53 -0800
---
You may be familiar with [pngthermal](https://encode.su/threads/1725-pngthermal-pseudo-thermal-view-of-PNG-compression-efficiency), the program that generates a heatmap-like representation of a PNG file's compression efficiency.  
I thought it would be fun to try to make a gif version of pngthermal, since I'm an unofficial GIF expert and I made that [GIF library]({{page.previous.url|absolute_url}}) in Python.  
But after making a gifthermal in Python, I realized it was really slow, so I decided to try to learn C to make a faster version; I'd heard C is pretty fast.

I guess I made [gifthermal, a C program]({{'/assets/gifthermal.c'|absolute_url}}) now. Compile it with a C compiler! (warning: probably kinda kludgy)

The colours gifthermal outputs are copied from pngthermal:

|Colour |Meaning|
|:-----:|-------|
|<span style="background-color:#000560;color:#fff">#000560</span>|&lt;1 bit per pixel|
|<span style="background-color:#023D9A;color:#fff">#023D9A</span>|&lt;2 bits/pixel|
|<span style="background-color:#005FD3;color:#fff">#005FD3</span>|&lt;3 bits/pixel|
|<span style="background-color:#0186C0;color:#000">#0186C0</span>|&lt;4 bits/pixel|
|<span style="background-color:#4AB03D;color:#000">#4AB03D</span>|&lt;5 bits/pixel|
|<span style="background-color:#B5D000;color:#000">#B5D000</span>|&lt;6 bits/pixel|
|<span style="background-color:#EBD109;color:#000">#EBD109</span>|&lt;7 bits/pixel|
|<span style="background-color:#FBA70F;color:#000">#FBA70F</span>|&lt;8 bits/pixel|
|<span style="background-color:#E00;color:#fff">#EE0000</span>|&lt;9 bits/pixel|
|<span style="background-color:#D00000;color:#fff">#D00000</span>|&lt;10 bits/pixel|
|<span style="background-color:#B20000;color:#fff">#B20000</span>|&lt;11 bits/pixel|
|<span style="background-color:#950000;color:#fff">#950000</span>|&lt;12 bits/pixel|
|<span style="background-color:#700;color:#fff">#770000</span>|12 bits/pixel (GIF can't have over 12 bits/pixel)|

If a GIF image is interlaced, gifthermal will remove the interlacing, which is what pngthermal does. There's a comment in the source explaining how to make gifthermal keep the interlacing, if desired.

C is super wacky. As someone with mostly experience in JavaScript, I can see a lot of similarities between C and JavaScript. Even some between C and Python, as if Python took the names of some of C's functions.  
C also has things that seem really messy and confusing to me with no experience in C. I feel reminded of when I had just started programming and spent more time debugging code than writing code.

If anyone attempts to make a jpgthermal or such, good luck! Especially with the image formats where the pixels can't neatly be mapped to a number of bits; those sound really challenging.
