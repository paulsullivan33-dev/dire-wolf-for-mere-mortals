# APRS in Plain Terms

APRS — the **Automatic Packet Reporting
System**, built by Bob Bruninga,
WB4APR — is a way for stations to publish
small facts about themselves to whoever
is listening: *I am here. The wind is
doing this. Send this message to that
station. This repeater exists, on this
hill.* One AX.25 frame (chapter 2)
carries one fact, broadcast to everyone,
and listeners assemble the facts into a
map and a message board. This chapter
takes the six facts in the lab's fixture
apart, one at a time, in the order the
lab wrote them. By the end you can read
any packet Dire Wolf prints.

The lab's guide to itself is the project's
own explainer, `decode_aprs`, run on the
same lines (transcript
`dire-wolf-lab/transcripts/t03-decode-aprs.txt`).
What it says about packet one:

```text
N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional
Position, Generic digipeater, DireWolf, WB2OSZ
N 44 49.9800, W 089 30.0200
 Bramble Hill lab site - fictional
```

## A position

The payload's first character is its
**data type identifier** — it says what
kind of fact follows. `!` means a
position with no timestamp (`=` is its
twin; `/` and `@` carry a time as well).
Then the position itself, in APRS's
fixed-width shorthand:

- `4449.98N` — latitude: degrees, then
  minutes to two decimals, then the
  hemisphere. *44 degrees, 49.98 minutes
  north.*
- `/` — the **symbol table** character:
  which set of map icons to draw from.
- `08930.02W` — longitude, three digits
  of degrees.
- `#` — the **symbol code**: in the
  primary table, a digipeater. The
  rover's `>` draws as a car, which is
  what `decode_aprs` reported for packet
  two ("Position, normal car").
- The rest is a free-text **comment**.

Two habits this teaches. Positions are
**public by design** — a beacon is a
notice nailed to a public board, and
chapter 11's internet side makes it more
public still. And the format is
**positional**: one wrong digit quietly
moves you a county. The lab's position
is invented and sits over open farmland;
yours should be as true as you are
comfortable publishing, and no truer.

## An object

```text
N0CALL>APDW17,WIDE1-1:;HILLTOP  *111111z4449.98N/08930.02W#Fictional object from the lab
```

An **object** (data type `;`) is a
position that speaks for something other
than the sender: a repeater, a summit, a
club station, an event. It has a name,
padded to nine characters — `HILLTOP` —
and a live-or-dead mark: `*` means the
object is alive, `_` withdraws it. The
digits after the mark are a timestamp.
Objects are how a fixed thing with no
radio of its own gets on the map: some
station that *does* have a radio
advertises it, and answers for it.

## A message

```text
N0CALL-9>APDW17,WIDE1-1::N0CALL   :Off-air loop test, nobody is transmitting{001
```

Data type `:` opens a **message**. The
addressee — padded to nine characters,
which is why `N0CALL` is followed by
spaces — is a station, or a bulletin
name for news addressed to everyone in
earshot. After the second colon is the
text, and the `{001` at the end is a
**message number**: it asks the
receiving station to acknowledge, by
replying with `ack001`, so the sender
stops repeating the message. APRS
messaging is patient and store-and-
forward — messages hop digipeaters and
igates and wait for a station that may
be off the air — which is why a bare
"hello" carries bookkeeping.

## A status, and telemetry

Two smaller kinds round out the fixture:

```text
N0CALL-5>APDW17,WIDE1-1:>Lab weather box says hello - generated audio only
N0CALL-5>APDW17,WIDE1-1:T#001,123,045,006,078,090,00000000
```

A **status** (data type `>`) is one free
line a station says about itself —
heard, shown, nothing parsed. A
**telemetry** report (data type `T`) is
numbers with no names: a sequence number
(`#001`), five **analog** values from 0
to 255, then eight **digital** bits.
`decode_aprs` reads the lab's as "Seq=1,
A1=123, A2=45, A3=6, A4=78, A5=90" and a
row of zeroed bits. The numbers mean
nothing until the station also sends
definition messages (named `PARM`,
`UNIT`, `EQNS` and `BITS`) saying
*A1 is battery volts, scaled so* — the
subject of chapter 12.

## The shape of the whole system

Notice what APRS never does. There is
no login, no privacy, no delivery
promise. A packet is heard by whoever
hears it: the station two valleys over,
the igate that puts it on the internet
(chapter 11), the archive that keeps it
for years. Paths like `WIDE1-1` and
`WIDE2-2` in the fixture are requests
for repetition (chapter 10), not routing
in the internet sense. And the whole
bustling map is, at bottom, stations
volunteering facts in a fixed format on
a shared channel — which is why the
format is short, why the channel
etiquette is strict, and why chapter 1's
rule is not decoration.

Check: run `decode_aprs` on any line you
meet — including lines from other
people's guides and logs — and it will
name the kind, the position and the
comment in plain words, exactly as it
did for all six of the lab's.
