---
layout: post
date: 2017-4-19
title: "DIY Mass Flow Controller Interface"
---

When the Fusor is in operation, it's useful to know how much deuterium is entering the chamber for data collection purposes.  Having some control over this flow is vital for exact operation of the Fusor.  This is where a mass flow controller comes in to play, which both measures and controls the flow of gas.

Because the mass of a given gas volume changes with pressure, measuring the volumetric flow rate in the deuterium line of the fusor would not be accurate, as the pressure in the deuterium line is not constant.  A mass flow controller gives an exact measure of the amount of gas flowing in terms of standard cubic centimetres per minute ([SCCM](https://en.wikipedia.org/wiki/SCCM_(flow_unit))), which accounts for differences in temperature and pressure affecting how much gas is flowing.  You can read more about how they work [here](http://mfchelp.com/mass-flow-controller-tutorial/theory-of-operation), or check out [Ben Krasnow's video](https://www.youtube.com/watch?v=BfdwD1V3jNk&t=310s).

I picked up a Mass flow controller on eBay, a Hastings-Teledyne [HFM-300](http://www.teledyne-hi.com/products-services/thermal-mass-flow/hfm-300-hfc-302).  The specific unit was configured for a maximum 10SCCM flow of N2.  Mass flow controllers are built to cater to a specific gas, but [conversion tables](https://www.mksinst.com/docs/ur/MFCGasCorrection.aspx) exist for taking a reading for a non-configured gas and converting it to a real flow rate.  I got an N2 device on purpose, because the conversion factor between deuterium and N2 is 1.00, or 0.99, which requires no actual converting.
