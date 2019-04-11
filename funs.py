from math import sqrt 
from operator import itemgetter 
import random 
import pygame 
import database_1003 as f
apple = 1 

#default distance assigned to canteens is 0
canteens_name_and_distance=[['Canteen 1',0], ['Canteen 2',0], ['Canteen 9',0], ['Canteen 11',0], ['Canteen 13',0], ['Canteen 14',0], ['Canteen 16',0], ['North Hill',0], ['Tamarind',0], ['Pioneer',0], ['Quad Cafe',0], ['North Spine',0], ['South Spine',0]]

#pre-assigned coordinates of canteens on map
coord_list = [['Canteen 1', 687.0, 632.0], ['Canteen 2', 755.0, 514.0], ['Canteen 9', 977.0, 294.0], ['Canteen 11', 1168.0, 212.0], ['Canteen 13', 690.0, 91.0], ['Canteen 14', 822.0, 101.0], ['Canteen 16', 613.0, 172.0], ['North Hill', 1205.0, 296.0], ['Tamarind', 1063.0, 113.0], ['Pioneer', 796.0, 792.0], ['Quad Cafe', 221.0, 386.0], ['North Spine', 353.0, 305.0], ['South Spine', 254.0, 672.0]]


def MouseClick():
   finish = False
   while finish == False:
   ## pygame.event.get() retrieves all events made by user
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           finish = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            finish = True
   pygame.quit()
   return (mouseX, mouseY)

def get_user_location():
   
   ## make necessary initializations for Width, Height
   W = 1221
   H = 862
   
   # initialize display window, call it screen
   screen = pygame.display.set_mode((W, H))
   
   # read image file and rescale it to the window size
   screenIm = pygame.image.load("NTU Campus.png")
   screenIm = pygame.transform.scale(screenIm, (W , H))
   
   # add the image over the screen object
   screen.blit(screenIm,(0, 0))   
   # add the text over the screen object
   
   #will update the contents of the entire display window
   pygame.display.flip()
   
   # get outputs of Mouseclick event handler 
   buttonX, buttonY = MouseClick()
   return buttonX, buttonY
   
#to calculate distance of user from canteens
def distance_a_b(x_coord,y_coord): 
  apple=0
  for i in range(0,13):
    canteens_name_and_distance[i][1]=(sqrt(((x_coord - coord_list[i][1])**2)+((y_coord - coord_list[i][2])**2)))
  
#to sort the calculated distances in ascending order
def sort_distance():
  canteens_name_and_distance.sort(key=itemgetter(1))
  for i in canteens_name_and_distance:
    print(i)

#to sort data of prefered food cuisine by distance in ascending order 

def sort_by_rank(food_cuisine):
  if apple==1:
    x_coord, y_coord= get_user_location()
    distance_a_b(x_coord,y_coord)
  
  
  #filtering data of prefered cuisine 

  food_cuisine_list= f.cuisineTypeData(food_cuisine)
  
  food_cuisine_list_sorted=[]
  
  for i in range(len(food_cuisine_list)):
    #comparing the filtered data to distance data to find intersection and store in a new list  
    for j in range(len(canteens_name_and_distance)):
      if food_cuisine_list[i][5]==canteens_name_and_distance[j][0]:
        food_cuisine_list_sorted.append(canteens_name_and_distance[j])

  #sorting the list    
  food_cuisine_list_sorted.sort(key=itemgetter(1))
  
  for a in food_cuisine_list_sorted:
    print(a)

#to find distance from nearest canteen 
def nearest_canteen_cumulative():
  x_coord, y_coord= get_user_location()
  distance_a_b(x_coord,y_coord)
  sort_distance()
