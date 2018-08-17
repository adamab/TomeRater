from TomeRater import *

print("Creating Users")
user1 = User("Beatriz Rodriguez", "Bella@last.org")
user2 = User("Xiomei Li", "li@test.edu")
user3 = User("Beatriz Rodriguez", "Bella@last.org")
user4 = User("Jenny Parque", "jenny.from#theblock.org")
user5 = User("Pat Patterson", "pat@pat.pat")

print("Creating Books")
book1 = Book("The Book", 123789, 14)
book2 = Book("That Book", 123908, 23)
book3 = Book("This Book", 123809, 13)
book4 = Book("This Book", 123809, 13)
book5 = Book("Harvey Book", 123999, 22)

print("Creating Fictions")
fiction1 = Fiction("Untruth", 122345, "Jim Crowed", 90)
fiction2 = Fiction("Half Truth", 122456, "William T. Conker", 23)
fiction3 = Fiction("Look Over There", 122980, "Jefferson Jeffries", 54)
fiction4 = Fiction("Watch My Hand", 122999, "Nancy P. Magcian", 657)
fiction5 = Fiction("Watch My Hand", 122999, "Umaq Umaqraq", 34500)

print("Creating Non_Fiction")
non_fiction1 = Non_Fiction("Python for Dummies", 111999, "Beginner", "Programming", 22.9)
non_fiction2 = Non_Fiction("Python Cookbook", 111998, "Beginner", "Programming", 22.9)
non_fiction3 = Non_Fiction("Python for Dummies", 111999, "Advanced", "Snakes", 35)

print("Creating TomeRaters")
tomerater1 = TomeRater()
tomerater2 = TomeRater()
tomerater3 = TomeRater()
tomerater4 = TomeRater()

print("Creating TomeRaterBook")
tomeraterbook1 = tomerater1.create_book("That Book", 123908, 13)

print("Creating TomeRaterNovel")
tomeraternovel1 = tomerater1.create_novel("Untruth", 123908, "Jim Crowed", 90)

print("Creating TomerRaterNon_Fiction")
tomeraternon_fiction1 = tomerater1.create_non_fiction("Python for Dummies", 111999, "Beginner", "Programming", 22.9)

print("Begin users testing\n")
print("Testing user1 instance: Beatriz Rodriguez, Bella@last.org")
print(user1.name, user1.email, user1.books, sep=" , ")
print(user1)
print("Testing equality of user1 and user2: False")
user1 == user2
print("Testing equality of user1 and user3: True")
user1 == user3
print("Testing get_email user1: Beatriz Rodriguez")
print(user1.get_email())
print("Testing change_email user2: xiomei@that.org")
user2.change_email("xiomei@that.org")
print(user2.get_email())
print("Testing read_book user3: The Book and That Book")
user3.read_book(book1)
user3.read_book(book2, 2.67)
print(user3.get_books_read())
print("Testing get_average_rating user3: 2")
user3.read_book(book3, 1.33)
print(user3.get_average_rating())

print("Begin books testing\n")
print("Testing book1 instance: The Book, 123789, 14")
print(book1.title, book1.isbn, book1.price, sep=" , ")
print("Testing equality of user1 and user2: False")
book1 == book2
print("Testing equality of user1 and user3: True")
book3 == book4
print("Testing book as dictionary key: book5: success")
dict1 = {book5: "success"}
print(dict1)
print("Testing get_title book5: Harvey Book")
print(book5.get_title())
print("Testing get_isbn book5: 123999")
print(book5.get_isbn())
print("Testing set_isbn book4: 123555")
book4.set_isbn(123555)
print(book4.get_isbn())
print("Testing add_rating book4: 1.5, 3.5, 4")
book4.add_rating(1.5)
book4.add_rating(3.5)
book4.add_rating(4)
print(book4.ratings)
print("Testing get_average_rating book4: 3")
print(book4.get_average_rating())

print("Begin fiction testing\n")
print("Testing fiction1 instance: Untruth, 122345, Jim Crowed, 90")
print(fiction1.title, fiction1.isbn, fiction1.author, fiction1.price, sep=" , ")
print("Testing printing fiction1: Untruth by Jim Crowed")
print(fiction1)
print("Testing get_author fiction1: Jim Crowed")
print(fiction1.get_author())
print("Testing equality of fiction1 and fiction2: False")
fiction1 == fiction2
print("Testing equality of fiction4 and fiction5: True")
fiction4 == fiction5

