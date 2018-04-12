# Dar

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI](https://img.shields.io/pypi/v/dar.svg)](https://pypi.org/p/dar)
[![Travis CI Build](https://img.shields.io/travis/alanbato/dar.svg)](https://travis-ci.org/alanbato/dar)
[![Documentation Status](https://readthedocs.org/projects/dar/badge/?version=latest)](https://dar.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/alanbato/dar/shield.svg)](https://pyup.io/repos/github/alanbato/dar/)

> "Dar es mejor que recibir." - Anónimo

_Dar_ is a command line toolbelt for managing different project workflows.

Why is it a toolbelt? Because _Dar_ is not a tool that can be used _by itself_, but a place to store all the commands you use in a given project. _Dar_ remembers the workflows across all the different projects you contribute to so you don't have to.

It is important to note that dar is **user focused**. The user is the one that registers and uses the commands to their own preference. Projects do not need to adopt dar for contributors of that project to benefit from it. 

## Getting Started

These instructions will help you get started with _Dar_ so you can use it to manage your projects. 

### Installing

To install _Dar_ you need to have Python 3.6 or higher and pip.
Then you install it with:

```
$ pip install dar
```

Although _Dar_ is written in Python, it is language agnostic and can be used in _virtually_ any project. 

### Usage

The main _Dar_ commands are `register` and `run`.
First, let's register an alias with `dar register <alias> <command>`:

```
$ dar register greet echo "Hola mundo!"
```

This creates a `.darconfig` file in the root directory or adds the alias to it if one already exists.
For example, this is the content of the file generated by the command above:
```
[greet]
echo "Hola mundo!"
```

Then, you can call that command by running `dar run <alias>`:

```
$ dar run greet
Running: echo "Hola mundo!"
Hola mundo!
```

And that's it! You can register and run any commands you like and and they will be stored in the project's `.darconfig`.

Alternatively, you can edit the `.darconfig` directly to register aliases. This is helpful when you want to run multiple commands under a single alias.
Example:
```
[restartdocker]
sudo systemctl daemon-reload
sudo systemctl restart docker
```

## Built With

* [Click](http://click.pocoo.org/) - For the command line interface.
* The `subprocess` and `configparser` built-in modules.

### Developtment Tools

* [Pytest](https://docs.pytest.org/) - For painless testing.
* [Black](https://github.com/ambv/black) - Uncompromising code formatting.

## Running the tests

You can use _Dar_ to run its own tests by running:

```
$ dar run tests
```


## Contributing

Please read [CONTRIBUTING.md](https://github.com/alanbato/dar/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Alan Velasco** - *Initial work*

See also the list of [contributors](https://github.com/alanbato/dar/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
