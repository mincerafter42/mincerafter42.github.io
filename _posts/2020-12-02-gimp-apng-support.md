---
title: GIMP APNG support
tag: Programming
date: 2020-12-02 08:47 -0800
---
Things that happened to me:
1. "Gee, I wonder if [GIMP](https://gimp.org) supports the [APNG image format](http://wiki.mozilla.org/APNG_Specification)."
1. "Hmm, there's a plugin to support it."
1. "The GIMP team is actually aware of the plugin and won't add it to core GIMP because it uses a modified verion of the libpng library."
1. "I wonder how GIMP's existing _non_-animated PNG support works."
1. "It uses an _un_-modified version of libpng."
1. "Is it worth it for me to learn the C programming language to see if I can write APNG support for GIMP using unmodified libpng?"
