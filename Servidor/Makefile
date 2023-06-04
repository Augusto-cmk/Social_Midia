ifeq ($(OS), Windows_NT)
run:
	python servidor.py

install:
	pip install -r requirements.txt

build:
	python setup.py build bdist_wheel

else
run:
	python3 Main.py

install:
	pip3 install -r requirements.txt

build:
	python3 setup.py build bdist_wheel

endif