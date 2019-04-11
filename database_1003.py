"""
    This is the main database. Our team use phpMyAdmin, mySQL as our database. The code below is aimed to collect and access
    the data from the database. Since the database runs locally, we have provided the all of the 
    data below for your reference. We have designed our database as follows: 
        index 0 : Food Name (string/varchar in mySQL)
        index 1 : Price (float)
        index 2 : Cuisine (Chinese, Indian, Korean, etc) (string/varchar in mySQL)
        index 3 : Type of Food (Vegetarian, Non-Vegetarian, Halal) (string/varchar in mySQL)
        index 4 : Stall Name (string/varchar in mySQL)
        index 5 : Canteen Name (string/varchar in mySQL)
        index 6 : Telephone Number (integer)
        index 7 : Address (string/varchar in mySQL)
        index 8 : Opening hour (DATETIME in mySQL)
        index 9 : Closing hour (DATETIME in mySQL)
        
    We have standardized the data in our database. If we want to access food name, cuisine, type of food, stall name 
    or canteen name, the first letter in each words is always an uppercase letter. 
    
    Thank you and have a great day! 
"""

# Import modules

# Import mysql.connector to connect with our database
import mysql.connector  
# Import itemgetter to sort data
from operator import itemgetter

import pandas as pd

# Connect with our cz1003_canteen database 
mydb = mysql.connector.connect(
          host = "localhost",
          user = "root",
          passwd = "",
          database = "cz1003_canteen")

mycursor = mydb.cursor()

# Select all data from our table canteen_data in cz1003_canteen
mycursor.execute("SELECT * FROM canteen_data")

# Initializing data_list, this is the list to store all of our data
data_list = []  

for data in mycursor:
  data_list.append(list(data))                              # Append the list of data to data_list
                                                            # The output will be an array 

def printNice(input_data):
     data_frame = pd.DataFrame(input_data)
     new_cols = {
                 0 : 'Food Name',
                 1 : 'Price',
                 2 : 'Cuisine',
                 3 : 'Food Type',
                 4 : 'Stall',
                 5 : 'Canteen',
                 6 : 'Telephone',
                }
     
     data_frame.rename(columns = new_cols, inplace = True)
     pd.set_option('display.max_rows',101)
     pd.set_option('display.expand_frame_repr', False)
     return data_frame
    
# Search by table name function 
def linearSearch(data_list, column_index, target_data):
    index = 0                                               # Set the index to be 0
    target_list = []                                        # target_list is the list of searched items
    while index < len(data_list):
        if data_list[index][column_index] == target_data:   # the case when the target data is matched with data in data_list
            target_list.append(data_list[index])            # then it will append the data to target_list
        index += 1                                          # Increment the index
    return target_list                                      # The output is target_list

# Search by food name
def foodName(food):
    return printNice(linearSearch(data_list, 0, food))                 

# Search by price         
def priceSearch(price_):
    return printNice(linearSearch(data_list, 1, price_))     

# Search by cuisine
def cuisineType(cuisine):
    return printNice(linearSearch(data_list, 2, cuisine))
  
def cuisineTypeData(cuisine):
    return linearSearch(data_list, 2, cuisine)
# Search by food type
def foodType(food_type):
    return printNice(linearSearch(data_list, 3, food_type))

# Search by stall name
def stallName(stall):
    return printNice(linearSearch(data_list, 4, stall))

# Search by canteen name
def canteenName(canteen):
    return printNice(linearSearch(data_list, 5, canteen))

# Search by telephone number
def teleNum(telephone):
    return printNice(linearSearch(data_list, 6, telephone))

# Function to show all the data 
def showAll():
    return printNice(data_list)

# Sort the price using itemgetter module
def priceSort(max_price):
    price_sort = sorted(data_list, key = itemgetter(1))
    price_range = []
    index = 0
    while index < len(price_sort):
      if price_sort[index][1] <= max_price:
        price_range.append(price_sort[index])
        index += 1
      else:
        break
    return printNice(price_range)


