# About

Demo of using Swagger UI for API documentation for any codebase **without library dependencies**. Here, we provide a demo using [Flask](http://flask.pocoo.org/) and Python.

Check out [my blog post](http://blog.pangyanhan.com/posts/2017-11-26-using-swagger-ui-with-any-codebase.html) for more details and explanations, especially on how to generalize this to work across different languages & frameworks.


## Docker image

To save some installation effort, you can follow the instructions in this section to build and run a Docker image that has everything you need.

The following command builds a Docker image tagged `swagger-demo`:

```
./build-docker.sh
```

To run it (you have to be in the top level of this repo):

```
./run-docker.sh
```

Then go to `http://127.0.0.1:5000/swagger-ui`.

You can modify `api-docs.yml` and refresh to see the updates.


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


## License

All files except:

- files in [/swagger-ui-dist](/swagger-ui-dist)
- the `nocache` function in [server.py](/server.py)

are under the [MIT License](/LICENSE), Copyright (c) 2017-2018 Pang Yan Han
