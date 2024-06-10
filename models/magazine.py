from database.connection import get_db_connection
from database.setup import create_tables
from models.article import Article
from models.author import Author

conn = get_db_connection()
cursor= conn.cursor()
class Magazine:
    all={}
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.save()

    def __repr__(self):
        return f'<Magazine {self.name}>'


    def save(self):

        sql='''
            INSERT INTO magazines (name,category) VALUES (?,?)
        '''
        cursor.execute(sql,(self.name,self.category))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls,name):
        author= cls(name)
        author.save()
        return author
    @property
    def id(self):
        if not hasattr(self, '_id'):
            sql = "SELECT id FROM magazines WHERE name = ? AND category = ?"
            cursor.execute(sql, (self.name, self.category))
            row = cursor.fetchone()
            if row:
                self._id = row[0]
        return self._id

    
    @id.setter
    def id (self,value):
        if value is not None  and not isinstance(value, int):
            raise ValueError ("ID must be of type int")
        else: self._id =ValueError

    @property
    def name(self):
        if self._name is None and self.id is not None:
            sql = "SELECT name FROM magazines WHERE id = ?"
            cursor.execute(sql, (self.id,))
            row = cursor.fetchone()
            if row:
                self._name = row[0]
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value, str) and 2 <= len(value) <=16:
            self._name = value

        else: raise ValueError("NAME MUST BE A STRING BETWEEN 2 AND 16 CHARACTERS")
    @property
    def category(self):
        if self.category is None and self.id is not None:
            sql="SELECT category FROM magazines where id = ?"
            cursor.execute(sql, (self.id,))
            row = cursor.fetchone()
            if row:
                self._category= row[0]
        return self._category
    @category.setter
    def category(self,value):
        if isinstance (value , str) and len(value) > 0:
            self._category = value
        else: raise ValueError("NAME MUST BE A NON-EMPTY STRING")  

    def articles(self):
        sql ='''
            SELECT articles.title, articles.content, articles.author_id,articles.magazine_id
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        ''' 
        cursor.execute(sql,(self.id,))
        article_rows = cursor.fetchall()
        articles =[]
        for row in article_rows:
            article_id, title, content, author_id, magazine_id = row
            articles.append(Article(article_id, title, content, Author(author_id), self))
        return articles
    def contributors(self):
        sql = '''
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        '''
        cursor.execute(sql, (self.id,))
        author_rows = cursor.fetchall()
        contributors = []
        for row in author_rows:
            author_id, author_name = row
            contributors.append(Author(author_id, author_name))
        return contributors
    def article_titles(self):
        sql = '''
            SELECT articles.title
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        '''
        cursor.execute(sql, (self.id,))
        titles = [row[0] for row in cursor.fetchall()]
        return titles if titles else None

    def contributing_authors(self):
        sql = '''
            SELECT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
        '''
        cursor.execute(sql, (self.id,))
        author_rows = cursor.fetchall()
        if not author_rows:
            return None

        contributing_authors = [Author(author_id, author_name) for author_id, author_name in author_rows]
        return contributing_authors
 