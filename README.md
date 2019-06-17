# 1r1l1e

This is basically a Python script to do run-length encoding (RLE). Seeing as RLE
itself provides such poor compression, I thought I would write the script in as
few bytes as possible in order to save disk space.

It works with a similar interface to `base64`. You use `python rle.py` to RLE
encode stdin, and `python rle.py -d` to RLE decode stdin. It doesn't understand
file arguments because that would take up too many LoC. Instead, you should just
attach files to stdin and stdout as appropriate.

The encoding it uses is quite simple - it writes alternating counts and bytes,
where each byte of data is preceded by a count indicating how many times it
occurs. The counts are themselves single bytes. If a count is greater than 255,
it simple gets split into multiple count-byte pairs.

It is unaware of Unicode, but not necessarily to its detriment. It just operates
on stdin as a stream of bytes, and correctly restores this stream after
decoding.

There is also a script that generates some realistic real-world data,
accompanied by a makefile that tests the whole things.