""" 
This is the output if we call showAll() function

data_list = 
[['Lemon Chicken Rice', 2.8, 'Chinese', 'Non-Vegetarian', 'Chicken Rice', 'Canteen 2', 63343033],
['Roasted Chicken Rice', 3.5, 'Chinese', 'Non-Vegetarian', 'Chicken Rice', 'Canteen 2', 63343033],
['Steamed Chicken Rice', 3.5, 'Chinese', 'Non-Vegetarian', 'Chicken Rice', 'Canteen 2', 63343033],
['Dori Penyet', 5.0, 'Indonesian', 'Halal', 'Ayam Penyet', 'Canteen 2', 63343033],
['Ayam Panggang', 4.8, 'Indonesian', 'Halal', 'Ayam Penyet', 'Canteen 2', 63343033],
['Ayam Penyet', 5.0, 'Indonesian', 'Halal', 'Ayam Penyet', 'Canteen 2', 63343033],
['Kimchi Bokkeumbap', 3.8, 'Korean', 'Non-Vegetarian', 'Korean Cuisine', 'Canteen 2', 63343033],
['Korean Beef ', 5.5, 'Korean', 'Non-Vegetarian', 'Korean Cuisine', 'Canteen 2', 63343033],
['Chicken', 5.1, 'Korean', 'Non-Vegetarian', 'Korean Cuisine', 'Canteen 2', 63343033],
['Mala Xiao La', 5.0, 'Chinese', 'Non-Vegetarian', 'Mala Can1', 'Canteen 1', 63343033],
['Mala Zhong La', 5.1, 'Chinese', 'Non-Vegetarian', 'Mala Can1', 'Canteen 1', 63343033],
['Mala Da La', 5.2, 'Chinese', 'Non-Vegetarian', 'Mala Can1', 'Canteen 1', 63343033],
['Black Pepper Chicken', 3.2, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 1', 63343033],
['Salted Egg Fish', 3.1, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 1', 63343033],
['Cheese Tofu', 2.8, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 1', 63343033],
['Paneer', 3.0, 'Indian', 'Vegetarian', 'Indian Cuisine', 'Canteen 1', 63343033],
['Paratha', 4.5, 'Indian', 'Vegetarian', 'Indian Cuisine', 'Canteen 1', 63343033],
['Samosa', 5.1, 'Indian', 'Vegetarian', 'Indian Cuisine', 'Canteen 1', 63343033],
['Mala Xiao La', 5.0, 'Chinese', 'Non-Vegetarian', 'Mala Can9', 'Canteen 9'],
['Mala Zhong La', 5.1, 'Chinese', 'Non-Vegetarian', 'Mala Can9', 'Canteen 9'],
['Mala Da La', 5.2, 'Chinese', 'Non-Vegetarian', 'Mala Can9', 'Canteen 9'],
['Kimchi Bokkeumbap', 5.0, 'Korean', 'Non-Vegetarian', 'Korean 9', 'Canteen 9'],
['Beef Rice', 4.5, 'Korean', 'Non-Vegetarian', 'Korean 9', 'Canteen 9', 96923456],
['Samgye Tang', 4.7, 'Korean', 'Non-Vegetarian', 'Korean 9 ', 'Canteen 9', 96923456],
['Beef Ramen', 5.0, 'Japanese', 'Non-Vegetarian', 'Japanese Can9', 'Canteen 9', 96923456],
['Sushi', 5.0, 'Japanese', 'Non-Vegetarian', 'Japanese Can9', 'Canteen 9', 96923456],
['Chicken Katsu Don', 4.3, 'Japanese', 'Non-Vegetarian', 'Japanese Can9', 'Canteen 9', 96923456],
['Tonkatsu Don', 4.5, 'Japanese', 'Non-Vegetarian', 'Japanese Can11', 'Canteen 11', 97866726],
['Spicy Ramen', 4.7, 'Japanese', 'Non-Vegetarian', 'Japanese Can11', 'Canteen 11', 97866726],
['Chicken Curry ', 5.0, 'Japanese', 'Non-Vegetarian', 'Japanese Can11', 'Canteen 11', 97866726],
['Ji Dan', 1.2, 'Chinese', 'Non-Vegetarian', 'Japanese Can11', 'Canteen 11', 97866726],
['Ji Rou', 1.5, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice 11', 'Canteen 11', 97866726],
['Zhu Rou', 1.6, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice 11', 'Canteen 11', 97866726],
['Strawberry Waffle', 1.2, 'Italian', 'Halal', 'Waffle 11', 'Canteen 11', 97866726],
['Chocolate Waffle', 1.3, 'Italian', 'Halal', 'Waffle 11', 'Canteen 11', 97866726],
['Waffle + Ice Cream', 1.8, 'Italian', 'Halal', 'Waffle 11', 'Canteen 11', 97866726],
['Cereal Chicken', 5.0, 'Chinese', 'Non-Vegetarian', 'Golden Kitchen', 'Canteen 13', 98510908],
['Cereal Fish', 5.0, 'Chinese', 'Non-Vegetarian', 'Golden Kitchen', 'Canteen 13', 98510908],
['Sambal Chicken', 3.5, 'Chinese', 'Non-Vegetarian', 'Golden Kitchen', 'Canteen 13', 98510908],
['Chicken Curry', 5.0, 'Japanese', 'Non-Vegetarian', 'Menya Takashi', 'Canteen 13', 98510908],
['Tonkotsu Ramen', 5.1, 'Japanese', 'Non-Vegetarian', 'Menya Takashi', 'Canteen 13', 98510908],
['Mayo Karaage Don', 5.0, 'Japanese', 'Non-Vegetarian', 'Menya Takashi', 'Canteen 13', 98510908],
['Grilled Saba', 4.2, 'Korean', 'Non-Vegetarian', 'Korean 13', 'Canteen 13', 98510908],
['Samgye Tang', 4.7, 'Korean', 'Non-Vegetarian', 'Korean 13', 'Canteen 13', 98510908],
['Tteokbokki', 3.8, 'Korean', 'Non-Vegetarian', 'Korean 13', 'Canteen 13', 98510908],
['Fried Fish Ban Mian', 3.2, 'Chinese', 'Non-Vegetarian', 'Ban Mian', 'Canteen 14', 81127239],
['Tom Yum Ban Mian', 3.1, 'Chinese', 'Non-Vegetarian', 'Ban Mian', 'Canteen 14', 81127239],
['Teri Ban Mian', 3.0, 'Chinese', 'Non-Vegetarian', 'Ban Mian', 'Canteen 14', 81127239],
['Salted Egg Fish', 1.5, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 14'],
['Ji Rou', 1.6, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 14', 81127239],
['Zhu Rou', 1.7, 'Chinese', 'Non-Vegetarian', 'Mixed Veg Rice', 'Canteen 14'],
['Paneer', 3.8, 'Indian', 'Vegetarian', 'Indian 16', 'Canteen 16', 94505893],
['Paratha', 3.2, 'Indian', 'Vegetarian', 'Indian 16', 'Canteen 16', 94505893],
['Dosa', 3.2, 'Indian', 'Vegetarian', 'Indian 16', 'Canteen 16', 94505893],
['Tonkatsu Don', 5.0, 'Japanese', 'Non-Vegetarian', 'Japanese Can16', 'Canteen 16'],
['Beef Ramen', 3.7, 'Japanese', 'Non-Vegetarian', 'Japanese Can16', 'Canteen 16'],
['Tonkotsu Ramen', 4.8, 'Japanese', 'Non-Vegetarian', 'Japanese Can16', 'Canteen 16'],
['Dosa', 3.2, 'Indian', 'Vegetarian', 'Ananda Kitchen', 'North Hill', 82658140],
['Samosa', 3.7, 'Indian', 'Vegetarian', 'Ananda Kitchen', 'North Hill', 82658140],
['Biryani', 3.5, 'Indian', 'Vegetarian', 'Ananda Kitchen', 'North Hill', 82658140],
['Mala Xiao La', 5.0, 'Chinese', 'Non-Vegetarian', 'Mala NorthHill', 'North Hill', 82658140],
['Mala Zhong La', 5.1, 'Chinese', 'Non-Vegetarian', 'Mala NorthHill', 'North Hill', 82658140],
['Mala Da La', 5.2, 'Chinese', 'Non-Vegetarian', 'Mala NorthHill', 'North Hill', 82658140],
['Ayam Penyet', 5.0, 'Indonesian', 'Halal', 'Ayam Penyet', 'Tamarind ', 82963633],
['Ayam Panggang', 4.8, 'Indonesian', 'Halal', 'Ayam Penyet', 'Tamarind ', 82963633],
['Dori Penyet', 5.0, 'Indonesian', 'Halal', 'Ayam Penyet', 'Tamarind ', 82963633],
['Kimchi Bokkeumbap', 3.8, 'Korean', 'Non-Vegetarian', 'Korean Tamarind', 'Tamarind ', 82963633],
['Samgye Tang', 5.1, 'Korean', 'Non-Vegetarian', 'Korean ', 'Tamarind ', 82963633],
['Soondubu', 4.5, 'Korean', 'Non-Vegetarian', 'Korean ', 'Tamarind ', 82963633],
['Dosa', 3.2, 'Indian', 'Vegetarian', 'Indian 23', 'Tamarind ', 82963633],
['Samosa', 3.7, 'Indian', 'Vegetarian', 'Indian 23', 'Tamarind ', 82963633],
['Paratha', 5.0, 'Indian', 'Vegetarian', 'Indian 23', 'Tamarind ', 82963633],
['Lemon Chicken Rice', 3.5, 'Chinese', 'Non-Vegetarian', 'Chicken Rice', 'Pioneer', 82658181],
['Mala Xiao La', 5.0, 'Chinese', 'Non-Vegetarian', 'Mala Pion', 'Pioneer', 82658181],
['Fried Yong Tau Foo ', 4.5, 'Chinese', 'Non-Vegetarian', 'YTF', 'Quad Cafe', 82181829],
['Soup Yong Tau Foo ', 4.7, 'Chinese', 'Non-Vegetarian', 'YTF', 'Quad Cafe', 82181829],
['Pizza', 4.0, 'Italian', 'Halal', 'Pizza Hut Express', 'North Spine', 67626124],
['Roasted Duck', 3.3, 'Chinese', 'Non-Vegetarian', 'Cantonese Roast Duck', 'North Spine', 64658588],
['Chicken Fuyong', 3.5, 'Japanese', 'Non-Vegetarian', 'Japanese SS', 'South Spine'],
['Kaki Fuyong', 3.8, 'Japanese', 'Non-Vegetarian', 'Japanese SS', 'South Spine', 67900355]]

Total = 80 data

"""


