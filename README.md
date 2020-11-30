# fuzzing_python_example
A very simple example using AFL

## Install AFL
https://lcamtuf.coredump.cx/afl/

On MacOS:
```
brew install afl-fuzz
```

## Install Python requirements
https://github.com/jwilk/python-afl

```
pip install -r requirements.txt
```

## Running the example
```
py-afl-fuzz -m 400 -i initial-inputs/ -o fuzzing-results/ -- python fuzz.py
```

* The example inputs are in the initial-inputs folder
* The results are written to fuzzing-results
