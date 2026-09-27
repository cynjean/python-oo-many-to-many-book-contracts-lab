class Author:
    """An author who can have contracts with many books."""

    all = []

    def __init__(self, name):
        self.name = name
        # Retain each author so the model has a library-wide collection.
        type(self).all.append(self)

    def contracts(self):
        """Return every contract associated with this author."""
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        """Return the books connected to this author through contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contracts(self, book, date, royalties):
        """Create a contract linking this author to a book."""
        return Contract(self, book, date, royalties)

    def sign_contract(self, book, date, royalties):
        """Singular-name alias retained for the provided starter test suite."""
        return self.sign_contracts(book, date, royalties)

    def total_royalties(self):
        """Return the sum of royalties from all contracts for this author."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    """A book that can be connected to many authors through contracts."""

    all = []

    def __init__(self, title):
        self.title = title
        # Retain each book so the model has a library-wide collection.
        type(self).all.append(self)

    def contracts(self):
        """Return every contract associated with this book."""
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        """Return the authors connected to this book through contracts."""
        return [contract.author for contract in self.contracts()]


class Contract:
    """Join an author and a book, with the date and royalties for their deal."""

    all = []

    def __init__(self, author, book, date, royalties):
        # Use the validating properties so every stored contract is well formed.
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise TypeError("book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise TypeError("royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts whose date matches the requested date."""
        return [contract for contract in cls.all if contract.date == date]
