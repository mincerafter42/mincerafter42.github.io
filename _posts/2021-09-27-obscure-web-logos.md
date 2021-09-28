---
date: 2021-09-27 19:57:56 -0700
---
I've found some obscure web logos. They seem obscure to me because just attempting to search for them leads to tons of misinformation.  
I found the logos under the assumption that w3c.org is a trusted source.

## CSS

When searching for CSS logos, most results are some variation on [the HTML5 logo](https://www.w3.org/html/logo/), often in blue.  
However, w3.org actually has the official CSS logo, and  
[![CSS](http://www.w3.org/Style/CSS/Buttons/cssom)](http://www.w3.org/Style/CSS/Buttons)  
it looks ok i guess

There are other variations on the logo:
- [![](http://www.w3.org/Style/CSS/Buttons/cssos) small CSS button](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/mwcos) Made with Cascading Style Sheets](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/cssts) small CSS button but transparency](http://www.w3.org/Style/CSS/Buttons) (dithering!)
- [![](http://www.w3.org/Style/CSS/Buttons/mwcts) Made with Cascading Style Sheets but transparency](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/csstm) big CSS button but transparency](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/csso.svg) CSS but SVG](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/csst.svg) CSS but SVG and transparency](http://www.w3.org/Style/CSS/Buttons)
- [![](http://www.w3.org/Style/CSS/Buttons/mwco.svg) Made with Cascading Style Sheet](http://www.w3.org/Style/CSS/Buttons) (secret! maybe because on systems like mine the font overflows so it says "Style Sheet")
- [![](http://www.w3.org/Style/CSS/Buttons/mwct.svg) Made with Cascading Style Sheet, but transparent](http://www.w3.org/Style/CSS/Buttons) (also secret)

## Atom

When searching for the Atom Feed logo, I get many different images representing atoms, as well as variations on the RSS logo. The actual logo does show up! but it's impossible to tell it's the real one among the impostors.  
Before, I couldn't even tell if an official Atom Feed logo *existed*.

[The W3C Feed Validator's feed docs page](https://validator.w3.org/feed/docs/) links to atomenabled.org, and I trust this means atomenabled.org is itself a trusted source. atomenabled.org has no logo now, but *in the past* it had [Atom Buttons](https://web.archive.org/web/20040222114458/http://www.atomenabled.org/everyone/buttons/) showing the logo, and the logo itself is featured on that page too.  
In fact, the W3C Feed Validator uses one of those Atom Buttons and the logo can be faintly seen there. ![](https://validator.w3.org/feed/images/valid-atom.png)

Using the colour palette from  
![](https://web.archive.org/web/20040222114458im_/http://atomenabled.org/images/atom-logo75px.gif)  
the 75px logo, and the positioning from  
![](https://web.archive.org/web/20040909040847im_/http://atomenabled.org/images/atom-back500px.gif)  
the muted 500px logo, and then throwing out the precise positioning because it was a mess of slight inconsistencies, I was able to construct an SVG version of the Atom logo:
<svg width="500" height="500" version="1.1" viewBox="0 0 500 500" xmlns="http://www.w3.org/2000/svg">
<desc>Atom Feed Logo!</desc>
<g stroke-width="10">
 <defs>
  <mask id="trans" stroke="#000" fill="#fff">
   <rect stroke="none" width="500" height="500"/>
   <circle cx="245" cy="263" r="65"/>
   <circle cx="245" cy="47" r="43"/>
   <circle cx="54" cy="353" r="43"/>
   <circle cx="446" cy="353" r="43"/>
  </mask>
 </defs>
 <g mask="url(#trans)">
  <g fill="none" transform="translate(245 263)">
   <ellipse rx="29" ry="215" stroke="#6e8c9b"/>
   <ellipse transform="rotate(-65)" rx="29" ry="215" stroke="#d5cc74"/>
   <ellipse transform="rotate(65)" rx="29" ry="215" stroke="#83a4c0"/>
   <circle r="215" stroke="#646b41"/>
   <circle r="65" fill="#83a4c0"/>
  </g>
  <g fill="#6e8c9b">
   <circle cx="245" cy="47" r="43"/>
   <circle cx="54" cy="353" r="43"/>
   <circle cx="446" cy="353" r="43"/>
  </g>
 </g>
</g>
</svg>
pretty neato! I don't know what rights i have to this file. like the actual bytes are by me but the icon it represents isn't.
