# Your First Decode

Outcome: given a recording of packet
audio, you can decode it, count what
survived, and say *why* the rest didn't —
the whole receive side of packet radio,
practised on files where nothing can be
harmed by being practised on. The tool
is `atest`, the bench version of Dire
Wolf's decoder: same ears, no radio, no
configuration file, and it runs at
many times real speed.

## The recording

The lab's recording is
`dire-wolf-lab/packets.wav`: 4.7 seconds,
six packets, made in chapter 9 — stay in
order if you can, or just borrow the
file: decoding does not care who made
the audio. Any honest recording works
the same way: a WAV captured from a
receiver on a packet frequency is the
classic source, and collections of test
recordings circulate in the project's
documentation.

## The decode

```bash
atest packets.wav
```

Transcript
`dire-wolf-lab/transcripts/t02-atest-decode.txt`,
trimmed here to its skeleton:

```text
44100 samples per second.  16 bits per sample.  1 audio channels.
417232 audio bytes in file.  Duration = 4.7 seconds.
Fix Bits level = 0
Channel 0: 1200 baud, AFSK 1200 & 2200 Hz, A, 44100 sample rate.
DECODED[1] 0:00.792 N0CALL audio level = 50(14/14)
[0] N0CALL>APDW17,WIDE2-2:!4449.98N/08930.02W# Bramble Hill lab site - fictional<0x0a>
...
6 from packets.wav
6 packets decoded in 0.070 seconds.  67.7 x realtime
```

Read the output in the order it teaches:

- **The header judges the file**: sample
  rate, bits, channels, duration. If a
  recording is at a rate or format
  `atest` cannot use, this is where it
  says so, before any silence confuses
  you.
- **Fix Bits level = 0** — the mercy
  setting of chapter 2: nothing was
  repaired. What follows either passed
  its checksum or is not here.
- **The channel line** names the modem
  chosen for the speed: 1200 baud, the
  two tones, a demodulator profile.
  `atest -B 300` (or 9600) chooses
  another when your recording is not
  the VHF standard.
- **Each decode** gives its position in
  the file, the source it heard, the
  audio level (chapter 6: 50, balanced
  brackets, every time — generated audio
  is well-behaved), and the packet
  itself on a `[0]` channel line, with
  awkward bytes shown honestly — the
  trailing `<0x0a>` is a newline
  `gen_packets` included from the text
  file, decoded like anything else.
- **The summary counts**: 6 decoded, in
  a blink. Files are patient in a way
  the air is not: you can decode the
  same recording all afternoon and the
  answer never changes, which makes
  recordings the right place to learn
  and to test.

## When packets go missing

Same bench, worse weather. Chapter 9
also made `noisy.wav` — twelve copies of
a test packet with noise added in rising
amounts — and transcript t04 holds the
result: **9 decoded of 12**. Nothing in
the output is an error message. The
three lost packets are simply absent,
their absence the only evidence — which
is exactly chapter 2's checksum law seen
from the shore: a frame that fails does
not arrive damaged, it does not arrive.
Real channels behave like this at
smaller scale all day: a fade, a squelch
tail, a level set by guesswork, and a
packet that existed is a packet nobody
saw. The troubleshooting chapter starts
from this table of the missing.

Check: decode `packets.wav` yourself
and hold your output against transcript
t02 — same six packets, same levels,
same summary. Then decode any recording
of your own and count. The ratio is your
channel, confessed.
