pstetris
========
I opened my roommate's copy of The Elements of Computing Systems (The nand2tetris.org book) and looked at the Table of Contents.
I noticed the last actual chapter:
Postscript: More fun to go

After many 'fun' experiences with Postscript (the language for creating graphics), I assumed it was referring to the fact that they were going to program Tetris in Postscript. This is not the case sadly.

So I decided to do so.

I'm sorry in advance.

Notes
--------------
I gave up on this after realizing what a nightmare trying to reliably define and place the game pieces in postscript would be. Even if the game logic was broken out into the Python helper, this would be a herculean feat.
My heart goes out to anyone who's tried using postscript for something like this.

Installation
--------------
You'll need ghostscript and ghostview and python. (not that this actually works)

On OS X you can do this with Homebrew

    brew install ghostscript
    brew install gv

Use your favorite package manager on your favorite Linux distribution to get gv.
