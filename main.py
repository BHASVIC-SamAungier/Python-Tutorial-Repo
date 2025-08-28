#(rock paper scissors game)

#  def get_choices():
#     player_choice = input('Enter a choice: rock,paper,scissor: ')
#     options = ['rock','paper','scissor']
#     computer_choice = random.choice(options)
#     choices = {'player':player_choice, 'computer':computer_choice}
#     return choices

# def check_win(player, computer):
#     print(f'You chose {player} and computer chose {computer}')
#     if player == computer:
#         return 'It is a tie!'
#     elif player == 'rock':
#         if computer == 'scissor':
#             return 'Rock smashes scissors! You win!'
#         else:
#             return 'Paper covers rocks! You lose.'
#     elif player == 'paper':
#         if computer == 'rock':
#             return 'Paper covers rock! You win!'
#         else:
#             return 'Scissors cuts paper! You lose.'
#     elif player == 'scissors':
#         if computer == 'paper':
#             return 'Scissors cuts paper! You win!'
#         else:
#             return 'Rocks smashes papers! You lose.'
#
# choices = get_choices()
# result = check_win(choices['player'], choices['computer'])
# print(result)

# name = 'Beau'
# print(isinstance(name,str)) # checks if a variable is an instance of a data type
# number = "20"
# age = int(number)
# print(isinstance(age,int))

# age = 8
# age += 8 # age = age +8, can remove the + to any arithmetic operator
# print(age)
# def is_adult(age):
#     if age > 18:
#         return True
#     else:
#         return False

# def is_adult2(age):
#     return True if age > 18 else return False
#x = 'beau'
#print('au' in x)
#name = 'be\'au'
#print(name)
#name ='ja"mie'
#print(name)
# for double and single quote
#name_2 = 'je"\'nifar'
#print(name_2)
#string = 'beau is cool'
#print(string[1:7])
#done = True
#print(type(done) == bool) # checks if a value is boolean
#if done:
#    print('yes') # prints yes when done = true or when any variable is equal to true
#else:
#    print('no')
#num_1 = 2+3j
#num_2 = complex(2,3)
#print(num_1.real)
#print(num_1.imag)
#print(num_2.real)
#print(num_2.imag)
#from enum import Enum
#class State(Enum):
#    INACTIVE = 0
#    ACTIVE = 1
#print(State.ACTIVE.value) # assigns a constant value
#print(list(State)) # prints out the types of states
#print(len(State)) # prints out how many states are there
#age = input('What is your age? ')
#print("your age is "+ age)
# items = ['Rodger','Syd', 1, 2, True]
# print('Beau' in dogs) # checks if an item is in an list
# print(dogs[1])
# print(dogs.pop())
# print(dogs)
# dogs.insert(1,'Jean')
# print(dogs)
# items[1:1] = ['Test1', 'Test2']
# print(items)

# names = ['Jamie', 'Hubert','Amy','ben', 'Dean', 'Max', ]
# namescopy = names[:]
# names.sort(key=str.lower)
# print(sorted(names, key=str.lower))
# print(names)
# print(namecopy)

# names = ('Rodger', 'Syd')
# names[0]
# print(names[0])

# dog = {'name':'Rodger', 'age': 25, 'colour': 'green'}
# dog['name'] = 'Syd'
# print(dog['name'])
# print(dog.get('name'))
# print(dog.pop('name'))
# print(dog)
# print(dog.popitem())
# print(dog)
# print('colour' in dog)
# print(list(dog.keys()))
# print(list(dog.values()))
# print(list(dog.items()))
# dog['favourite food'] = 'Meat' # adding an item to a list
# print(dog)
# del dog['colour']
# print(dog)
# dogCopy
# set1 = {'Rodger', 'Syd'}
# set2 = {'Luna'}
#  intersect = set1 & set2 # sees what they both have in common
#  print(intersect)
#  mod = set1 | set2 # everything in both sets
#  print(mod)
#  mod = set1 - set2 # the difference between the sets
#  print(mod)
# x = set1 > set2
# print(x)
# def hello(name,age):
#     print('Hello!'+ name + "you are " + str(age), +"years old")
#
# hello("Beau", 24)  # these are called arguments
# hello("Quincy",16)
# def change(value):
#     value['name'] = 'Syd'
#
# val = {'name': 'Beau'}
# change(val)
# print(val)
# def hello(name):
#     print("Hello " + name+ "!")
#     return name,"Beau", 8
#
# print(hello("Syd"))
# age = 8
# def test():
#     print(age)
#
# print(age)
# test()
# def talk(phrase):
#     def Say(word):
#         print(word)
#     words = phrase.split(' ') # splits the word at each space and creates a list
#     for word in words:
#         Say(word)
#
# talk('I am going to buy the milk')
# def counter():
#     count = 0
#
#     def increment():
#         nonlocal count # allows us to access the variable that was declared outside
#         count += 1
#         print(count)
#
#     return increment
#
# increment = counter()
# print(increment())
# print(increment())
# print(increment())

