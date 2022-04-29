---
title: Recreational Drugs? No Thanks, I Prefer Recreational Hugs
---
I love cuddling!

Of course, this website is part of the [Cuddler Webring](https://cuddler-webring.netlify.app/).  
[«Cuddler Webring Previous](https://cuddler-webring.netlify.app/mincerafter42/previous) \| [Cuddler Webring Next»](https://cuddler-webring.netlify.app/mincerafter42/next)
{:style="text-align:center"}

## Cuddly geometry
<i>Trigonometry? In your cuddles? It's more likely than you think!</i>

<p><time datetime="2022-04-28">Recently</time>, a session of virtual cuddling led to a hidden trigonometry problem! dun dun dun<br>
In this case, the two of us were approximately the same height, so in this visual aid I'll just use identical copies of a public domain human silhouette.</p>
<svg width="300" viewBox="0 0 100 100">
<desc>Two identical human upper bodies in profile, labeled "Person 1" and "Person 2"</desc>
<path id="person" d="m11.47 89.67c3.876-8.701-2.765-23.49.2504-37.48.4282-1.714.6658-3.383 2.3-5.592 2.16-4.014 1.66-10.7.1492-12.97 0 0-2.966-3.914-3.055-6.062 0 0-.7826-3.624 2.916-7.751 1.778-1.983 4.129-3.825 9.936-3.867 2.269-.01896 5.733.5168 8.428 3.367 1.631 1.721 2.832 3.896 2.49 7.448-.07405.7703-1.175 1.662-.4015 3.152 0 0 1.661 2.924 1.606 3.413 0 0 .03026.8911-1.348.9173 0 0-.3426.04556-.2429.8036l.01434 1.104s-.04395.3289-.646.5296c0 0-.1148.1145.05733.3304 0 0 .3154.3542-.2311 1.118-.2024.2798-.5281.6305-.3291 1.348 0 0 .2582 1.387-.2866 1.72 0 0-.619.7336-3.112.4275-.8687-.1064-2.48-.5304-3.439.6745 0 0-.166 2.55.8021 3.856 1.987 2.442 3.508 4.554 4.505 7.241 2.161 5.82 2.398 9.524 2.009 15.03-.4053 5.727-.6976 11.41-1.393 17.1-.1656 1.355-.2044 2.856-.03806 4.056" fill="#fff" stroke="#000"/>
<use x="53" href="#person"/>
<g font-family="sans-serif" font-size="4pt" text-anchor="middle" aria-hidden="true">
<text x="23.49" y="10">Person 1</text>
<text x="76.51" y="10">Person 2</text>
</g>
</svg>
*Will person 2 be able to give person 1 a little kiss on the cheek in the following configuration?* We have to use *math!*
<svg width="300" viewBox="0 0 100 100">
<desc>Person 2 leans back onto person 1's shoulder.</desc>
<g id="people-leaning">
<use href="#person"/>
<use transform="rotate(-38.52 37.94 21.93)" href="#person"/>
</g>
</svg>
(The measurements I use are my measurements; values will be unique to every case)
<svg width="300" viewBox="0 0 100 100">
<desc>A right triangle is drawn from person 2's mouth to person 1's lower torso to person 2's lower torso. Person 1's lower torso is the right angle and Person 2's lower torso is marked with θ. The edge opposite θ is 60cm. A line perpendicular to the hypotenuse starting at person 2's lips and ending at the back of person 2's head is labelled "Person 2's mouth possible locations". This line divides the hypotenuse into two sections, the lower of which is 59cm.</desc>
 <defs><marker id="Arrow2Send" overflow="visible" orient="auto"><path d="m-1.926-1.210 3.279 1.205-3.279 1.205c.5235-.7116.5205-1.685 2e-7-2.411z"/></marker></defs>
<use href="#people-leaning"/>
<g font-family="sans-serif" font-size="4pt" text-anchor="middle" aria-hidden="true">
<text x="58.94" y="13.94">Person 1's cheek</text>
<text><tspan x="75.26" y="39.35">Person 2's mouth</tspan><tspan x="75.26" y="44.69">possible locations</tspan></text>
<g fill="none" stroke="#000">
<g id="theta"><path d="m61.89 97.76a11.17 11.17 0 014.459-8.825"/><text fill="#000" stroke="none" x="66.41" y="96.39">θ</text></g>
<path d="m50.51 43.74-7.601-3.624" marker-end="url(#Arrow2Send)"/><path d="m44.5 16.62-15.48 14.45" marker-end="url(#Arrow2Send)"/>
<path d="m25.78 92.84h5.025v5.025" id="right-angle"/><path d="m30.24 40.1 3.905-3.163 3.163 3.905"/>

<g stroke="red" id="triangle-1">
<path d="m25.73 34.13v63.73h47.33z" stroke-dasharray="3"/>
<path d="m43.94 36-15.08 11.07"/>
<g stroke="none" fill="#000">
<circle cx="25.73" cy="34.13" r="1.852" fill="red" stroke="none"/>
<text transform="rotate(-90)" x="-65.45" y="24.09">60cm</text>
<text x="75.83" y="-.2067" transform="rotate(52)">59cm</text>
</g>
</g>

</g>
</g>
</svg>
<svg width="300" viewBox="0 0 100 100">
<desc>A similar right triangle is drawn, from person 1's shoulder (the contact point) to person 1's lower torso to person 2's lower torso. The edge opposite θ is 51cm and the edge adjacent to θ is 35cm. θ≈atan(51÷35)≈55°</desc>
<use href="#people-leaning"/>
<g font-family="sans-serif" font-size="4pt" text-anchor="middle" aria-hidden="true">
<g fill="none" stroke="#000">
<use href="#theta" x="-7.5"/>
<use href="#right-angle" x="5.5"/>
<g stroke="red"><path d="m65.92 97.79h-34.55v-46.66"/><path d="m31.38 51.14 34.55 46.66" stroke-dasharray="3"/></g>
<path d="m52 41-17 8.7" marker-end="url(#Arrow2Send)"/>
</g>
<circle cx="31.4" cy="50.9" r="1.852" fill="red"/>
<text x="58.94" y="13.94">Similar triangles</text>
<text><tspan x="73" y="39.35">Person 1's shoulder</tspan><tspan x="73" y="44.69">(contact point)</tspan></text>
<text transform="rotate(-90)" x="-75.09" y="29.96">51cm</text>
<text x="45.84" y="96.34">35cm</text>
<text><tspan x="77.5" y="83">θ≈atan(51÷35)</tspan><tspan x="77.5" y="88.34">≈55°</tspan></text>
</g>
</svg>
<svg width="300" viewBox="0 0 100 100">
<use href="#people-leaning"/>
<desc>On the first triangle again, hypotenuse≈60÷cos(55°)cm≈72cm. The upper segment of the hypotenuse is 72-59=13cm.</desc>
<g font-family="sans-serif" font-size="4pt" text-anchor="middle" aria-hidden="true">
<text x="50" y="12">hypotenuse≈60÷cos(55°)cm≈72cm</text>
<g fill="none" stroke="#000">
<use href="#theta"/>
<use href="#right-angle"/>
<use href="#triangle-1"/>
</g>
<text transform="rotate(52)" x="46.62" y="-.9276">13cm</text>
</g>
</svg>
So the general formula for the distance person 2 needs to move their head upwards in this scenario is:<br><br>
(distance from person 1's cheek to thigh÷cos(atan(distance from person 1's shoulder to thigh÷distance from person 1's lower torso to person 2's lower torso)))-distance from person 2's lips to thigh<br><br>
And in this particular case, person 2 needs to move their head 13cm upward. Difficult from this position, but doable.

To prevent such math from being needed *during* cuddling, perhaps cuddlers should precalculate some cuddly constants :p

## Cuddly images
Cuddle-related images which I use in text-based communication; perhaps you will too.

![Ellen: *glomp* Hi Susan!
Susan: Ellen, I presume?
Ellen: Yep!
Susan: "Glomp"?
Ellen: You know, like, a big hug...
© 2005 Dan Shive](/assets/glomp.png)  
Good for introducing the concept of a glomp. From <i>[El Goonish Shive](https://www.egscomics.com/comic/2005-03-30)</i>.

![Tired... Want cuddles...](/assets/cuddles.png)  
From <i>Still Sick</i>.
