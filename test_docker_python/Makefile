
test: compare


docker_build:
	docker build --tag test_py .

docker_hello: docker_build
	docker run -it --rm test_py python3 -c "print('hello')"  > output.dat

compare: docker_hello
	diff output.dat GOLD_STANDARD.dat

docker_run_interactive_terminal:
	docker run -it --rm test_py

clean:
	rm -f output.dat

