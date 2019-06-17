.PHONY: default

SHELL = bash

default:
	@make -B data.dec

data.dat: make_data.py
	python make_data.py > $@.tmp
	cat make_data.py $@.tmp rle.py > $@
	rm $@.tmp

data.rle: data.dat
	python rle.py < $< > $@

data.dec: data.rle
	python rle.py -d < $< > $@
	@echo "$$(echo "scale=10; 100 * $$(wc -c data.rle | cut -d' ' -f1) / $$(wc -c data.dat | cut -d' ' -f1)" | bc)% compression"
	diff -s data.dec data.dat
