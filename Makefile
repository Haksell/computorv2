all:
	@python computorv2.py

test:
	@pytest -rA -vv

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache

loc:
	find . -name '*.py' | sort | xargs wc -l
