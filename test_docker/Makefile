
test: compare


docker_version:
	docker --version > output.dat

compare: docker_version
	diff output.dat GOLD_STANDARD.dat

clean:
	rm -f output.dat
