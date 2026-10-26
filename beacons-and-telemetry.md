# Beacons and Telemetry

A packet station that only answers is
half a station. **Beaconing** is the
other half: speaking on a schedule, so
the map knows you exist before anyone
asks. This chapter takes apart the
beacon line from chapter 5, its cousins
for objects and for stations that move,
and the telemetry reports of chapter 3
grown into a working habit — what the
numbers mean, and how a station teaches
listeners to read them. The mechanics
were all met in the lab; the operating,
on air, is documented.

## One line, one beacon

Chapter 5's announcement, again:

```text
PBEACON delay=1 every=30 overlay=S symbol="digi" lat=44.8330 long=-89.5003 comment="Bramble Hill lab site - fictional"
```

- **PBEACON** — a position beacon: "this
  station, here, saying this."
- **delay** and **every** — wait a
  minute after starting, then repeat
  every 30 minutes. Times in Dire Wolf
  beacon lines are minutes, or
  minutes:seconds.
- **lat / long** — decimal degrees here,
  where chapter 3's packets carried the
  degrees-and-minutes form; the beacon
  line takes the friendlier notation
  and converts.
- **overlay / symbol** — the map icon,
  the same table-and-code pair of
  chapter 3 in friendlier dress.
- **comment** — the free text. Also the
  place a digi or igate names its
  operator (chapter 11's custom), and
  the first thing to make truthful when
  a station moves house.

The path a beacon asks for is a separate
choice — a `via=` on the line — and it is
an etiquette decision wearing a config
line's clothes: a fixed station beaconing
to `WIDE2-2` every ten minutes is buying
two counties of airtime to say *still
here*. The defaults lean local for a
reason.

## Cousins: objects and trackers

**OBEACON** is the same line for an
object (chapter 3): the station speaks a
position and a name for something that
has no radio — a repeater, a meeting, a
summit — and takes responsibility for
keeping it true, including withdrawing
it when it stops being true. **TBEACON**
is the tracker's line: it reads a GPS
(via **gpsd**, for which the lab's build
reports support compiled in) and beacons
a *moving* position, with **smart
beaconing** — the documented algorithm
that beacons faster when travelling
fast or turning, slower when parked, so
the track on the map is dense where the
road was interesting and silent where
nothing happened. A transponder in a
balloon, a car on a long drive: same
line, judged by whether the rate tells
the story without shouting it.

## Telemetry: numbers with names

Chapter 3 met the raw report:

```text
N0CALL-5>APDW17,WIDE1-1:T#001,123,045,006,078,090,00000000
```

Five analog values, eight digital bits,
a sequence number — and no units, no
names, no scale. The completed system
is a conversation of four message kinds,
sent as addressed APRS messages to the
station's own call sign:

- **PARM** names the channels: *batt,
  temp, ...*
- **UNIT** gives their units: *volts,
  degrees, ...*
- **EQNS** gives the scaling: each
  analog value is read as
  *a·x² + b·x + c* with coefficients
  from the message.
- **BITS** names the digital bits and
  their sense.

A listening program that has collected
the definitions draws labelled graphs
instead of rows of bytes: the
solar site's battery sagging through
the night, the hilltop's temperature in
a storm. Dire Wolf's part in this is
honest plumbing — it can build telemetry
beacons from values a small script
supplies (the distribution ships
example configurations that do exactly
this, reading a script's output on a
schedule), and it carries other
stations' reports like any packet. The
definitions are the station's promise
that the numbers mean what the graph
will say, which is why the telemetry
chapter of a careful station is mostly
prose like this one.

Check: you understand the fixture —
`decode_aprs` on the lab's telemetry
line (transcript t03) prints the bare
values, *Seq=1, A1=123, ...*, precisely
because the lab station never sent its
definitions. A reader who can say what
is missing, and which four messages
would supply it, has this chapter.