print("Begin non fiction testing\n")
print("Testing non_fiction1 instance: Python for Dummies, 111999, Beginner, Programming, 22.9")
print(non_fiction1.title, non_fiction1.isbn, non_fiction1.level, non_fiction1.subject, non_fiction1.price, sep=" , ")
print("Testing printing non_fiction1: Python for Dummies, a Beginner manual on Programming")
print(non_fiction1)
print("Testing get_subject non_fiction1: Programming")
print(non_fiction1.get_subject())
print("Testing get_level non_fiction1: Beginner")
print(non_fiction1.get_level())
print("Testing equality of non_fiction1 and non_fiction2: False")
non_fiction1 == non_fiction2
print("Testing equality of non_fiction1 and non_fiction3: True")
non_fiction1 == non_fiction3

print("Begin tomerater testing\n")
print("Testing tomerater1 instance")
print(tomerater1.users, tomerater1.books, sep=" , ")
print("Testing tomeraterbook1 equal to book2: True")
tomeraterbook1 == book2
print("Testing tomeraternovel1 equal to fiction1: True")
tomeraternovel1 == fiction1
print("Testing tomeraternon_fiction1 equal to non_fiction1: True")
tomeraternon_fiction1 == non_fiction1
print("Testing add_user tomerater1: Beatriz Rodriguez, Bella@last.org, The Book, Henry Book")
tomerater1.add_user("Beatriz Rodriguez", "Bella@last.org", [book1, book5])
print(tomerater1.users, tomerater1.books, sep=" , ")
print("Testing add_book_to_user tomerater1 user1: That Book")
print(tomerater1.add_book_to_user(tomeraterbook1, "Bella@last.org"))
print(tomerater1.users, tomerater1.books, sep=" , ")
print("Testing print_catalog tomerater1: The Book, That Book, That Book")
tomerater1.print_catalog()
print("Testing print_users tomerater1: Beatriz Rodriguez, Bella@last.org")
tomerater1.print_users()
print("Testing most_read_book tomerater2: Watch My Hand by Nancy P. Magcian")
tomerater2.add_user("Beatriz Rodriguez", "Bella@last.org")
tomerater2.add_user("Xiomei Li", "li@test.edu")
tomerater2.add_book_to_user(fiction4, "Bella@last.org")
tomerater2.add_book_to_user(fiction4, "li@test.edu")
tomerater2.add_book_to_user(tomeraternovel1, "Bella@last.org")
print(tomerater2.most_read_book())
print("Testing highest_rated_book tomerater3: Untruth by Jim Crowed")
tomerater3.add_user("Beatriz Rodriguez", "Bella@last.org")
tomerater3.add_user("Xiomei Li", "li@test.edu")
tomerater3.add_book_to_user(fiction3, "Bella@last.org", 4)
tomerater3.add_book_to_user(fiction3, "li@test.edu", 3)
tomerater3.add_book_to_user(tomeraternovel1, "Bella@last.org", 3.7)
print(tomerater3.highest_rated_book())
print("Testing most_positive_user tomerater3: Beatriz Rodriguez")
print(tomerater3.most_positive_user())
print("Testing get_n_most_read_books tomerater3: That Book & Python for Dummies")
tomerater3.add_book_to_user(tomeraterbook1, "Bella@last.org", 4)
tomerater3.add_book_to_user(tomeraterbook1, "li@test.edu", 2)
print(tomerater3.get_n_most_read_books(2))
print("Testing get_n_most_prolific_readers tomerater3: Beatriz Rodriguez & Jenny Parque")
tomerater3.add_user("Jenny Parque", "jenny.from@theblock.org")
tomerater3.add_book_to_user(tomeraterbook1, "Bella@last.org", 3.8)
tomerater3.add_book_to_user(tomeraterbook1, "jenny.from@theblock.org", 2)
tomerater3.add_book_to_user(non_fiction1, "jenny.from@theblock.org", 1.5)
tomerater3.add_book_to_user(tomeraternovel1, "jenny.from@theblock.org", 2.3)
print(tomerater3.get_n_most_prolific_readers(2))
