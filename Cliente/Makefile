ifeq ($(OS), Windows_NT)
run:
	python Main.py

install:
	pip install -r requirements.txt

build:
	python setup.py build bdist_wheel

else
run:
	python3 Main.py

install:
	sudo apt-get install python3-tk
	pip3 install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

endif