PYTHON = python3
RM_THESE = ./*.txt ./__pycache__

target:
	chmod u+x ./*.py

clean:
	rm -f $(RM_THESE)

