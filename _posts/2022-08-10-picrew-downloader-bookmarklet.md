---
tag: update
title: "Picrew Downloader: This Time, It's Bookmarklet"
---
You may remember my [Picrew Downloader browser extension](/2021/04/18/picrew-downloader).
Well now I've discovered bookmarklets and I've decided the Picrew Downloader would work better as a bookmarklet than as an extension. (technically two bookmarklets, one for downloading the current state and one for downloading the entire maker)
Now I don't have to worry about manifest versions, polyglotting between browsers' different extension implementations, or browser extension stores!  
I also added some spiffy features in the rewrite: A progress bar showing the portion of images downloaded, and a `comment.txt` within the generated file containing the image maker's description. (It's probably ignored by image editors; it's just there if you open the image as a ZIP.)

You can add the bookmarklets at the [Picrew Downloader Bookmarklet](/picrew-download-bookmarklet/) page.

## wait how is it so much smaller

These bookmarklets are approx. 3 kilobytes each, a lot smaller than the Picrew Downloader extension! While the bookmarklets are minified, most of the reduction comes from the removal of JSZip,
the ZIP library I was using, which is nearly 100 kilobytes when minified. JSZip is a fine library, just probably not suited to being embedded in a bookmarklet.

With JSZip removed, I still need a way to generate ZIP files. I decided to leave every file in the ZIP uncompressed. This doesn't enlarge the file very much because JSZip already doesn't compress PNGs.
I then trawled through the ZIP specification and the hexdumps of working ZIP files and wrote basically the minimum amount of ZIP generation code necessary (and took some CRC32 code from StackOverflow).

There's no compression and there's only generation, not extraction, hence the reduced filesize of the ZIP-related code.
