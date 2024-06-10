from database.connection import get_db_connection
from database.setup import create_tables
from models.author import Author
from models.magazine import Magazine
conn = get_db_connection()
cursor= conn.cursor()

class Article:
    all ={}
    def __init__(self, id, title, content, author, magazine):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.magazine = magazine
        self.author_id = author.id()
        self.magazine_id = magazine.id()
        self.save()

    def __repr__(self):
        return f'<Article {self.title}>'


    def save(self):
        sql= '''
        INSERT INTO article(title,content,author_id,magazine_id)  VALUES(?,?,?,?)
            '''
        cursor.execute(sql,(self.title,self.content,self.author_id,self.magazine_id))
        conn.commit()
        self.id = cursor.lastrowid  
        type(self).all[self.id] = self
    @property
    def author(self):
        sql ='''
            SELECT authors.id , authors.name
            FROM articles
            JOIN authors ON authors.id = articles.author_id
            WHERE article.id = ?                    
        '''
        cursor.execute(sql,(self.id,))
        author_row = cursor.fetchone()
        if author_row:
            author_id, author_name = author_row
            return Author(author_id, author_name)
        else:
            return None
        
    @property
    def magazine(self):
        sql='''
            SELECT magazines.id, magazines.name, magazines.category
            FROM articles
            JOIN magazines ON magazines.id = articles.magazine_id
            WHERE article.id = ?
        '''
        cursor.execute(sql, (self.id,))
        magazine_row = cursor.fetchone()
        if magazine_row:
            magazine_id, magazine_name, magazine_category = magazine_row
            return Magazine(magazine_id, magazine_name, magazine_category)
        else:
            return None
        