#!/usr/bin/env python3
from book import Book
from pandas import pd
def main():
	book = Book("TEST")
	book.insert_buy(10, 10.0)
	book.insert_sell(120, 12.0)
	book.insert_buy(5, 10.0)
	book.insert_buy(2, 11.0)
	book.insert_sell(1, 10.0)
	book.insert_sell(10, 10.0)
	return book
if __name__ == "__main__":
	book=main()




'''def main():
      book = Book("TEST")
      boo=[]
       
      book.insert_buy(10, 10.0)
      book.insert_sell(120, 12.0)
      book.insert_buy(5, 10.0)
      book.insert_buy(2, 11.0)
      book.insert_sell(1, 10.0)
      book.insert_sell(10, 10.0)
      for i in book.orders:
           
           boo.append(i)
      return boo
if __name__ == "__main__":
        book=main()
        len(book)
        """dic={'buy':[],'sell':[]}
        for i in book:
            if i[0]=='B':
                dic['buy'].append(book[i])
            else:
                
             dic['sell'].append(book[i])
        data=pd.DataFrame[dic]
        data'''