# age = 8
# print(age.real)
# print(age.imag)
# print(age.bit_length())

# items = [1,2]
# items.append(3)
# items.pop()
# print(id(items))

# count = 0
# while count < 10:
#     print("The condition is true")
#     count += 1
# print("After the loop")
# items = [1,2,3,4]
# for item in items:
#     if item == 2:
#         break
#     print(item)
# class Animal:
#     def Walk(self):
#         print("Walking....")

# class Dog(Animal):
#     def __init__(self, name, age): # initialise properties
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print("Woof")
#
# roger = Dog("Roger",8)
# print(roger.name)
# print(roger.age)
# roger.bark()
# roger.Walk()
# from dog import Bark
# Bark()

# import math
#print(math.sqrt(4))
#         =
#from math import sqrt
#print(sqrt(4))

# Lambda Functions
#multiply = lambda a, b : a * b
#print(multiply(2, 4))

# map(), filter(), reduce()

#numbers = [1, 2, 3]
#result = map(lambda a : a * 2, numbers)
#print(list(result))

#numbers = [1, 2, 3, 4, 5, 6,]
#def isEven(n):
#result = filter(lambda n : n % 2 == 0, numbers)
#print(list(result))

#from functions import reduce
#expenses = [
#   ('Dinner', 80),
#   ('Car repair', 120)
# ]
#sum = reduce(lambda a, b: a[1] + b[1], expenses)
#print(sum)

# Recursion

#def factorial(n):
#   if n == 1: return 1
#   return n * factorial(n-1)
#print(factorial(3))
#print(factorial(4))
#print(factorial(5))

# Decorators

# def logtime(func):
#   def wrapper():
#       print("before")
#       val = func()
#       print("after")
#       return val
#   return wrapper

# @logtime
# def hello():
#   print("hello")
# hello()

# Docstrings

# def increment(n):
#   """Increment a number"""
#   return n + 1

# class Dog:
#   """A class representing a dog"""
# def __init__(self, name, age):
#   """Initialize a new dog"""
#   self.name = name
#   self.age = age

#   def bark(self):
#       """Let the dog bark"""
#       print('WOOF!')

# print(help(Dog))

# Annotations

# def increment(n: int) -> int:
#    return n + 1
# count: int = 0

# Exceptions

#try:
#   result = 2 / 0
# except ZeroDivisionError:
#   print('Cannot divide by zero!'):
# finally:
#   result = 1
# print(result) #1

#try:
#    raise Exception('An error!') //set whatever error msg you want
# except Exception as error:
#   print(error)

#class DogNotFoundException(Exception):
#   print("inside")
#   pass

#try:
#    raise DogNotFoundException()
#exception DogNotFoundException:
#   print('Dog not found!')

#filename = '/Users/flavio.test.txt'
#with open(filename, 'r' as file:
#   content = file.read()
#   print(content)

# List Compressions
# numbers = [1, 2, 3, 4, 5]
# numbers_power_2 = [n**2 for n in numbers] // same functionality as line 331-333 in a single line & line 335
# print(numbers_power_2)

#numbers_power_2 = []
#for n in numbers:
#   numbers_power_2.append(n**2)

#numbers_power_2 = list(map(lambda n : n**2, numbers))

# Polymorphism

#class Dog
#   def eat(self)
#       print('Eating dog food')

#class Cat:
#   def cat(self):
#       print('Eating cat food')

#animal1 = Dog()
#animal2 = Cat()

#animal1.eat()
#animal2.eat()

# Operator Overloading

#class Dog:
#   def __init__(self, name, age):
#       self.name = name
#       self.aeg = age
#   def __gt__(self, other):
#       return True if self.age > other.age else False

#roger = Dog('Roger, 8)
#syd = Dog('Syd', 9)

#print(roger > syd)

#__add__() respond to the + operator
#__sub__() respond to the - operator
#__mul__() respond to the * operator
#__truediv__() respond to the / operator
#__floordiv__() respond to the // operator
#__mod__() respond to the % operator
#__pow__() respond to the ** operator
#__rshift__() respond to the >> operator
#__lshift__() respond to the << operator
#__and__() respond to the & operator
#__or__() respond to the | operator
#__xor__() respond to the ^ operator

#(blackjack game)

#import random

#class Card:
#   def __init__(self, suit, rank):
#       self.suit = suit
#       self.rank = rank
#   def __str__(self):
#       return f"{self.rank['rank']} of {self.suit}"



