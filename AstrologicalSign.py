"""
#This program will take the Month of your birth and the day to determine what zodiac sign you are,
#and what element that zodiac sign belongs to
#At the moment you have to enter the  birth months as followed :
#"January", "Febuary", "March", "April" , "May","June","July","August","September","October","November","December"
#Make sure to include the first letter as a capital"""

import sys

#Signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo","Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn","Aquarius", "Pisces"]
inputMonth = input(" Please enter your birth month : ")
inputDay = int(input("Please enter the day of your birth : "))

#for x in range(1,32):

Months = []
Days = []
Days.append(int(inputDay))
Months.append(inputMonth)
    
    
    #print(Days[0],Months[0])
    
    
    
if inputMonth == "January":
    
    
    Astro = "Capricorn"
    if (Days[0] >= 20):
        Astro = "Aquarius"
    Type = "Air"
    print(Astro)
    message = print("Earth signs are “grounded” and the ones that bring us down to earth They are mostly conservative and realistic,")
    
      
elif inputMonth == "Febuary":
    
    Astro = "Aquarius"
    if (Days[0] >=19):
        Astro = "Pisces"
    Type = "Water"
    print(Astro)
    message = print("Water signs are exceptionally emotional and ultra-sensitive ")
    
     
elif inputMonth == "March":
    Astro = "Pisces"
    if (Days[0] >= 21):
        Astro = "Aries"
    Type = "Fire"
    print(Astro)
    message = print("Fire signs tend to be passionate, dynamic, and temperamental They get angry quickly, but they also forgive easily. ")
    
       
elif inputMonth == "April":
    Astro = "Aries"
    if (Days[0] >= 20):
        Astro = "Taurus"
    Type = "Earth"
    print(Astro)
    message =  print("Earth signs are “grounded” and the ones that bring us down to earth They are mostly conservative and realistic")
    
    
elif inputMonth == "May":
    Astro = "Taurus"
    if (Days[0] >= 21):
        Astro = "Gemini"
    Type = "Air"
    print(Astro)
    message = print("Air signs are rational, social, and love communication and relationships")
   
    
elif inputMonth == "June":
    Astro = "Gemini"
    if (Days[0] >= 21):
        Astro = "Cancer"
    Type = "Water" 
    print(Astro)
    message = print("Water signs are exceptionally emotional and ultra-sensitive ")
    
elif inputMonth == "July":
    Astro = "Cancer"
    if (Days[0] >= 23):
        Astro = "Leo"
    Type = "Fire" 
    print(Astro)
    message = print("Fire signs tend to be passionate, dynamic, and temperamental They get angry quickly, but they also forgive easily. ")

elif inputMonth == "August":
    Astro = "Leo"
    if (Days[0] >= 23):
        Astro = "Virgo"
    Type = "Earth"
    print(Astro)
    message =  print("Earth signs are “grounded” and the ones that bring us down to earth They are mostly conservative and realistic")
    
    
elif inputMonth == "September":
    Astro = "Virgo"
    if (Days[0] >= 23):
        Astro = "Libra"
    Type = "Air" 
    print(Astro)
    message = print("Air signs are rational, social, and love communication and relationships")
    
elif inputMonth == "October":
    Astro = "Libra"
    if (Days[0] >= 23):
        Astro = "Scorpio"
    Type = "Water" 
    print(Astro)
    message = print("Water signs are exceptionally emotional and ultra-sensitive ")
    
elif inputMonth == "November":
    Astro = "Scorpio"
    if (Days[0] >= 22):
        Astro = "Sagittarius"
    Type = "Fire" 
    print(Astro)
    message = print("Fire signs tend to be passionate, dynamic, and temperamental They get angry quickly, but they also forgive easily. ")
    
elif inputMonth == "December":
    Astro = "Sagittarius"
    if (Days[0] >= 22):
        Astro = "Capricorn"
    Type = "Earth"
    print(Astro)
    message =  print("Earth signs are “grounded” and the ones that bring us down to earth They are mostly conservative and realistic")
        
else:
        print("Not a Valid Month")
        sys.exit()
        
print("Your birthday is : ", inputMonth , inputDay, ", And your Zodiac sign is : ", Astro , " , The element of the sign is : ", Type)



    

