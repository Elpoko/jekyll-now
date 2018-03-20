---
layout: post
date: 2018-3-19
title: "Programming Magic Square Solutions"
---

From time to time I do some Maths Olympiad style problem solving.  A few years ago I got a book "The First 25 Years of the Superbrain" from one of its authors, Prof.  Des McHale.  The Superbrain is an annual Olympiad-style competition for all students in University College Cork, and the book has a nice set of problems (and solutions).

The first problem of the first Superbrain is like the opposite of a [magic square](https://en.wikipedia.org/wiki/Magic_square):

Given a 3 x 3 square containing the whole numbers from 1 - 9, find an arrangement such that each of the sums of the rows, columns and diagonals are unique.  I.e. The sum of the 3 numbers along the top of the square can't be the same as the sum of the 3 numbers in one of the diagonals, one of the columns, or one of the other rows.

After some trial and error I found one.  One thing to note is that all of the pairs of numbers on either side of the central number must have different sums - i.e. The central row and a diagonal must have different sums, and they share the central number, so the other two numbers in each must have a different sum.  This sort of rule helps to narrow things down for trial and error.

Having found a solution I figured it wouldn't be too complex to find all solutions - using a computer that is...  There's probably something very similar already on Project Euler etc.  If you represent the square as an array of length 9, all permutations of [1, 2, 3, 4, 5, 6, 7, 8, 9] correspond to a unique arrangement of numbers in the square.  From each permutation, create a function that creates a corresponding sum array - A simple array containing the sum of each row, column and diagonal.  If this is sum array contains each number only once (no two of the same number appear), then the permutation corresponding to that particular array has to be a solution of the problem.

Python code [here](../hello.py)

Note that this probably has far more solutions than the magic square, where each sum has to be the same, as opposed to all unique.

I got a working program, using Python 3.  I haven't programmed in months, and never used Python before.  Nonetheless, it was a nice way to get back into coding, and into Python too.  In the past, I've mainly used Ruby (on Rails), but Python is the language of choice for quantum computing kits, I'm as well off to get acquainted with it.

Also I'm reminded of something.  I spent a few weeks in [Intercom](https://www.intercom.com/) during the Summer of 2016, it was fantastic and they were (and continue to be) very nice to me.  One thing I found was that the programming/development I did at Intercom was very different to this sort of problem solving.  Although they're both 'programming', there seems to be a major divide between directly maths/physics/modelling style programming and web development.  I guess it's obvious when you know it, and there's probably a lot more to it at the same time, but the difference was something I had to get my head around at Intercom.

~~I'm rushing to write this before heading to bed, would like to rewrite with concepts better explained and attach the code I wrote.~~ 
