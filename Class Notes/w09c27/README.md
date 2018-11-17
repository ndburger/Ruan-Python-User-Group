# w09c27

In this class we begin to look at another way to work with python, iPython and Jupyter.

The goal for this class is simply to get you up an running with Jupyter.

## Jupyter introduction

### iPython and Jupyter

#### iPython
Is a command shell for interactive python programming. It presents a more user-friendly interactive framework that the standard command line.

iPython evolved from command line interface to a fully fledged interactive development environment.

https://en.wikipedia.org/wiki/IPython

#### Project Jupyter

Jupyter is a spin-off project of IPython. Within jupyter, IPython is one of the many kernels for Jupyter. Jupyter attempts to provide a language agnostic language-agnostic iPython notebook interface that supports many different languages (i.e. Julia, R, Haskell and Ruby).

## Jupyter Installation

There exist specialized distributions of Python that focus on support for Jupyter, iPython and data analysis (i.e. Anaconda). One of the pros of such distributions is that many common libraries for data analysis are already included (some of which are difficult to install within the standard python distribution). The cons include that these distros can also involve managing a separate package distribution and installation system (conda). To keep this simple, in this course we will be - and are using - the standard python distribution.

The instructions below apply only to the standard python distribution.

__Now, let's install Jupyter__

```
$ pip install jupyter
```

## Install Numpy, Scipy, Pandas, and Bokeh

__NOTE: These instructions are for Windows only....__

There are a few modules that we will commonly use when working with data in Jupyter -- Numpy, Scipy, Pandas, and Bokeh.

Many of these packages are distributed in C and require you to compile the code for your local machine.

We will not be compiling code for our local machine. Instead (as I mentioned a while back when introducing packages) you can often find pre-build binaries available as "wheel files") we will download pre-built binaries from http://www.lfd.uci.edu/~gohlke/pythonlibs/

Go to [this](http://www.lfd.uci.edu/~gohlke/pythonlibs/) site and download Numpy for your platform. You will need to download the correct whl file for your version of python (you should be running 3.5) and operating system (most are now 64bit). Download this file to a known location. You will now install this using the pip for your virtual environment.

For 64bit windows...

```
numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl
```

And install...
```
pip install numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl
```

For 32bit windows...

```
numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl
```

And install...
```
pip install numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl
```




>__NOTE__: From hereon, I should the 64bit versions. If your Windows is 32 bit, be sure to download the appropriate whl fil for 32 bit.

....

Now, download SciPy

```
scipy-0.18.1-cp35-cp35m-win_amd64.whl
```

... and install.

```
pip install scipy-0.18.1-cp35-cp35m-win_amd64.whl
```

You'll also need to do this for Pandas.

Download
```
pandas-0.19.0-cp35-cp35m-win_amd64.whl
```

And install...
```
pip install pandas-0.19.0-cp35-cp35m-win_amd64.whl
```

And, finally (at least for now) we'll also need to get the Bokeh library. This is easy to install, as it's available on PiPI.

```
pip install bokeh
```

## using jupyter notebook

Jupyter is great for exploratory data analysis.

Start jupyter

```
jupyter notebook
```

Enter python code in a cell. When you want to run the code in a cell press control enter. If you want to create a new cell, alt-enter. Shift-enter will both run the code and start a new cell.

You have two modes -- command mode (grey rectangle around the cell).  edit mode (focus on current cell). (cell is green around the cell).

In edit mode you can insert in the cell.

TO delete a cell, hit escape and enter DD.

Got to help to see the other shortcuts (and introduction to Jupyter).




## Appendix:

Useful resources:

* https://github.com/wesm/pydata-book
* http://nbviewer.jupyter.org/
