.PHONY: build publish deps

build:
	python3 setup.py bdist_wheel

publish:
	twine upload --skip-existing dist/*

deps:
	pip3 install wheel
	pip3 install twine
