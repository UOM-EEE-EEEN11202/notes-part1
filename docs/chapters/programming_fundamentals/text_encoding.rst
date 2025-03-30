Text encoding
=============

There are multiple different standards for how computers store and represent text.


ASCII
-----
ASCII stands for the American Standard for Information Interchange. It is the oldest, and extremely common, standard for how characters are represented as binary numbers. 

We often refer to *plain text*, and by this we mean text represented by ASCII (or UTF-8, see below). ASCII is so common that it's extremely unlikely you'll encounter a computer system that's in use today which wouldn't be able to take an ASCII text input and display the associated letters if you asked it to. It's a very robust format to be working with. 

It uses a very simple encoding system. So simple that the full table is displayed at the bottom of this page. Each letter, and a number of other characters such as full stops, are given a binary number that represents them. (The binary number can of course also be represented in decimal form,) If the computer sees this number, and is asked to interpret it as a character, it's the character that gets displayed. A table of ASCII characters and the numbers used to represent each character is given below. ASCII uses 7 bits, and so there are 128 possible characters that it can represent. Some of the early ones represent control signals for a computer, rather than letters.

Latin-I
-------
While very robust, and recognized by essentially every computer, the big limitation of ASCII is that it assumes you are writing English, using the 26 letters of the English alphabet. It is not very inclusive, and does not allow characters from other languages to be used. 

Latin-I was an updated version of ASCII which used 8 bits rather than 7 to represent each character. This allowed the character map to have numbers representing 256 characters rather than 128, and so it supports many character accents, as used in many European languages. 


Unicode and UTF-8 (and similar)
-------------------------------
Unicode and UTF-8 (and UTF-16 and UTF-32) are how plain text is represented in modern computer systems. You may still encounter some older computer systems in use which only recognize ASCII, but in general if you say *plain text* today, this would probably be assumed to be Unicode encoded in UTF-8. Your programming files are being written in plain text, most likely UFT-8 plain text, and VSCode shows you the encoding used for your text file at the bottom of the screen. 

.. figure:: encoding_in_vscode.png
  :width: 800
  :align: center
  :alt: Highlighting of the text encoding used in VSCode
 
The encoding scheme, mapping letters to binary numbers computers can store, is more complicated with Unicode and UFT-8 and the details are not important here. The major benefit of UTF-8/16/32 based schemes is that essentially every character from any language can be represented. It is much more inclusive and should be the default. 

The negative of UTF-8/16/32 based schemes is that there are lots of characters that look very similar. For example, :console:`'` and :console:`’` are both characters for quotes, one is curved and one is straight. It's easy to get the wrong one, especially if copying and pasting between different programs and/or the Internet. In general, programming files expect a straight quote symbol :console:`'`. You'll get an error if you try and put :console:`’` in your code. 

This is just one example. You can get some very hard to spot errors in your text files with characters that look very similar, but are in fact different ones. Occasionally, switching the encoding to ASCII can be useful as it's more limited character set limits what can be entered.


Which should I use
------------------
Most modern files and programs will accept UTF-8. You shouldn't need to worry about text encoding more this until you get to more advanced programming.

.. csv-table::
   :file: ascii.csv
   :widths: 10, 10, 10, 10, 10, 10, 10, 10, 10
   :align: center
   :header-rows: 1
