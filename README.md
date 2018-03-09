# jubilant-potato

## News API

#### Installation

In order to get this project running, you need to have python and pip running.

+ Install virtualenv using pip 

	+ `sudo pip install virtualenv`

+ At the project root directory run 

	+ `virtualenv env`

	+ `source env/bin/activate`

+ Then Install all the requirements for the project using 

	+ `bash pip install -r requirements.txt`

+ Now you can run this application using 

	+ `python headlines.py`

#### API Documentation

* `"/"` -> will give you all the available publications in a list.

* `"/pub"` -> will give you all the news headlines from the publication.

* `"/pub/article_num"` -> will give you the news details for the requested news article.


##### TODO

- [x] Option to select publications dynamically.
- [x] Get full news article details.
- [ ] Unittest all the methods.
- [ ] Respond with HTTP error codes when the request contains errors.