#class Deck:
#   def__init__(self)
#       self.cards = []
#       suits = ["Spades","Clubs","Hearts","Diamonds]
#       ranks = [
#               {"rank", "A", "value": 11},
#               {"rank", "2", "value": 2},
#               {"rank", "3", "value": 3},
#               {"rank", "4", "value": 4},
#               {"rank", "5", "value": 5},
#               {"rank", "6", "value": 6},
#               {"rank", "7", "value": 7},
#               {"rank", "8", "value": 8},
#               {"rank", "9", "value": 9},
#               {"rank", "10", "value": 10},
#               {"rank", "J", "value": 10},
#               {"rank", "Q", "value": 10},
#               {"rank", "K", "value": 10},
# ]

# for suit in suits:
#   for rank in ranks:
#       self.cards.append(Card(suit, rank))

#   def shuffle(self)
#       if len(self.cards) > 1:
#           random.shuffle(self.cards)

#   def deal(self, number):
#       cards_dealt = []
#       for x in range(number):
#           if len(self.cards) > 0
#               card = self.cards.pop():
#               cards_dealt.append(card)
#       return cards_dealt

# class Hand:

#   def __init__(self, dealer=False):
#       self.cards = []
#       self.value = 0
#       self.dealer = dealer

#   def add_cards(self, card_list):
#       self.cards.extend(card_list)
#
#   def calculate_value(self)
#       self.value = 0
#       has_ace = False
#
#       for card in self.cards:
#           card_value = int(card.rank["value"])
#           self.value += card_value
#           if card.rank["rank"] == "A":
#               has_ace = True

#       if has_ace and self.value > 21:
#           self.value -= 10

#   def get_value(self):
#       self.calculate_value()
#       return self.value

#   def is_blackjack(self):
#       return self.get_valued() == 21

#   def display(self, show_all_dealer_cards=False):
#       print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
#       for index, card in enumerate(self.cards):
#       if index = 0 and self.dealer \
#       and not show_all_dealer_cards and not self.is_blackjack():
#           print("hidden")
#       else:
#           print(card)

#       if not self.dealer:
#           print("Value:", self.get_value())
#       print()

#   class Game:
#       def play(self):
#           game_number = 0
#           game_to_play = 0
#
#       while games_to_play <= 0:
#           try:
#               games_to_play = int(input("How many games do you want to play? "))
#           except:
#               print("You must enter a number.")
#
#       while game_number < games_to_play:
#           game_number += 1
#
#           deck.Deck()
#           deck.shuffle()
#
#           player_hand = Hand()
#           dealer_hand = Hand(dealer=True)
#
#           for i in range(2):
#               player_hand.add_card(deck.deal(1))
#               dealer_hand.add_card(deck.deal(1))
#
#           print()
#           print("*" * 30)
#           print(f"Game {game_number} of {games_to_play}")
#           print("*" * 30)
#           player_hand.display()
#           dealer_hand.display()

#           if self.check_winner(player_hand, dealer_hand):
#               continue

#           choice = ""
#           while player_hand.get_value() < 21 and choice not in ["S", "stand"]:
#               choice = input("Please choose to 'Hit or 'Stand': ").lower()
#               print()
#               while choice not in ["h", "s", "hit", "stand"]:
#                   choice = input("Please enter 'Hit' or 'Stand': ").lower()
#                   print()
#               if choice in ["hit", "h"]:
#                   player_hand.add_card(deck.deal(1))
#                   player_hand.display()

#           if self.check_winner(player_hand, dealer_hand):
#               continue

#           player_hand_value = player_hand.get_value()
#           dealer_hand_value = dealer_hand.get_value()

#           while dealer_hand_value < 17:
#               dealer_hand.add_card(deck.deal(1))
#               dealer_hand.value = dealer_hand.get_value()

#           dealer_hand.display(show_all_dealer_cards=True)

#           if self.check_winner(player_hand, dealer_hand):
#               continue

#           print("Final Results")
#           print("Your hand:", player_hand_value)
#           print("Dealer's hand:", dealer_hand_value)

#           self.check_winner(player_hand, dealer_hand, True)

#       print("\nThanks for playing!")

#   def check_winner(self, player_hand, dealer_hand, game_over=False):
#       if not game_over:
#           if player_hand.get_value() > 21:
#               print("You busted, dealer wins!")
#               return True
#           elif dealer_hand.get_value() > 21:
#               print("Dealer busted, you win!")
#               return True
#           elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
#               print("Both players haver blackjack it's a tie!")
#               return True
#           elif player_hand.is_blackjack():
#               print("You have blackjack, you win!")
#               return True
#           else:
#               if player_hand.get_value() > dealer_hand.get_value():
#                   print("You win!")
#               elif player_hand.get_value() == dealer_hand.get_value():
#                   print("Tie")
#               else:
#                   print("Dealer wins!")
#           return False

# g = Game()
# g.play()
