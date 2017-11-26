# About

Demo of using swagger-ui for any codebase without library dependencies. Here, we make use of [Flask](http://flask.pocoo.org/) and Python.

For more details, such as generalizing this to work across different languages & frameworks, please check out my blog post.


## Requirements

- [pyenv](https://github.com/pyenv/pyenv)
- [npm](https://github.com/creationix/nvm)

Install any version of Python 3.x using pyenv and nodejs 8.x using nvm. Details using concrete examples below.


## Installation Instructions

For pyenv and npm, follow the instructions on their GitHub READMEs.


### Install Python 3.6.3 using pyenv

```
pyenv install 3.6.3
```

### Create virtualenv for this demo

```
pyenv virtualenv 3.6.3 swagger-demo
```

### Install Flask

```
pyenv activate swagger-demo
pip install -r requirements.txt
```


## Running

```
pyenv activate swagger-demo
python server.py
```

Go to http://127.0.0.1:5000/swagger-ui to see the swagger ui. Update [api-docs.yml](/api-docs.yml) and refresh to see the changes
