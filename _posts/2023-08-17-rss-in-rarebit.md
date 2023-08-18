---
title: RSS in Rarebit
---
A widely used webcomic framework online nowadays is [Rarebit](https://rarebit.neocities.org/). (I wouldn't recommend Rarebit as a first option but this page isn't about that.)

One downside of Rarebit is the lack of an RSS feed. As a solution, I have made [a script which can generate a webcomic RSS feed from any Rarebit-using website](/assets/rarebit-rss.js).

To run `rarebit-rss.js`, first make sure you have [NodeJS](https://nodejs.org) installed. Open `rarebit-rss.js` with a text editor and edit the three strings at the beginning to match your comic's URL, title, and a file to output the RSS to.  
Whenever you post a new page, update it as normal, making sure the page is present on the live version of your website, then run the command `node rarebit-rss.js`. This will generate the RSS feed file, which you can then upload to your website.  
It works like this because I made it for my friend who didn't have a local copy of their website, so we have to get the data from the live version.
