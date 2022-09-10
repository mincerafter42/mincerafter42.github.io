<?xml version="1.0" encoding="utf-8"?>
<!--
SOMEWHAT SHORTFORM slash SOCIAL STRINGS stylesheet
by https://mincerafter42.github.io

To make your own SSSS:
1. create an RSS 2.0 feed where each <item> has a <description>
2. Place ssss.xsl (this file) in the same directory as the feed
3. Place ssss.css in the same directory as the feed
4. Add the following declaration in the RSS feed, before the <rss> start tag:
       <?xml-stylesheet href="ssss.xsl" type="text/xsl"?>
5. If your browser supports XSLT, navigating to the live RSS feed should show
   an SSSS. You can customize ssss.css or ssss.xsl to your liking.

RSS 2.0 (usually just called RSS) spec: https://rssboard.org/rss-specification

To post *others'* text to give the impression of "reblogging" or similar, you
can use the following Dublin Core elements in your <item>s:
<dc:isPartOf>: The source URL of the text.
<dc:source>: A human-readable name for the source URL.
(Dublin Core spec: http://purl.org/dc/elements/1.1/)
If the text is from another RSS feed, you can use RSS' <source> element 
instead of those Dublin Core elements.

<item>s are automatically given IDs in reverse sequence; don't delete an <item>
since it'll make the IDs of all items before it change
-->
<xsl:transform xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
 <xsl:output method="html" doctype-system="about:legacy-compat"/>
 <xsl:variable name="item-count" select="count(/rss/channel/item) + 1"/>

 <xsl:template match="/">
  <html>
   <xsl:if test="rss/channel/language"><xsl:attribute name="lang"><xsl:value-of select="rss/channel/language"/></xsl:attribute></xsl:if>
   <head>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <script>function htmlifyLast(frames) {frames[frames.length-1].outerHTML="&lt;div&gt;"+frames[frames.length-1].srcdoc.slice(36)}+"&lt;div&gt;"</script>
    <link rel="stylesheet" href="ssss.css"/>
    <link rel="alternate" type="application/rss+xml" href=""/>
    <title><xsl:value-of select="rss/channel/title"/> — Somewhat Shortform/Social Strings</title>
   </head>
   <body class="ssss">
   <div>
    <header class="side content">
     <b>Somewhat Shortform / Social Strings</b><br/>
     A generic social medium with all its flatness and rounded corners. wow. except this time, it's just an RSS feed.
     <xsl:choose>
      <xsl:when test="rss/channel/image">
       <img class="photo" src="{rss/channel/image/url}" alt=""/>
      </xsl:when>
      <xsl:otherwise><span class="photo">No photo</span></xsl:otherwise>
     </xsl:choose>
     <h1><xsl:value-of select="rss/channel/title"/></h1>
     <pre class="flow"><xsl:value-of select="rss/channel/description"/></pre>
    </header>
    <main class="centre content"><xsl:apply-templates select="rss/channel/item"/></main>
   </div>
    <footer class="global-footer">Call 1-899-SCROLLY to claim your prize for scrolling to the end! Just kidding, there is no prize.</footer>
   </body>
  </html>
 </xsl:template>

 <xsl:template match="item">
  <!-- find reblog name and reblog url, if they should exist -->
  <xsl:variable name="dc-source" select="*[namespace-uri()='http://purl.org/dc/elements/1.1/' and local-name()='source']"/>
  <xsl:variable name="dc-ispartof" select="*[namespace-uri()='http://purl.org/dc/elements/1.1/' and local-name()='isPartOf']"/>
  <xsl:variable name="reblog-name">
   <xsl:choose><xsl:when test="$dc-source"><xsl:value-of select="$dc-source"/></xsl:when>
   <xsl:when test="$dc-ispartof"><xsl:value-of select="$dc-ispartof"/></xsl:when>
   <xsl:when test="string-length(source)"><xsl:value-of select="source"/></xsl:when>
   <xsl:when test="source"><xsl:value-of select="source/@href"/></xsl:when></xsl:choose>
  </xsl:variable>
  <xsl:variable name="reblog-url">
   <xsl:choose><xsl:when test="$dc-ispartof"><xsl:value-of select="$dc-ispartof"/></xsl:when>
   <xsl:when test="$dc-source"/>
   <xsl:when test="source"><xsl:value-of select="source/@href"/></xsl:when></xsl:choose>
  </xsl:variable>
  
  <article class="post" id="{$item-count - position()}">
   <header>
    <xsl:choose>
     <xsl:when test="string-length($reblog-name)"><span aria-label="Reblogged">&#128472;</span><xsl:text> </xsl:text><b><a>
      <xsl:if test="string-length($reblog-url)"><xsl:attribute name="href"><xsl:value-of select="$reblog-url"/></xsl:attribute></xsl:if>
      <xsl:value-of select="$reblog-name"/>
     </a></b></xsl:when>
     <xsl:otherwise><b><xsl:value-of select="/rss/channel/title"/></b></xsl:otherwise>
    </xsl:choose>
   </header>
   <main><iframe class="fallback" srcdoc="&lt;link rel=stylesheet href=ssss.css&gt; {description}"/></main>
   <script>htmlifyLast(document.getElementsByTagName("iframe"))</script><!--workaround; mozilla doesn't support disable-output-escaping-->
   <footer>
    <xsl:for-each select="category"> #<xsl:value-of select="."/></xsl:for-each>
    <xsl:if test="category"><br/></xsl:if>
    <a href="#{$item-count - position()}">🔗Link</a>
   </footer>
  </article>
 </xsl:template>

</xsl:transform>
