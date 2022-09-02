---
title: "OPML feed-reader metadata extension"
date: 2022-09-01 13:19:45 -0700
---

I was certain, given [OPML]'s existed for decades, there'd exist some extension somewhere for user-selected update frequency in OPML.  
I was right! [Thunderbird Mail] stores and loads update frequency in OPML, as well as some other feed reader metadata.  
Thunderbird's ways only seem present in its source code, so I attempted to document them for convenience here. After all, the OPML spec says
"Developers should, whenever possible, use capabilities that are already in use by others, or included in this spec, or recommendations or guidelines",
and this certainly is a capability that's already in use by an other.

The [XML namespace] is "`urn:forumzilla:`".  
(Note that Thunderbird checks for the namespace prefix `fz`, not the namespace itself.
Thus, to support Thunderbird, the xmlns declaration should be `xmlns:fz="urn:forumzilla:"`.)  
(Thunderbird uses the same namespace for some RDF stuff too but that's outside the scope of this document)

## Attributes

The namespace adds the following attributes to OPML `<outline>` elements where `type="rss"` (no behaviour defined for other `<outline>` elements):

### `fz:quickMode`

Optional. Defaults to "`true`".

If "`true`", for each item the reader should show the user a feed message summary (such as from RSS' `<description>` element).  
If "`false`", for each item the reader should show the user a web page (such as linked from RSS' `<link>` element).

### `fz:options`

Optional.

[JSON] containing the following name/value pairs:  
(While I've tried to document their types here, you should probably be prepared for these values to be not present or `null` or an unexpected type. Their default values may be user-selectable.)

`version`
: A Number. Has been known to be `1` or `2`. A reader setting this value must set it to `2` if `updates` is present.

`updates`
: An Object. Contains information about when a reader should request the feed.
  
  `updates.enabled`
  : `true` if the reader should ever request the feed and `false` if it shouldn't.
  
  `updates.updateMinutes` and `updates.updateUnits`
  : The frequency at which the feed should be requested.  
    
    `updateMinutes` is a Number and `updateUnits` is a String.  
    If `updateUnits`' value is "`min`", then `updateMinutes` is the update frequency in minutes.  
    If `updateUnits`' value is "`d`", then `updateMinutes` is the update frequency in days. (1 day is 1440 minutes.)
  
  `updates.lastUpdateTime`
  : A Number, or `null`. The date, in milliseconds since the Unix epoch, when the feed was last requested.
  
  `updates.lastDownloadTime`
  : A Number, or `null`. The date, in milliseconds since the Unix epoch, when the feed was last requested *and* successfully parsed.
  
  `updates.updatePeriod`, `updates.updateFrequency`, and `updates.updateBase`
  : The same content as the corresponding elements from the [PURL RSS module].  
    `updateFrequency` could be a Number or a String.

`category`
: An Object. Contains information about how the feed's items' keywords should be displayed to the user.
  
  `category.enabled`
  : If `false`, keywords should not be displayed to the user.  
    If `true`, keywords should be displayed to the user.
  
  `category.prefixEnabled` and `category.prefix`
  : If `prefixEnabled` is `true`, then `prefix` should be prefixed before every keyword. `prefix` might be a String, or sometimes `null`.

## Example
(This example doesn't include every possible name in `fz:options`)

    <?xml version="1.0" encoding="utf-8"?>
    <opml version="2.0" xmlns:fz="urn:forumzilla:">
     <head/>
     <body>
      <outline type="rss" text="Example Feed" xmlUrl="https://example.com/feed" fz:quickMode="true" fz:options='{"version":2,"updates":{"enabled":true,"updateMinutes":100,"updateUnits":"min"}}'/>
     </body>
    </opml>

[JSON]: https://json.org
[OPML]: http://opml.org/
[PURL RSS module]: http://purl.org/rss/1.0/modules/syndication/
[Thunderbird Mail]: https://www.thunderbird.net
[XML namespace]: https://www.w3.org/TR/xml-names/
