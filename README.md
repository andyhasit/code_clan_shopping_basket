
# Shopping Basket

A code exercise for job application to Code Clan.

## Exercise

You have been asked to model a shopping basket. We must be able to
 - Add items to the shopping basket         
 - Remove items from the shopping basket         
 - Empty the shopping basket
 -        
Additionally, we must be able to calculate the total of the shopping basket 
accounting for:

 - Buy one get one free discounts on items         
 - 10% off on totals greater than £20 (after bogof)         
 - 2% off on total (after all other discounts) for customers with loyalty          
cards

There is no requirement to create a GUI but we must be able to see the code 
running correctly.


## Installing & Running

Either download and extract the zip, or clone this repo:
```sh
$ git clone https://github.com/andyhasit/code_clan_shopping_basket
```

You can then run it with:

```sh
$ cd code_clan_shopping_basket
$ python shopping_basket
```
The program is written in Python 2.7, it may run on other versions, but that's not been tested.


## Running the tests

The tests are written with [pytest](http://pytest.org/latest/contents.html) which you will need to install if you want to run the tests:

```sh
$ pip install pytest -U
```
You may experience problems (in particular with it not finding the colorama lib) which you can usually fix by upgrading **pip** first:

```sh
$ easy_install --upgrade pip
```

You can then run the tests with:

```sh
$ cd code_clan_shopping_basket
$ py.test
```

## Decision

Here's some decisions I made and why:

 - I decided against using [venv](https://docs.python.org/3/library/venv.html), as you may not by a Pythony person and it would just cause extra grief when all you want to do is check my code.
 - I used [argparse](https://docs.python.org/3/library/argparse.html) instead of better alternatives because I want to avoid dependencies that might stop you running the app.
 - I used [pytest](http://pytest.org/latest/contents.html) because I find it better than Python's default unittest, although this is a depencency which you might stop you being able to run the tests, but not the app.
 - I put the test files in the same directory as the source files. That makes things easier for a project this size (plus thanks to naming convention you can immediately see if any source file doesn't have a test counterpart!)

## Documentation

I put my comments and explanations in the source code instead of in here, to avoid you jumping back and forth.
