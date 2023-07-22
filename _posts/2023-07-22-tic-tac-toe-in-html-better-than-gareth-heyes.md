---
title: "\"Implementing Tic Tac Toe with 2MB of HTML - no JS or CSS\""
---
So some internet person named Gareth made [tic-tac-toe in pure HTML, totaling 170MB](https://portswigger.net/blog/tic-tac-toe-in-html).
And I was like "hold your horses, this method has incredible redundancy when storing board states." So I made tic-tac-toe in pure HTML, totaling 2MB. Here's a [python script which generates 2MB HTML tic-tac-toe](/assets/tictactoe.only.html.gen.py). The script iterates over the possible board states, only writing the states that can be achieved through normal gameplay: where the number of Xs is equal to or one greater than the number of Os, where it is possible the previous turn had no three-in-a-row, and where the winner, if any, was the player with the most recent turn.
