# Python library tutorial

Tutorial for creating a python library called `hello-universe`.

Structure your python code in a way this repository is structured.

Publish it as a GitHub repository.

Now it can be installed as a python library via `pip install` and used as a python library with `import`.

## Install

Install via

```bash
$ pip install git+https://github.com/sagitta42/tutorial-python-library
```

## Usage

Import:

```python
import hello_universe
```
or
```
from hello_universe import is_answer, hello_world
```

Check whether a number is the answer to the question of life, universe, and everything:

```python
from hello_universe import is_answer

is_answer(43)
```

Print hello world:
```python
from hello_universe import hello_world

hello_world()
```

