
test:
	find test_* -maxdepth 2 -name Makefile -execdir make test \;

clean:
	find test_* -maxdepth 2 -name Makefile -execdir make clean \;
