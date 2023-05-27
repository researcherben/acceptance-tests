

test: compare

version:
	podman --version > output.dat

compare: version
	diff output.dat GOLD_STANDARD.dat

clean:
	rm -f output.dat
