.PHONY: default integrity

SHELL = bash

default: integrity
	@make -B data.dec

data.dat: make_data.py
	python make_data.py > $@.tmp
	cat make_data.py $@.tmp rle.py > $@
	rm $@.tmp

data.rle: data.dat
	python rle.py < $< > $@

# https://stackoverflow.com/questions/34943632/linux-check-if-there-is-an-empty-line-at-the-end-of-a-file
integrity:
	@if [ -z "$$(tail -c 1 rle.py)" ]; then >&2 echo "Trailing newline alert!"; exit 1; fi
	@if [ -z "$$(tail -c 1 elr.py)" ]; then >&2 echo "Trailing newline alert!"; exit 1; fi
	@echo "Characters:"
	@cat elr.py rle.py | wc -c

data.dec: data.rle
	python elr.py < $< > $@
	@echo "$$(echo "scale=10; 100 * $$(wc -c data.rle | cut -d' ' -f1) / $$(wc -c data.dat | cut -d' ' -f1)" | bc)% compression"
	diff -s data.dec data.dat
