---
title: Digital Creations
layout: default
last_modified_at: 2022-08-10
---
# Digital Stuff I've Made
{:.no_toc}
I've made some cool stuff digitally. Here I've tried to collect it all into an easy-to-read page.

This list may be incomplete. If there's a cool thing I did that I forgot about, [let me know](/contact) I guess.

* toc
{:toc}

## Standalone programs
### Janky kludges you shouldn't use
- A [triangle solver](/2021/02/18/triangle-solver) which doesn't work
- [No Setup Syndication](https://github.com/mincerafter42/no-setup-syndication), an RSS feed reader browser extension (**Do not use this!** It is janky and barely functional. If you want a feed reader without accounts or ads I recommend [QuiteRSS](https://quiterss.org))  
  Released 2021-01-12.  
  Pages from the development of No Setup Syndication:
  {% for post in site.tags.nss %}
  1. <a href="{{post.url}}">{{post.title}}</a> ({{post.date|date:"%F"}}){% endfor %}
  {:reversed="true"}

### Janky kludges you should use
- [The Picrew Downloader Bookmarklets](/picrew-download-bookmarklet/), which download the layered images from Picrew in the OpenRaster format. Released 2022-08-10.
  - This is a remake of [the Picrew Downloader browser extension](https://github.com/mincerafter42/picrew-downloader), released 2021-04-18, but it's better as bookmarklets I decided.
- [make-parent.sh](/assets/make-parent.sh), a shell script for joining the heads of 2 or more e-mail threads. Code of the day 2022-07-20.  
  Fabian was impressed with the amount of `sed` syntax I learned in one day.
- [gifthermal](/2022/01/15/gifthermal.c), a tool to visualize the compression efficiency of GIF images, inspired by pngthermal. Published 2022-01-15.
  - The prequel: A [gif library in Python](/2021/11/04-gif-library-or-whatever)
- I took the Computer Programming class in my high school, and here is the best work I did from there. These are all Python 3 programs from circa 2021-03.
  - A [text adventure game where you play as a dragon meeting a human](/assets/python-for-school/dragon, by vivi.py). The _example_ shown to the class was a game where the player character was a human, and the only two outcomes were a dragon sharing treasure with them or a dragon eating them. I expanded on that.
  - A [sorting algorithm visualizer](/assets/python-for-school/vivi turtle sorting.py). It uses turtle graphics because that was the assignment, but I've added a text display because my laptop can't use Python turtle graphics. I went way overboard on this; the actual assignment was just to display the list before and after sorting.
  - A ["horoscope generator" (random phrase generator)](/assets/python-for-school/horoscope_Viatrix.py). The assignment was to make a random phrase generator with a theme, so I picked horoscopes and just made them super confident in wacky things.
- [The WordPress theme Chroma Park](https://wordpress.org/themes/chroma-park/), a modernized version of [Green Park from 2006](https://cordobo.com/free-wordpress-templates/cordobo-green-park/). Published 2021-01-07.  
  Pages from the development of Chroma Park:
  {% for post in site.tags['Chroma Park'] %}
  1. <a href="{{post.url}}">{{post.title}}</a> ({{post.date|date:"%F"}}){% endfor %}
  {:reversed="true"}
- [McJar Font Getter](https://github.com/mincerafter42/mcjarfontgetter), written in JavaScript, which seemed like a good idea at the time I guess? It turned the font in a Minecraft .jar file into an OTF font. Initial release 2020-07-15.
- I contributed to the Pronoun Dressing Room and PIL Tool on [asteine8.github.io](https://asteine8.github.io/) on 2020-02-28. I have apparently improved since then because my commits make me want to go *what were you thinking, past me*, but uhh the cool part was building on existing code, which I seem to remember being commented well and easy to navigate, so good job asteine8 if my past self's memory is correct.

## Media
- [vintafade.gif](/assets/vintafade.gif) (2021-05-26). it's just a gif of a box of vinta fading, showing what happens to boxes of vinta left near me (the vinta disappears via me eating it all :p )
- I animated [a video about the PNG image format.](/2021/04/12/png). Published 2021-04-12.
  - The prequel: [A brief foray into animated PNG](/2020/12/04/a-brief-foray-into-animated-png) (2020-12-04)
- I was on [a podcast hosted by my friend Maple](https://anchor.fm/maplestrip/episodes/Not-a-Date-at-the-Magic-Comic-Book-Shop-w-Viatrix-emq1ll). I don't remember most of what happened but that's cool. The episode was released 2020-11-20.
- I was the voice of a screaming person in [a 5-hour video](https://youtu.be/F_nL5d9lxJU) filled largely with screaming people (credited as mincerafter42 in the description). Video released 2020-09-03.
- Starting on 2020-04-17, I began making edits of [El Goonish Shive](https://egscomics.com) for humour. I [traced the font the author used](/2021/04/03/legs-font), which was unavailable anywhere. On 2020-10-10 I began uploading [some of the edits to Reddit](https://i.reddit.com/search?q=author:mincerafter42+subreddit:elgoonishshiveedits)
- [The card game mɛkso](/2020/10/24/mekso), a game about maths. Published 2019-11-07.
- I made a YouTube channel on 2017-04-13 and published videos there, but I deleted the channel because I just didn't feel like distributing content on YouTube idk. Most of the content was not very good.
- I made stuff on [Scratch](https://scratch.mit.edu) starting 2016-02-27, but i kinda don't want to make my scratch account public because I was like 12 and way less skilled at programming than I am now.

