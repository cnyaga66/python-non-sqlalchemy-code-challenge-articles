class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        
        self.author = author
        self.magazine = magazine
        self.title = title

        @property
        def title(self):
            return self._title
        
        @property
        def author(self):
            return self._author
            
        @author.setter
        def author(self, author):
            if isinstance(author, Author):
                raise TypeError("Author must be of type Author")
                self._author = author
           
        @property
        def magazine(self):
            return self.magazine
            
        @magazine.setter
        def magazine(self,magazine):
            if isinstance(magazine, Magazine):
                raise TypeError("Magazine must be of type Magazine")
                self._magazine = value

               
        
class Author:
    def __init__(self, name):
     if not isinstance(name, str):
            raise ValueError("Name must be a string")
     if len(name) == 0:
            raise ValueError("Name cannot be empty")
    self.name = name

    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list ({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        if not isinstance(title, str) or not (5<= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        return Article(self, magazine, title)

    def topic_areas(self):
        mag_categories = [article.magazine.category for article in self.articles()]
        if mag_categories:
         return list(set(mag_categories))  # returns a list of unique categories
        return None 
        
class Magazine:
     all = []

     def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self.name = name
        self.category = category
        type(self).all.append(self)

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, name):
         if isinstance(value, str) and (2<= len(value) <=16):    
                self._name = name
         else:
             raise ValueError("Name must be a string between 2 and 16 characters")

        @property
        def category(self):
                return self._category
            
        @category.setter
        def category(self, category):
                if not isinstance(value, str) or len(value) == 0:
                    raise ValueError("Category must be a non-empty string")
                    self._category = category
     def articles(self):
        return [article for article in Article.all if article.magazine is self]

     def contributors(self):
        return list ({article.author for article in self.article()})

     def article_titles(self):
        titles = [article.title for article in self.articles()]
        if titles:
         return titles
        return None
     def contributing_authors(self):
        non_unique_authors = [article.author for article in self.articles()]
        if unique_contributors := list(
            {
                author
                for author in non_unique_authors
                if non_unique_authors.count(author) > 2
            }
        ):
            return unique_contributors
        else:
            None

            @classmethod
            def top_publisher(cls):
                return(
                    max(cls.all, key=lambda magazine: len(magazine.articles()))
                    if Article.all
                    else None
                )