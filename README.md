## Overview
This is a very simple Raspberry Pi Pico project to turn on/off a strip of LEDs in a cabinet. The cabinet 
has double doors.  If either door is opened, the LED strip is turned on. When both doors are closed, the 
LED strip is turned off.

## Technical Details
Even though this is programmatically very simple, I'm going to the trouble of writing this because 
as far as I know, there are few documented examples of opto-couplers for the Pico. 

### Opto-Couplers 
Someone suggested I try [opto-couplers](https://en.wikipedia.org/wiki/Opto-isolator) instead of 
[reed switches](https://en.wikipedia.org/wiki/Reed_switch) to sense when a door is open.  That sounded 
like a good idea, so this project uses opto-couplers exclusively. [Here](https://www.amazon.com/dp/B08977QFK5?psc=1&ref=ppx_yo2ov_dt_b_product_details) 
is the particular one I'm using.


### State Detection

Since there are 2 doors on the cabinet, there are 2 opto-couplers to detect their individual status. Each 
opto-coupler is mounted on the door frame in the upper left and right respectively (see pics below). On 
each door is a small plastic wedge which fits in the opto-coupler's slot. When the door is closed, the
wedge interrupts the beam sent from one arm of the slot to the other. Conversely, when the door is open,
the wedge is pulled away and the beam is uninterrupted. 

### Wiring


## Lessons Learned 
Opto-couplers are a mixed blessing.  On the one hand, they are simpler then a reed switch to program. With reed switches, you have to 
contend with Normally Open/Normally Closed logic that can be confusing (not to mention the one [case](https://github.com/gamename/raspberry-pi-pico-w-mailbox-sensor#fun-with-reedish-switches) 
I experienced where the vendor got it backwards).  With opto-couplers that goes away. there are only two states: open and closed.

However, reed switches are simpler to set up mechanically.  You just make sure the switch is in proximity to a magnet,
and you're set.  Opto-couplers, or at least the version I'm using, require a more precise approach.  There is a beam
between the 2 arms of the coupler and something has to break that beam in order to establish a state change. Cobbling
that together takes some ingenuity.  I experimented with several physical configurations before I found one I liked. Hence, the opto switch is physically more of a challenge.

## Gotchas 
There was one interesting gotcha. Everything seemed to be working after the initial installation.  The LEDs came on as 
expected when I opened the doors.  But the LEDs would NOT turn off when both doors were closed. Ok, I thought, the beams
are not interrupted by the wedges I had screwed to the doors.  Alignment problem of some kind, no doubt.  

But after re-re-checking alignment, it was clear they were exactly where they should be: positioned between the beam 
emitter and receiver when the door was closed.  

After much experimentation, I figured out the *color* of the wedge was key.  My example was light colored.  I tried putting a white sheet of paper in the slot (between transmitter 
and receiver) and got the same result. The coupler didn't consider itself "blocked". I then tried a dark sheet of paper and got a successful result.  Therefore, the coupler would consider itself blocked if something dark was used. 

On a hunch, I wrapped black electrical tape around the wedges (see pics below) and it worked! The coupler finally considered itself
blocked with the doors closed.  The LEDs dutifully turned off. 

Bottom line: Whatever blocks the beam on the coupler needs to be dark.

## Pictures 

## Parts List
raspberry pi Pico
Pico breakout board
optocouplers
project box
magnetic tape
sliding door guides (hack to create the wedges)
black electrical tape
wire
wire joiners
USB power supply
USB power cable
wood screws
drill
Phillips head screwdriver drill bit
5/32" drill bit
nylon screws and bolts
wire cutters
Dupont wire connectors
Dupont wire connector crimping tool






