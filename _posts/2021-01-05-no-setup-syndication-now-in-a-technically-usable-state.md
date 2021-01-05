---
title: "No Setup Syndication: Now in a technically usable state"
tag: programming
date: 2021-01-05 15:33:38 -0800
---
A few days ago I decided to try making an RSS feed reader. It is now technically working!

A lot of functionality is not present, such as:
- Removing a feed after you add it
- The options actually doing anything instead of just being some cool inputs
- Looking halfway decent

but the functionality of "add feeds. Click extension to view feed contents" is now available!

I essentially started over with manifest version 2, which magically solved weird problems I had with manifest version 3. Version 2 has more documentation too, since it is essentially compatible with Firefox. Firefox even supports the functions Chromium uses in the `chrome` namespace so at the current time the extension should support both Chrome and Firefox.

I named the extension _No Setup Syndication_. Not only is it accurately describing the goal of the extension, its abbreviation is **NSS**, which looks a lot like RSS.

You are now able to download [the current, very much in development, version of NSS](https://github.com/mincerafter42/no-setup-syndication).
