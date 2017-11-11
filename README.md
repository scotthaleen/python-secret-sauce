# Python Secret Sauce

A collection of functions I use as the base for most projects.



## Prerequisites

## Install

```
$ pip install .
```

## Build

```
$ python setup.py build
```

## Tests

```
tox
```


## Generate Documentation
Install `sphinx` and `sphinx_rtd_theme` packages:
```
$ pip install sphinx sphinx_rtd_theme
```

Build HTML docs:
```
$ make docs
```

or:
```
$ python setup.py build_sphinx
```

Documentation will be generated in `docs/_build/`.
