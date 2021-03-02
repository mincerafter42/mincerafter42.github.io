---
title: Pokémon episodes are free to watch on pokemon.com
date: 2021-02-22 17:53:25 -0800
tag: Programming
---
You might know that [watch.pokemon.com](https://watch.pokemon.com) features Pokémon episodes free to watch. To my knowledge these are always the same episodes available on the Pokémon TV app, which I am unable to obtain.

Recently I found where the episodes are stored. It's a third-party server! Meaning downloading these episodes or whatever is not against the pokemon.com terms of service.

The episodes appear to be stored multiple times, once as a whole .mp4 file and once as a set of roughly 10-second clips.
For example, here's the [famous jelly filled donut clip (1077992 bytes)](http://s2.content.video.llnw.net/smedia/4953336d7f544f678a12270b176ea386/Tg/Ab1XJBz96rSq8VYgXILuY99TmePPow7H4Ee9cX45s/pok_tv_s0124_2398-master-en.mpegts/playlist20.ts).
Each episode also has a JSON file linking to several m3u8 files linking to the subtitles or to the 10-second clips or such. They're also available in multiple languages (not the original Japanese strangely enough)

Instead of doing homework, I spent the afternoon cobbling together [a Chromium/Firefox extension to download pokemon.com episodes using the URLs and linking and stuff from the JSON file](/assets/straight up download pokemon episodes (chrome extension).zip). (No I didn't compile it, it's just a .zip file, figure out how to install extension yourself)  
Humorously, it doesn't even need permission to access any subdomain of pokemon.com, because it entirely requests files from llnw.net, which is where all the stuff is stored. I will reiterate that third-party services are explicitly *not covered* by the pokemon.com terms of service, but also I am not a lawyer, it's probably a bad idea to take a random person's legal advice unquestioningly.
