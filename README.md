# Phase 3 -WK3 - Code Challenge: Articles - with database

In this code challenge, you will be working with a Magazine domain.

We have three models: `Author`, `Article`, and `Magazine`.

For our purposes, an `Author` has many `Article`s, a `Magazine` has many
`Article`s, and `Article`s belong to both `Author` and `Magazine`.

`Author` - `Magazine` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Set Instructions

To get started, while inside of this directory.
  - run `pipenv install` 
  - run `pipenv shell` to jump into the shell. 
  - run `python3 app.py` to create the database

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

<!-- **Remember!** This code challenge has tests to help you check your work. You can
run `pytest` to make sure your code is functional before submitting. -->

The folder structure is as follows:

1. On the root folder, we have created the main file and named app.py. make use of it to test your code. You re expected to add more code to test your own implementation.

2. Still on the root path, we have the following folders:
    - database: Here the most important files are the setup.y where you are expected to write your queries to crate the database. in the same folder, there is another file called connection.py where we have proivded the connection string for your database
    - models: Here we have created 3 files Article.py, Author.py and Magazine.py wehere you are expected to implement your CRUD methods to interact with the database
    - tests: Here we have provided few tests to guide you with you own tests

You can add code to the `/app.py` file to define variables and create
sample instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Core Deliverables

Write the following methods in the models(Article, Author, magazine) provided in the models folder. Feel free to build out any helper methods if needed.

### Initializers and Properties

#### Author

- `Author __init__(self, id, name)`
  - Author is initialized with a name
  - This initialization should create a new entry in the database `authors` table
- `Author property id`
  - Returns the id of the newly created `Author`
  - Names must be of type `int`
  - Remember to use the setter and getter method for easy retrieval, since this will be needed when creating `articles`
- `Author property name`
  - Returns the author's name
  - The value of the name property should derive from the database `authors`. You should makes use of getters and setters methods to manipulate this property.
  - Names must be of type `str`
  - Names must be longer than 0 characters
  - Should **not be able** to change after the author is instantiated.
  - _hint: hasattr()_

#### Magazine

- `Magazine __init__(self, id, name, category)`
  - A magazine is initialized with a name and a category
  - This initialization should create a new entry in the database `magazines` table 
- `Magazine property id`
  - Returns the id of the newly created `Magazine`
  - id must be of type `int`
  - Remember to use the setter and getter method for easy retrieval, since this will be needed when creating `articles`
- `Magazine property name`
  - Returns the magazine's name
  - The value of the name property should derive from the database `magazines`. You should makes use of getters and setters methods to manipulate this property.
  - Names must be of type `str`
  - Names must be between 2 and 16 characters, inclusive
  - Should **be able** to change after the magazine is instantiated.
- `Magazine property category`
  - Returns the magazine's category
  - The value of the category property should derive from the database `magazines`. You should makes use of getters and setters methods to manipulate this property.
  - Categories must be of type `str`
  - Categories must be longer than 0 characters
  - Should **be able** to change after the magazine is instantiated.

#### Article

- `Article __init__(self, author, magazine, title)`
  - Article is initialized with an `Author` instance, a `Magazine` instance, and a title. 

  NB: Creating a new entry in the `article` table requires the author and magazine PKs(Primary Keys) as FKs(Foreign Keys). Find a way to retrive the author and maagzine id properties from their respective models then use them here
  - The initialization should create a new entry in the database `articles` table
- `Article property title`
  - Returns the article's title
  - Titles must be of type `str`
  - Titles must be between 5 and 50 characters, inclusive
  - Should **not be able** to change after the article is instantiated.
  - _hint: hasattr()_

### Object Relationship Methods and Properties

#### Article

- `Article property author`
  - Write a method in the Article model that returns the author of the article.
  - You can make use of the SQL JOINS to achieve this

- `Article property magazine`:
   - Write a method in the Article model that returns the magazine of the article.
  - You can make use of the SQL JOINS to achieve this

#### Author

- `Author articles()`
  - Write a method called articles() in the Author model that will return all articles associated with an author
  - Remember to make use of the SQL JOINS concept to achieve this
- `Author magazines()`
  - Write a method called magazines() in the Author model that will return all magazines associated with an author
  - Remember to make use of the SQL JOINS concept to achieve this

#### Magazine

- `Magazine articles()`
  - Write a method called articles() in the Magazine model that will return all articles associated with a Magazine
  - Remember to make use of the SQL JOINS concept to achieve this

- `Magazine contributors()`
  - Write a method called contributors() in the Magazine model that will return all Authors associated with a magazine
  - Remember to make use of the SQL JOINS concept to achieve this

### Aggregate and Association Methods

#### Magazine

- `Magazine article_titles()`
  - Write a article_titles() method in the magazine model that returns a list of the titles strings of all articles written for that magazine
  - Returns `None` if the magazine has no articles
- `Magazine contributing_authors()`
  - Write a contributing_authors() in the Magazine model that returns a list of authors who have written more than 2 articles for the magazine
  - Authors must be of type `Author`
  - Returns `None` if the magazine has no authors with more than 2 publications




