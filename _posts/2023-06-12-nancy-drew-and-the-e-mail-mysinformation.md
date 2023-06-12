---
title: "Nancy Drew and the E-mail Mysinformation"
date: 2023-06-12 14:21:22 -0700 
---
(Thanks to Fabian for that pun)

So I read <i>Nancy Drew and the E-mail Mystery</i> (1998).
Of course a book about the Internet from 1998 for general audiences is going to
be outdated and assume the reader is unfamilar with the Internet, but what I
list here are the instances of outright misinformation in this book. Enjoy :p

1. This is not how e-mail works:

   > She entered the “virtual mailroom.” There she addressed the copies of the settlement documents to the phone number listed for Williams & Brown and dialed them on the modem.

   This sounds more like a fax than an e-mail, the thing which uses e-mail addresses and not phone numbers.

2. > “You can tell what kind of organization a computer is in by the last part of its Internet address—”  
   > “Is that an IP address?” Nancy asked, remembering the term Bess had used.  
   > “That's right,” Byron said. “IP stands for Internet Protocol. So, as I was saying, the last part of that name tells you what kind of organization the computer belogs to. For instance, educational institutions, like schools and universities, all end in ‘edu’. Government offices, like NASA and the White House, end in ‘gov’. Military groups, like the navy or the air force, end in ‘mil’. And commercial companies, like television networks or computer manufacturers, end in ‘com.’”

   ......NO those are URLs not IP ADDRESSES!

3. Apparently she needs a digital copy of a PLAIN TEXT LOG FILE which she PRINTED OUT because the digital copy CONTAINS INFORMATION WHICH ISN'T IN THE PRINTOUT‽‽

4. > ... warnings not to give out their company or school's computer system, modem phone numbers, or other identifying information that could be used by computer pirates.
   
   Pretty accurate except for the COMPUTER PIRATES!

5. > The two girls watched in fascination as the screen filled with letters, numbers, names, dates, abbreviations.  
   > “What is all that?” Nancy asked, mystified.  
   > “Most mail programs filter out all this stuff,” Henry said. “But it's what tells the mail server how to route the mail, identifies each computer user who sends E-mail out, and where it went. Take a look.” He pointed to what looked to Nancy like a coded language.

   Now this is just E-MAIL HEADERS, the thing I can see on my e-mail client just by pressing CTRL+H.
   The headers look to be in mbox format. They are sensible except for a missing space, an IPv4 address with six bytes instead of the usual four, and the fact that there's a `Received:` header when this is supposed to be the sender's log, not the recipient's.
