---
title: Site Setup
last_modified_at: 2021-09-26
---
This page will describe how you are able to view this very website, assuming you know pretty much nothing about that.

This website is stored as multiple files. Your computer is able to use the files to put the words and other stuff I want on your screen in the right place, unless it isn't. Hopefully it is.  
The files are stored on another computer, called a **server**. Your computer asked the server to send this page to it, and it did. I don't know where the server is. I am sending the files to the server through the service GitHub Pages (through the service GitHub and the program git, but that's less important right now).

Some servers can do cool things like keep a list of followers and send e-mails to them, or let users post comments on the site. GitHub Pages doesn't let me do that with their server.  
However, it does have a tool that allows you to follow the blog, and allows me to only change one file when I want to add stuff to the sidebar or header, instead of changing it in every individual page. That tool is called **static site generation.**

Static site generation means that the server will store every page as its own file with its own header and sidebar and such, but those aren't the files I give it. The files I give it are instructions for the server to put all the parts together on each page. This means I can avoid duplicate parts of the file. When I send new files to the server, it follows all the instructions once then keeps the files it got by following them.

The files that the server holds include **syndication feeds**, which you can see linked from the sidebar. Syndication feeds just contains information about the 10 most recent posts (but I could choose another number if I wanted). You can use syndication feeds to be notified when I add a post, using a **feed reader**. There are different feed formats but they all contain the same info. A feed reader will check if the feed has changed periodically. It only notifies you when the feed has changed, meaning the feed itself only needs to change when a new post is added, which I can do with GitHub Pages.
