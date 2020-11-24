---
title: Alexandru Cosmin reviews Chroma Park
date: 2020-11-04 13:58:05 -0800
tags: [Chroma Park, Programming]
---
News! On Chroma Park!  
[@acosmin](https://profiles.wordpress.org/acosmin) is the reviewer for Chroma Park!  
They said I should escape the custom color CSS, escape my `aria-label` attributes, and escape the URLs in the footer. Seeing a pattern here?  
("Escaping" in this context means "tell WordPress to change the text so it's all OK, because a user or translator could put not-OK text in these places, accidentally or on purpose")  
After doing that, I escaped a bunch more text, just in case.  
I also added a feature for touch screens, and general graphical convenience: In the header menu, any menu item with a sub-menu will have a little triangle next to it. (Specifically, U+25BE, which looks like ▾). A touch-screen user could touch the triangle to open the sub-menu, since touching the link would just take them to that link without opening the sub-menu.  
When a sub-menu is visible, the triangle turns upside-down (specifically, it becomes U+25B4, which looks like ▴). I think that's a neat graphical feature that will also make a website running Chroma Park more usable for touch-screen users.  
The accessibility review is a separate review predicted to take 1-2 months. Chroma Park is going through the accessibility review because I gave it the `accessibility-ready` tag, which means I followed the accessibility-ready guidelines.
