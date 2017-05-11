---
layout: post
date: 2017-4-30
title: "Irregular Conflat Gaskets"
---

I ran into a bit of trouble recently with an irregularly sized conflat port, still working through it:

In pulling a vacuum in a chamber, it must be sealed from the surrounding atmosphere/air.  Otherwise the outside air will keep rushing in (a leak) as the vacuum pump(s) work and there'll never be a decent vacuum.  Calling it a leak would make you think the air is 'leaking' out of the vessel, but in vacuum context, a leak is air coming in.

Conflat is the gold standard for vacuum seals.  A [conflat seal](http://www.lesker.com/newweb/flanges/flanges_technicalnotes_conflat_1.cfm) is made up of two unisex flanges, and a gasket.  The flanges have a narrow metal lip below the flange face around the interior circumference.  The edge of the lip is called a knife edge.  A gasket, usually copper, but aluminium is sometimes used, viton too, fits snugly in the lips between the two flanges.  The flanges are bolted together, causing the knife edge to [bite into the gasket](http://www.mtm-inc.com/av-20150331-how-a-cf-knife-edge-seal-works.html) on both sides and seals the interior system from the outside.  Copper gaskets are almost never reused.  A picture paints a thousand words:

![Conflat flange]({{ site.baseurl }}/images/penning_conflat.jpg)

Bringing me to the main point:  The high vacuum gauge I'm using in the Fusor is a [Penning gauge](https://cds.cern.ch/record/455555/files/p75.pdf).  It has a standard 2.75" port for connecting, of which there are 4 to choose from on the chamber.  There are a range of standard conflat sizes, based on the outside diameter of the flange, specified in inches or DNXX, European standard, which measures the connected pipe diameter in mm eg 2.75" = DN40.  For the standard sizes, gaskets are easy to get.  So, all was good with the Penning gauge, until it started acting up and I took it apart.  There was an internal conflat seal, smaller than the 2.75" one.  I compared it and its gasket dimensions to the smaller standard sizes (2.125", 1.33", 1") for ordering new gaskets.  No luck, I was stuck with an odd-one-out.  

Having to work with an irregular sized fitting means gaskets can't be ordered from the normal suppliers, and are more expensive.  This isn't terrible; there's nothing awfully special about the gaskets used, just need the right dimensions.  The copper doesn't need to be specially treated or anything.  The gasket dimensions are OD: ~29.4mm  ID: ~21.5mm.  I initially ordered a set of 1.33" gaskets, hoping they were right, but they were too big.  They weren't suitable for grinding down to fit as their ID was too large, and the gaskets wouldn't contact the knife edge.

Giving up on standard sizes, I was pointed in the direction of [copper crush gaskets](http://www.ebay.com/bhp/copper-crush-washers) and ordered a set of 30mm.  These arrived, and I grinded one down to fit and bolted up the flanges.  Promptly met with the hiss of a leak when I turned on the RV3 (forepump).  Got the right OD and ID, but neglected to check the gasket thickness and the gasket was too thin and had some wiggle room to avoid sealing.  

Time to get some 30mm OD, 22mm ID, 2mm thick copper gaskets.  Hoping I don't get something wrong again.  Irregular sizings are a pain.
