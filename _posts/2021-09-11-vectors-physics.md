---
title: Vectors (Physics)
date: 2021-09-11 18:29:07 -0700
---
Recently the 2021-2022 school year started, including Physics class. The first thing we're doing is reviewing vectors, but yesterday I found a way to not have to draw vectors for a specific task, which has likely already been documented.


## Defining the coordinate forms (in a very obscure manner)
Vectors have direction and magnitude. They can be represented in polar form or rectangular form, and physics class tells me i gotta draw the vectors to convert between them.  
I'm gonna use <abbr title="Augmented Backus-Naur Form">ABNF</abbr> to represent these for no particular reason.
```
polarForm = NUMBER UNIT "@" NUMBER %xB0 DIRECTION ; %xBO is DEGREE SIGN °
; the first number is the vector's magnitude and the second number is the vector's direction
rectangularForm = NUMBER %xEE "+" NUMBER %x135 WSP UNIT
; %xEE is LATIN SMALL LETTER I WITH CIRCUMFLEX î
;%x135 is LATIN SMALL LETTER J WITH CIRCUMFLEX ĵ
; (technically, as defined here, if ĵ is negative the string "+-" would be needed, but just "-" can be used in practice.)

DIRECTION = (NS "of" EW) / (EW "of" NS)
NS = "N" / "S"
EW = "E" / "W"
; indicating angle offset from a cardinal direction to a perpendicular cardinal direction
NUMBER = ["-"] *DIGIT [ "." 1*DIGIT ] ; number, with optional decimal point and optional negative sign
UNIT = 1*VCHAR
```

In rectangular form, <var>î</var> represents the horizontal component and <var>ĵ</var> represents the vertical component. Positive values of <var>î</var> correspond to the east. Positive values of <var>ĵ</var> correspond to the north.

## Converting between the coordinate forms
These correspondences will be needed for both conversions:
- North = positive <var>ĵ</var>
- South = negative <var>ĵ</var>
- East = positive <var>î</var>
- West = negative <var>î</var>

### Polar form to rectangular form
Look at the \<DIRECTION>. It consists of a horizontal cardinal direction and a vertical cardinal direction. These indicate whether the <var>î</var> and <var>ĵ</var> components of the rectangular form will be positive or negative.

The magnitude of the rectangular component corresponding to the <b>first</b> cardinal direction (before the "of") is: the sine of the vector's direction, multiplied by the vector's magnitude.  
The magnitude of the rectangular component corresponding to the <b>second</b> cardinal direction (after the "of") is: the cosine of the vector's direction, multiplied by the vector's magnitude.
### Rectangular form to polar form
Using the correspondences, determine which horizontal and which vertical cardinal direction will be used in the polar form.  
Here the horizontal direction will always be first and the vertical direction will always be second, because it's easier.

The vector's direction is: the absolute value of the tangent of (<var>î</var> divided by <var>ĵ</var>).
The vector's magnitude is: the square root of (î² + ĵ²). (yes it's just the Pythagorean theorem again.)
## Conclusion
bye
