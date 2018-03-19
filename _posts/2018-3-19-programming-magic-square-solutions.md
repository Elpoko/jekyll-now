---
layout: post
date: 2018-3-19
title: "Programming Magic Square Solutions"
---

I used to do a lot of Maths Olympiad related stuff.  I came close, but never made the Irish team.  I stopped taking part after Transition Year (4th year of secondary school in Ireland) in order to focus on the Fusor and other projects.

From time to time I still do some problem solving.  A few years ago I got a book "The First 25 Years of the Superbrain" from one of its authors, Prof.  Des McHale.  The Superbrain is an annual Olympiad-style competition for all students in University College Cork, and the book has a nice set of problems (and solutions).

The first problem of the first Superbrain is a magic square style one.  Given a 3 x 3 square containing the whole numbers from 1 - 9, find an arrangement such that each of the sums of the rows, columns and diagonals are unique.  After some trial and error I found one.  One thing to note is that all of the pairs of numbers on either side of the central number must have different sums - i.e. The central row and a diagonal must have different sums, and they share the central number, so the other two numbers in each must have a different sum.  This sort of rule helps to narrow things down for trial and error.

Having found a solution I figured it wouldn't be too complex to find all solutions.  There's probably something very similar already on Project Euler etc.  If you represent the square as an array of length 9, all permutations of [1, 2, 3, 4, 5, 6, 7, 8, 9] correspond to a unique arrangement of numbers in the square.  Mapping each permutation to an array containing the sums of the rows, columns and diagonals of that array is the next step.  Then all solutions are those permutations which give a sum array that has only unique elements.  Say, if the sum array contained 15 twice, then you know two of the rows/columns/diagonals add to 15, which is not a solution.

It took me an hour or so to get a result, using Python 3.  I haven't programmed in months, and never used Python before.  Nonetheless, it was a nice way to get back into coding, and into Python too.  In the past, I've mainly used Ruby (on Rails), but Python is the language of choice for quantum computing kits, so I'm as well off to get acquainted with it.

I'm rushing to write this before heading to bed, would like to rewrite with concepts better explained and attach the code I wrote. 
