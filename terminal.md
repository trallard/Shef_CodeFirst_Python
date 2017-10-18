# Basic use of the command line

Learning to use the command line is essential for advanced programming, but it can also
improve your day to day tasks.
You can access your entire computer via the command line and do everything you can normally do
using the Graphical User Interface... and more.

This (mini)tutorial will guide you through the very basics of using
the command line.

When you launch a terminal, the default path/location is your home directory, however
if at any point you are unsure which folder you are "in" (which is your working
directory) you only need to type the command `pwd`.

## Understanding the syntax
When you open the terminal you might see a *prompt* similar to:

```
username@computer ~ $
```

- The `~` character is typically shorthand for your *home directory*.  Here you being told that your *present working directory* is your home directory.
- The `$` (Ready) indicates that the prompt is ready to accept your command; the `$` is just there, you do not need to type it.

## Clear
At some point you might end up with your terminal full of lines. By typing the command `clear` you can clear the terminal screen.

## Listing the Directory contents
If within a directory you want to see its content you can use the `ls` command.

If you need more detailed information on the contents (e.g. access permissions,
date the file was last modified, etc.) you can use the command `ls -l`.

## Moving between directories
To change your working directory you need to use the `cd` command (change directory), followed by the *pathname* of the directory you want to move into e.g:

```bash
cd /HelloWorld/src/
```

If you do not specify a pathname and just type `cd`, which will take you back to your home directory.

If you want to go to the previous directory (or a directory closer to the root) you can type `cd ..`. This will take you back one directory at a time.

If you are trying to move to a directory that has spaces in the path you need to use "" to preserve the spaces: `cd "Mini tutorial"`

## Creating directories
So far we have covered how to move between existing directories, but we can just as well create directories using the command line:
`mkdir HelloWorld`
If you want to create a folder within the HelloWorld directory you just created you can do it by typing `mkdir HelloWorld/data` without the need to change directories first.

If you need to create a multiple embedded directories, instead of creating one by one you can use the `mkdir` option `-p` which will create the parent directories i.e.

```bash
mkdir -p Helloworld/data/myproject/test1/
```

## Creating files
You can create empty files using the `touch` command, for example `touch project.scala`. For this you need to be into the directory you want the file to be created, otherwise you need to specify the full path of the file:

`touch HelloWorld/data/one.txt`

You can even create multiple files at a time `touch one.txt two.txt`


## Deleting files
To permanently delete files you can use the `rm` command e.g.

```bash
rm one.txt
```

Or even delete various files at a time

```bash
rm one.txt two.txt
```

To delete *empty* directories:

```bash
rmdir dir1/an-empty-dir
```

To recursively delete directories (delete non-empty directories and their contents):

```bash
rm -r dir1/dir_with_stuff_in
```

## Copying files
You can copy files between directories by using `cp source destination` indicating the path of the file and then the path where you want the copy to be created.

## But it is too much typing...
We've got you covered! Let's say you want to go to your data directory. You can start use the autocomplete function you can start typing `cd HelloWorld/da` and then press the **Tab** key on your keyboard and the prompt will... well autocomplete the path for you.
