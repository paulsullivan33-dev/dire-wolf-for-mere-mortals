# The Igate and Its Responsibilities

An **igate** — internet gateway — is a
station with one foot in each world: it
hears APRS on the radio and posts what
it heard to the **APRS-IS**, the APRS
internet system, a worldwide network of
servers that gather every packet from
every connected igate into one stream.
Websites draw the global map from that
stream; a station with no internet of
its own appears on it because some
volunteer's igate heard its beacon.
Two-way igates also run the road back:
messages from the internet side,
addressed to stations recently heard on
the local frequency, are transmitted on
the radio. This chapter describes the
machine and then spends its second half
where the first half of this book would
predict — on what the operator answers
for. The lab ran no igate: no connection
was made, no passcode used, nothing
forwarded. The configuration forms below
follow the project's own shipped
examples, and are labelled documented,
here and in `criteria.md`.

## The shape of the connection

Three lines of configuration carry the
idea, in the shape the project's
examples ship:

```text
IGSERVER noam.aprs2.net
IGLOGIN N0CALL 123456
```

**IGSERVER** names a regional server of
the APRS-IS — the shipped example uses
the North American pool; other pools
serve other continents. **IGLOGIN** is
the station's call sign and its
**passcode**: a number computed from
the call sign by a published little
algorithm. Understand what that makes
it: an *identifier*, not a lock. The
algorithm is public, anyone can compute
anyone's, and the system's honesty runs
on the same fuel as the radio side —
your call sign attached to everything
you send, and the community's long
memory.

A receive-only igate stops there: hear,
post, done — no radio transmission
involved, only the duty of posting
honestly. The road back to RF is gated
harder, and rightly:

```text
IGTXVIA 0 WIDE1-1
```

**IGTXVIA** permits transmitting, on
channel 0, with the stated path — and a
companion limit line (`IGTXLIMIT`, which
the distribution's own example
configuration carries) caps how many
gated packets per hour may go out. The
defaults lean towards silence: the
internet stream is a firehose, the local
channel is a village lane, and a TX
igate is a valve, not a funnel.

## What the operator answers for

Chapter 1's rule was about transmitting.
The igate form is sharper, because the
transmitter is now partly *other
people's intentions*:

- **Everything you forward wears your
  call sign.** A packet your igate posts
  is recorded against your station, on a
  system with archives. A packet your TX
  igate transmits is, in law and in the
  community's eyes, your transmission —
  the internet sender has no licence,
  no call sign of consequence, and no
  presence; you have all three.
- **The firehose is not yours to pour.**
  Gating general internet traffic onto
  RF would swamp the local channel in
  minutes. The accepted pattern is
  narrow: messages addressed to stations
  your receiver has actually heard,
  locally, recently — plus the rate
  limit, set and left alone.
- **Unattended is not unaccountable.**
  Igates run for months unwatched, on
  hilltops and in spare rooms. The
  station is still yours on the day its
  clock is wrong, its position is stale,
  or its software misbehaves into the
  stream. Run one you can reach, read
  its logs sometimes, and let it be
  known whose it is: a station beacon or
  object naming the operator is the
  community's custom for a reason
  (chapter 12).

None of this is a reason to never run
one. Igates are how most of the map
exists — a travelling station's family
watches it cross the country because a
chain of strangers' receivers posted
its beacons. It is a reason to run one
*as* infrastructure: deliberately,
configured narrowly, under your own
name.

Check: the honest test of readiness is
chapter 5's, unchanged — if your
configuration still carries the
placeholder call sign, the question of
an igate has not yet arisen, and Dire
Wolf's four warnings are the correct
and complete review of the plan.
