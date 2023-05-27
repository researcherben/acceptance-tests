
test: compare

compile:
	g++ -o hello.lex hello.cpp

run: compile
	./hello.lex > output.dat

compare: run
	diff output.dat GOLD_STANDARD.dat

# static compilation doesn't work on Mac OS X; see

compile_static:
	g++ -o hello.lex -static hello.cpp

clean:
	rm -f hello.lex output.dat

