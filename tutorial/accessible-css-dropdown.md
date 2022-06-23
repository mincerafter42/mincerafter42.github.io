---
title: Accessible CSS navigation dropdown
last_modified_at: 2022-06-23
---
There are many tutorials for accessible CSS navigation dropdowns online, but none of them use the method I had in my mind for the past couple of years. Which is odd, considering I thought I had learned it somewhere.
Well, now I can share my knowledge!

**This tutorial assumes you are already familiar with HTML and CSS.**

For sighted users, the content of the dropdown isn't visible until it's hovered or focused.  
For keyboard users, the dropdown's interactive elements are focusable just as any other interactive elements, and the dropdown content appears when an element is focused.
(Do note this tutorial is only useful for dropdowns *of interactive elements*.)  
For sightless users, the dropdown's interactive elements can be interacted with exactly like always visible navigation.

## Example
<nav class="tutorial-dropdown">
<img class='dropdown-icon' src="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' width='35' height='30' ><path d='m0 0h35v6h-35zm0 12h35v6h-35zm0 12h35v6h-35' fill='white'/></svg>" alt>
<ul>
<li><a href="http://example.com">Stuff</a></li>
<li><a href="http://example.net">Things</a></li>
<li><a href="http://example.org">Thing-Stuff</a></li>
</ul>
</nav>
<style>
.tutorial-dropdown {display:inline-block;}
.tutorial-dropdown:not(:hover, :focus, :focus-within) :not(.dropdown-icon) {position:absolute;left:-9999px;}
</style>

(the example may be a bit small on some devices because i haven't implemented the `<meta name=viewport>` element)
<section markdown=1>
## Code

aight so you got your `nav` and give it a nice `class` and put your interactive elements inside it. Also put an element with class `dropdown-icon` inside, which will be the only visible part when the dropdown is closed:
~~~html
<nav class=dropdown>
<img class=dropdown-icon src=/dropdown-icon.svg alt>
<ul>
<li><a href=/stuff>Stuff</a>
<li><a href=/things>Things</a>
<li><a href=/thingstuff>Thing-Stuff</a>
</ul>
</nav>
~~~
(in this example I use an `img` element; the `alt` attribute is empty because the image only serves a purpose for mouse users)

then in your CSS you wanna do a:

~~~css
.dropdown {display:inline-block;}
.dropdown:not(:hover, :focus, :focus-within) :not(.dropdown-icon) {position:absolute;left:-9999px;}
~~~

### CSS explanation

`.dropdown {display:inline-block}` is here because i felt the hoverable area with `nav`'s default `display:block` would be unexpected for users.

`.dropdown:not(:hover, :focus, :focus-within) :not(.dropdown-icon) {position:absolute;left:-9999px;}` means all the dropdown's children, except the dropdown-icon, will be hidden unless the dropdown is hovered or focused.
However, to avoid hiding the elements from keyboard users or sightless users, the children are just moved offscreen.  
If I remember correctly, in right-to-left writing systems it's better to use the `right` attribute here instead of `left`.  
The reason I use the `:not()` selector is so browsers which don't support this CSS will always show the menu rather than always hide it.
</section>

Of course you can customize the CSS to your own website.

You can also put dropdowns within dropdowns.

You can use a [CSS width media-query](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/width) to make the dropdown only present on small screens, making the menu always visible on larger screens.

I hope I've helped!  
If you find any problems with this tutorial, please contact me.
