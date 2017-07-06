[![Patrick Luboobi](https://img.shields.io/badge/Patrick%20Luboobi-Andela--SLC--Day--4-green.svg)
[![Build Status](https://travis-ci.org/patlub/Andela-SLC-Day-4.svg?branch=master)](https://travis-ci.org/patlub/Andela-SLC-Day-4)
[![Coverage Status](https://coveralls.io/repos/github/patlub/Andela-SLC-Day-4/badge.svg)](https://coveralls.io/github/patlub/Andela-SLC-Day-4)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


# Getting Started

###### You can start by cloning the project:
`git clone https://github.com/patlub/Andel-SLC-Day-4.git`


## Prerequisites
Working installation of python 3. if you don't, you can refer to this
[Install Python 3](https://www.python.org/downloads/)

# Usage
## Binary Search
#### Searches list using binary search
import it first:

`from BinarySearch.binary_search import binary search`

then create an obj and call the search method, for example:

It takes 2 arguments, the step and length of list to search

`bs = BinarySearch(100, 10)`

`bs.search(40)` will return `{'count' : 7, 'index' : 3}`

## Find Missing
#### Finds missing number from two lists

`from FindMissing.find_missing import find_missing`

`fing_missing([1, 2, 3], [1, 2, 3, 4])` returns  `4`

## Recreation of Google HomePage

Navigate to the HTML_CSS_google directory and open index.html in browser

# Running the Tests

### Binary Search
Navigate into BinarySearch directory

And run`python test_binary_search.py`

You should see:

`All 3 tests passed`

### FindMissing
Navigate into FindMissing directory

And run `python test_find_missing.py`

You should see:

`All 6 tests passed`

# Enjoy.