

test: compare

run:
	python3 hello.py > output.dat

compare: run
	diff output.dat GOLD_STANDARD.dat

clean:
	rm -f output.dat

