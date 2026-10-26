# Making a Packet and Hearing It Back

Chapter 8 decoded somebody else's audio.
This chapter makes your own — with no
radio, no licence question, and no
audience — and closes the loop by
decoding it again. Outcome: you have
written real APRS packets as text, heard
what they become as sound, and proved
with the checksum that what came back is
what you wrote. It is the transmit side
of the modem, rehearsed into a file.

## The fixture: six packets in words

Everything starts as text —
`dire-wolf-lab/packets.txt`:

```text
N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional
N0CALL-9>APDW17,WIDE1-1:!4450.10N/08929.88W>Lab rover, invented for the guide
N0CALL>APDW17,WIDE1-1:;HILLTOP  *111111z4449.98N/08930.02W#Fictional object from the lab
N0CALL-9>APDW17,WIDE1-1::N0CALL   :Off-air loop test, nobody is transmitting{001
N0CALL-5>APDW17,WIDE1-1:>Lab weather box says hello - generated audio only
N0CALL-5>APDW17,WIDE1-1:T#001,123,045,006,078,090,00000000
```

You have met every one of these in
chapter 3: two positions, an object, a
message that asks for an acknowledgement,
a status line, and a telemetry report.
The station is fictional, the hill is
invented, the position is open farmland,
and the call sign is the placeholder —
because nothing here will ever be
transmitted, and the file is a *fixture*,
a thing made to be measured. Write yours
the same way while you are learning:
true statements about nobody.

## Text into audio

```bash
gen_packets -o packets.wav packets.txt
```

`gen_packets` is Dire Wolf's modulator
as a file tool: it reads packets in the
written form of chapter 2 and emits the
complete on-air signal — framing,
checksum, bit-stuffing, NRZI, tones — as
a WAV. Transcript
`dire-wolf-lab/transcripts/t01-gen-packets.txt`
shows it echoing each packet as it
encodes it, and the result:

```text
$ ls -l packets.wav
-rw-rw-r-- 1 dwlab dwlab 417276 Oct 26 03:52 packets.wav
```

4.7 seconds for six packets: packet
radio is not in a hurry, and half of the
file is the honest overhead of flags and
gaps that a real transmission also
spends. The tool's options (its usage
text lists them) set the baud rate, the
tones, the amplitude; the defaults are
the 1200-baud standard the whole guide
uses. Play the file through speakers and
you will hear chapter 2: a warbling
two-tone chatter, each packet a short
burst. That sound, unremarkable in
itself, is the entire payload of a
packet station's life.

## Audio back into text

Chapter 8 already ran the return half —
`atest packets.wav`, 6 of 6, levels at
50 — so this chapter claims the loop as
a whole and points at the two numbers
that prove it: **six lines went in,
six packets came out, and every one
passed the checksum that would have
rejected a single flipped bit.** Nothing
about the loop is simulated: the audio
is the true modulated signal, and the
decoder that read it is the decoder a
live station runs. Swap the WAV for a
recording of a radio and only the source
of the audio changes.

## The loop, abused on purpose

A loop that only passes teaches half
the lesson, so the lab broke it gently.
`gen_packets` has a noise option — `-n
12` generates its own test packet twelve
times with noise added in rising
amounts. Transcript t04 is the autopsy:
the first nine decode (at climbing audio
levels, chapter 6's warning in numbers),
and the last three are simply gone. Keep
both files' results in mind the first
time a live station seems to "mostly"
work: the channel does not grade on a
curve, and neither does the checksum.

Check: write one packet of your own in
the fixture's shape — a position with an
invented comment — add it to a copy of
the text, regenerate, and find your line
in the decode, word for word. That is
the whole transmit chain of APRS,
minus the radio, and minus any need for
permission to practise it.
