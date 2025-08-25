---
# Documentation: [Managing content | Academic](https://sourcethemes.com/academic/docs/managing-content/)

title: "Modelling, Simulation and Control of Hydro-Power System - Part 6"
subtitle: "Packing the code in a python library"
summary: "In this series I will show the entire process of developing a model, performing simulations and the use of different control techniques for decision support in flood management systems."
authors: []
tags: ["Flood Forecasting", "Model Predictive Control"]
categories: ["Flood Management"]
date: 2022-02-06T10:01:00
lastmod: 2022-02-06T10:01:00
featured: false
draft: false

# Featured image

# To use, add an image named `featured.jpg/png` to your page's folder.

# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.

image:
 caption: "Image by <a href='https://pixabay.com/users/russmac-756431/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=929406'>Russ McElroy</a> from <a href='https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=929406'>Pixabay</a>"
 focal_point: "Smart"
 preview_only: false

# Projects (optional).

# Associate this post with one or more of your projects.

# Simply enter your project's folder or file name without extension.

# E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.

# Otherwise, set `projects = []`.

projects: ["Modelling, Simulation and Control of Hydro-power system"]
---
# Table of Contents

+ [Part 1 - System description]({{<  relref "../01"  >}})
+ [Part 2 - Theoretical model of the lakes]({{<  relref "../02"  >}})
+ [Part 3 - Theoretical model of the reaches]({{<  relref "../03"  >}})
+ [Part 4 - Implementing the model of lakes using DAE approach with Python]({{<  relref "../04"  >}})
+ [Part 5 - Improving the DAE approach using OOP with Python]({{<  relref "../05"  >}})
+ [Part 6 - Packing the code in a python library]({{<  relref "../06"  >}})
+ [Part 7 - Model of lakes, ducts, pumps and turbines]({{<  relref "../07"  >}})

# Overview

If you have gone through all the other posts I have written in this series, you may have noticed that a bunch of reusable code was written and all this code can and should be used along the rest of the process. To do so in an organized and efficient way, I thought about packing it all together in a Python library. The name I chose is: **Cacao**! Why? No specific reason, I had other ideas but they were already taken by someone else who made another library with the same name. As Python libraries must have a unique name, **cacao** is a name which is simple, easy to remember, with meaning (not made-up word) and it wasn't already taken at the time I released the first version.

If you want to go and check the latest version of this library, you can go to the [Github repository](https://github.com/euanrussano/cacao). Or if you just want to test it locally, you can type in the console:

```
pip install cacao
```
You can also check the library Pypi page [here](https://pypi.org/project/cacao/).

I've made some changes on the code since the last post to make it more concise and intuitive. To make it as an actual Python library which someone can easily install just by typing `pip install cacao` I've gone through the process described [here](https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14). This is an amazing post, which describes in lots of details how to properly setup and give a kickstart to your own Python library. So I will just summarize the process here.

## Write and organize your Python code.

All the code that belongs to the library should stay in a folder with the same name of the library. Normally, this folder is inside another source which contains the whole project, and this can take whatever name. For example:

```
project folder: cacao_project
library folder: cacao_project/cacao
```
And then you may add other folder in the project regarding documentation, examples, tests, readme file, etc...

```
cacao_project
|-- cacao
|   |-- __init__.py
|   |-- cacao_submodule1
|   |   |-- __init__.py
|   |   |-- some_python_code.py
|   |-- cacao_submodule2
|   |   |-- __init__.py
|   |-- ...
|-- docs
|   |-- make
|   |-- ...
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- setup.py
|-- tests
|   |-- test1.py
```

## Write some tests and run them

This step is necessary to make sure that your code works. If you use the `unitest` module to write the tests, then you can run them by typing in the console:

```
python -m unittest -v tests/test1.py
```

## Write the README.md, requirements.txt and setup.py files

These are very important files to keep together with your project. However, setup.py is the essential one so people can install the library using pip. You can use as an example the one I have in the [cacao project](https://github.com/euanrussano/cacao) or the one from the [Bienvenu's medium post](https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14).

README.md file will provide some very basic documentation and quickstart tips for people using your library. The content of this file is rendered at the top-level of the library in the Github repository.

The file requirements.txt makes a compilation of all the dependencies (external libraries) that your library depends on. There are different ways of generating it. The two most common are:
+ using pip: `pip freeze > requirements. txt`
+ using pipenv(when you have a virtual environment managed by pipenv): `pipenv lock -r > requirements.txt`

## Install the required dependencies to publish the library

```
pip install wheel
pip install twine
```

### Compile the library

Type in the console (from the project directory):

```
python setup.py sdist bdist_wheel
```

This command will generate several folders and files. They can be deleted later, after they've been sent to Pypi. The two main folder are `dist` and `build`. `dist` contains the packaged version of the library.

### Check the build

The following command makes sure that the build was done properly, without mistakes.

```
twine check dist/*
```

It should output 2 lines saying **PASSED**. When this happens then we are ready to publish the library to Pypi.

### Upload to Pypi

Before uploading to "real" Pypi, it is often useful to make sure that everything is ok by uploading to TestPypi, which is a platform almost exactly equal to Pypi but used to generate a testing version of the library, so you can double check it and make sure that all is according expected. If not, make the changes and upload again until you have everything properly working.

First, create an account in [testPypi](https://test.pypi.org/) and [Pypi](https://pypi.org/) if you do not already have.
To upload to testPypi, type in the console:

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Check the webpage. Make sure everything is as expected. If yes, then you are ready to upload the library to Pypi.

```
twine upload dist/*
```

### Upload to Github

To make the code of the library available for others, upload the project folder to Github. To do so, first create a new repository in Github. Suppose the name of the repository is `my_repository`. Then in the console you have to initialize (`git init`) the repository locally, then add the files (`git add .`), commit them (`git commit -m "my first commit"`) and push it (`git push`). The commands to be types in the console are:

```
git init
git remote add origin <url of the github repository>
git add .
git commit -m "my commit message goes here"
git push -u origin master
```

Once this is done, your project should be available in Github, and the library available in Pypi for anyone install it using `pip install`. 

# Conclusion

The article from [Bienvenu](https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14) goes much deeper in the whole process of puslishing your python library, also explaining how to setup documentation and to host it in readthedocs. I encourage you to visit this article if you are interested in creating your own Python library. Thanks for reading and I see you in the next post.
