all: prepare upload clear
prepare:
	python setup.py sdist
	python setup.py bdist_wheel
upload:
	twine upload dist/*
clear:
	rm dist/*
