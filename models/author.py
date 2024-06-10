from database.connection import get_db_connection
from database.setup import create_tables
from models.magazine import Magazine
from models.article import Article
conn = get_db_connection()
cursor= conn.cursor()

class Author:
    all ={}
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.save() 

    def __repr__(self):
        return f'<Author {self.name}>'
    @property
    def id(self):
        if not hasattr(self, '_id'):
            sql = '''
                SELECT id FROM authors WHERE name = ?
            '''
            cursor.execute(sql,(self.name,))
            row = cursor.fetchone()
            if row:
                self._id = row[0]
        return self._id
    @id.setter
    def id(self,value):
        
        if isinstance(value,int):
            self._id =value

        else: raise ValueError("ID MUST BE OF TYPE INT")
    
    @property
    def name(self):
        if  self._name is None and self.id is not None:
            sql = '''
                SELECT name FROM authors WHERE id = ?
            '''
            cursor.execute(sql,(self.id,))
            row = cursor.fetchone()
            if row :
                self._name = row[0]
        return self._name
    @name.setter
    def name(self,value):
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change the author's name after it is set")
        
        if isinstance(value, str) and len(value)>0:
            self._name = value
        else: raise ValueError("NAME MUST BE A NON-EMPTY STRING ")
    def _retrieve_from_db(self, id):
        sql = '''
            SELECT id, name FROM authors WHERE id = ?
        '''
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        if row:
            self.id = row[0]
            self.name = row[1]
            type(self).all[self.id] = self
        else:
            raise ValueError("Author with given ID does not exist")

    def save(self):

        sql='''
            INSERT INTO authors (name) VALUES (?)
        '''
        cursor.execute(sql,(self.name))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls,name):
        author= cls(name)
        author.save()
        return author
    
    
    def author(self):
        sql = '''
            SELECT  articles.title, articles.content, articles.author_id,articles.magazine_id
            FROM authors
            JOIN articles ON authors.id = articles.authors_id
            WHERE  author.id = ?
        '''
        cursor.execute(sql,(self.id,))
        article_row = cursor.fetchone()
        if article_row:
            article_title, article_content, article_author_id,article_magazine_id = article_row
            return Article(article_title, article_content, article_author_id,article_magazine_id)
        else:
            return None


    def magazine(self):
        sql = '''
            SELECT  magazines.id, magazines.name, magazines.category
            FROM articles
            JOIN magazines ON articles.magazine_id = magazine.id
            WHERE  articles.author_id = ?
        '''
        cursor.execute(sql, (self.id,))
        magazine_rows = cursor.fetchall()
        magazines = []
        for row in magazine_rows:
            magazine_id, magazine_name, magazine_category = row
            magazines.append(Magazine(magazine_id, magazine_name, magazine_category))
        return magazines