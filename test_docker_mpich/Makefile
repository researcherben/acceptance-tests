
test: compare

docker_build:
	docker build --tag test_mpi .

docker_hello: docker_build
	docker run -it --rm test_mpi

compare: docker_hello
	diff output.dat GOLD_STANDARD.dat

docker_run_interactive_terminal:
	docker run -it --rm test_mpi

clean:
	rm -f output.dat

