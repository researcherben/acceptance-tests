test: compare

apptainer_build:
	apptainer --verbose build --fakeroot centos.sif my_centos.def

apptainer_python:
	apptainer exec centos.sif python3 -c "print('hello')" > output.dat

compare: apptainer_python
	diff output.dat GOLD_STANDARD.dat


