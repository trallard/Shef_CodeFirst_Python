#  Pre-course setup for Windows users

There are a few things you'll need to get set up before our first class, so that you have everything you need to get the most out of the Advanced Python Course. Chances are you'll have most of these things done already, from the Code First Girls Beginners Course.

**If you have any trouble with these tasks, please make sure you contact an instructor as soon as possible, so they can help. You'll find their email address in your welcome/acceptance email from Code First Girls.**

Things we need to do (we'll explain each of them in these notes):

1. Install Git
2. Install Python
3. Install pip
4. Install a text editor
5. Make sure you've got a GitHub account



### Install Git

We need Git to serve as our default version control tool, it will also provide a nice bash terminal that will come very handy for the course.

1. Download the Git for Windows [installer](https://git-for-windows.github.io/)
2. Run the installer and make sure you select the following options when needed:
  1. **Keep using Git from the Windows command Prompt**
  2. **Checkout windows style, commit Unix-style line endings**
  3. **Use Window's default console window**
3. If your &quot;HOME&quot; environment variable is not set (or you do not know what this is) ask one of the instructors for help

### Install Python

Python does not come pre-installed with Windows

1. Head to the Python main website ([here](https://www.python.org/downloads/windows/)) and download the latest version.
2. Make sure you choose a '2.x' version
3. Once this has been downloaded click on the **.exe** file and follow the installer instructions

### Install pip

**pip** is a package management system for installing and managing software packages (libraries) written in Python. We'll be using it to install things like Flask and any other libraries we want to make use of during this course.

A library is a collection of pre-written code we want to re-use. As an example, we don't want to re-invent or re-write a web server from scratch for each of our web projects, so instead we use a library to provide us with the functionality we want. Don't worry about what Flask is. We'll tell you all about it during the course.

**pip** comes with most of the newest Python distributions. First check if you have this installed, open the Git bash you just installed and type the following command:

`pip –V`

you should see a legend stating the version of pip you have installed and the location of this package. If you do not have pip installed go to [https://pip.pypa.io/en/stable/installing/ - do-i-need-to-install-pip](https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip) and download **get-pip.py**

Download  [get-pip.py](https://bootstrap.pypa.io/get-pip.py), being careful to save it as a .py file rather than .txt. Then, run it from the command prompt:

python get-pip.py

You possibly need an administrator command prompt to do this. Follow  [_Start a Command Prompt as an Administrator_](http://technet.microsoft.com/en-us/library/cc947813(v=ws.10).aspx) (Microsoft TechNet).

## Install a text editor

You should already have either Atom or Sublime installed on your laptop, from the beginners course.

 If you don't, head [here](https://atom.io) to get Atom and [here](https://www.sublimetext.com) for Sublime.

 To save time later on, you should add your text editor to your dock.

## Make sure you've got a GitHub account

You should have a GitHub account already, from the beginners course. If you don't have one yet, sign up for a free one [here](https://github.com).
