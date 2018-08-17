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
fiction5 = Fiction("The Left Way", 122333, "Umaq Umaqraq", 34500)

print("Creating Non_Fiction")
non_fiction1 = Non_Fiction("Python for Dummies", 111999, "Beginner", "Programming", 22.9)

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

print("Testing user1 instance: Beatriz Rodriguez, Bella@last.org")
print(user1.name, user1.email, user1.books)
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
