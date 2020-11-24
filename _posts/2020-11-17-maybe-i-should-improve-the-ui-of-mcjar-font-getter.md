---
title: maybe I should improve the UI of McJar Font Getter
date: 2020-11-17 12:55:59 -0800
tags: Pre-blog Programming
---
You may not know that I made [McJar Font Getter](https://github.com/mincerafter42/mcjarfontgetter). McJar Font Getter extracts the font from a Minecraft JAR file, and turns it into the commonly used OTF format instead of Mojang's proprietary bitmap font format. It uses the [opentype.js](https://github.com/opentypejs/opentype.js), [JSZip](https://github.com/Stuk/jszip), and [UPNG.js](https://github.com/photopea/UPNG.js) libraries.

There's some things about the <abbr title="user interface">UI</abbr> I'd like to improve though:  
* The <abbr title="graphical user interface">GUI</abbr> is incredibly default-settingsy. I have already started testing a new GUI but there's no guarantee I'll finish, just like with a lot of things.
* Recent Minecraft JAR files (and resource packs, the more generalized Minecraft resource container) allow for pretty much as many individual fonts as one would want in one file. However McJar Font Getter always only reads the `minecraft:default` font. An improvement would be allowing the user to choose a font out of the fonts in their file.
* Recent Minecraft JAR files allow for multiple providers in a font. The providers are sources that combine to make the font, and can be in multiple formats. Currently McJar Font Getter uses all the `bitmap` providers in the `minecraft:default` font and ignores all the `legacy_unicode` providers (which are identical to the [GNU Unifont](http://unifoundry.com/unifont/index.html) by default) and the `ttf` providers (which would require lots more coding on my part to appear identical to how this provider displays in Minecraft). An improvement would be allowing the user to choose which providers they want out of their selected font.

I have the capability to work on these. Does that mean I will? Who knows? Maybe I'll get more invested in something else and abandon this entirely! You never know what'll happen with my human brain!
