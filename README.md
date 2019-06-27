# 1r1l1e

This is basically a Python script to do run-length encoding (RLE). Seeing as RLE
itself provides such poor compression, I thought I would write the script in as
few bytes as possible in order to save disk space.

You use `python rle.py` to RLE encode stdin, and `python elr.py` to RLE decode
stdin. The use of separate programs avoids branching and parsing of argv in
the scripts, which is a huge savings on bytes. It doesn't understand file
arguments because that would take up too many LoC. Instead, you should just
attach files to stdin and stdout as appropriate.

The encoding it uses is quite simple - it writes alternating counts and bytes,
where each byte of data is preceded by a count indicating how many times it
occurs. The counts are themselves single bytes. If a count is greater than 255,
it simply gets split into multiple count-byte pairs.

It is unaware of Unicode, but not necessarily to its detriment. It just operates
on stdin as a stream of bytes, and correctly restores this stream after
decoding.

There is also a script that generates some realistic real-world data,
accompanied by a makefile that tests the whole things.
