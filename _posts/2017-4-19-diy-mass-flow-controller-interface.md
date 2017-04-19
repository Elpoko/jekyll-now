---
layout: post
date: 2017-4-19
title: "DIY Mass Flow Controller Interface"
---

When the Fusor is in operation, it's useful to know how much deuterium is entering the chamber for data collection purposes.  Having some
control over this flow is vital for exact operation of the Fusor.  This is where a mass flow controller comes in to play, which both
measures and controls the flow of gas.

Mass flow controllers are used for controlling how much of a fluid - a gas in this case and most others - flows through a point in
a given time.  When measuring, say, water flow in a pipe, it's enough to know the volumetric flow rate, regardless of temperature or pressure.  
If you know that there's a liter of water flowing per second, you know you're going to be able to fill a milk carton every second.
The mass of water flowing is constant, as is the mass of the water.

This is not the case for a gas under changing pressure or temperature.  While temperature is not too big of a deal in the Fusor's context, 
a liter of deuterium (1000cm^3) at normal atmospheric pressure, 10
