"""
#This program will take the Month of your birth and the day to determine what zodiac sign you are,
#and what element that zodiac sign belongs to
#At the moment you have to enter the  birth months as followed :
#"January", "Febuary", "March", "April" , "May","June","July","August","September","October","November","December"
"""

import sys
inputMonth = input(" Please enter your birth month : ")
inputDay = int(input("Please enter the day of your birth : "))
Months = []
Days = []
Days.append(int(inputDay))
Months.append(inputMonth)
messageAir = ("Air signs are rational, social, and love communication and relationships")
messageEarth = ("Earth signs are “grounded” and the ones that bring us down to earth They are mostly conservative and realistic")
messageFire = ("Fire signs tend to be passionate, dynamic, and temperamental They get angry quickly, but they also forgive easily.")
messageWater =( "Water signs are exceptionally emotional and ultra-sensitive")
    

jan = ["January","january","JANUARY"]
feb = ["Febuary","febuary","FEBUARY"]
mar = ["March","march","MARCH"]
apr = ["April","april","APRIL"]
may = ["May","may","MAY"]
jun = ["June","june","JUNE"]
jul = ["July","july","JULY"]
aug = ["August","august","AUGUST"]
sept = ["September","september","SEPTEMBER"]
octo = ["October","october","OCTOBER"]
nov = ["November","november","NOVEMBER"]
dec = ["December","december","DECEMBER"]


if inputMonth == jan[0] or inputMonth == jan[1] or inputMonth == jan[2]:
    inputMonth = "January"
if inputMonth == feb[0] or inputMonth == feb[1] or inputMonth == feb[2]:
    inputMonth = "Febuary"
if inputMonth == mar[0] or inputMonth == mar[1] or inputMonth == mar[2]:
    inputMonth = "March"
if inputMonth == apr[0] or inputMonth == apr[1] or inputMonth == apr[2]:
    inputMonth = "April"
if inputMonth == may[0] or inputMonth == may[1] or inputMonth == may[2]:
    inputMonth = "May"
if inputMonth == jun[0] or inputMonth == jun[1] or inputMonth == jun[2]:
    inputMonth = "June"
if inputMonth == jul[0] or inputMonth == jul[1] or inputMonth == jul[2]:
    inputMonth = "July"
if inputMonth == aug[0] or inputMonth == aug[1] or inputMonth == aug[2]:
    inputMonth = "August"
if inputMonth == sept[0] or inputMonth == sept[1] or inputMonth == sept[2]:
    inputMonth = "September"
if inputMonth == octo[0] or inputMonth == octo[1] or inputMonth == octo[2]:
    inputMonth = "October"
if inputMonth == nov[0] or inputMonth == nov[1] or inputMonth == nov[2]:
    inputMonth = "November"
if inputMonth == dec[0] or inputMonth == dec[1] or inputMonth == dec[2]:
    inputMonth = "December"
    
 
if inputMonth == "January":
    if (Days[0] <= 19):
        print(messageEarth)
        Astro = "Capricorn"
        Type = "Earth"
        
    elif (Days[0] >= 20):
        print(messageAir)
        Astro = "Aquarius"
        Type = "Air"
        print(Astro)
        
elif inputMonth == "Febuary":
    if (Days[0] <= 18):
        print(messageAir)
        Type = "Air"
        Astro = "Aquarius"
        
    elif (Days[0] >=19):
        print(messageWater)
        Astro = "Pisces"
        Type = "Water"
        print(Astro)
        
elif inputMonth == "March":
    
    if (Days[0] <=20):
        print(messageWater)
        Astro = "Aries"
        Type = "Water"
        print(Astro)
        
    elif (Days[0] >= 21):
        print(messageFire)
        Astro = "Aries"
        Type = "Fire"
        print(Astro)
        
elif inputMonth == "April":
    
    if (Days[0] <= 19):
        print(messageFire)
        Astro = "Aries"
        Type = "Fire"
        print(Astro)
        
    elif (Days[0] >= 20):
        print(messageEarth)
        Astro = "Taurus"
        Type = "Earth"
        print(Astro)
        
elif inputMonth == "May":
    
    if (Days[0] <= 20):
        print(messageEarth)
        Astro = "Taurus"
        Type = "Earth"
        print(Astro)
        
    elif (Days[0] >= 21):
        print(messageAir)
        Astro = "Gemini"
        Type = "Air"
        print(Astro)
         
elif inputMonth == "June":
    
    if (Days[0] <= 20):
        print(messageAir)
        Astro = "Gemini"
        Type = "Air"
        print(Astro)
        
    elif (Days[0] >= 21):
        print(messageWater)
        Astro = "Cancer"
        Type = "Water" 
        print(Astro)
        
elif inputMonth == "July":
    
    if (Days[0] <= 22):
        print(messageWater)
        Astro = "Cancer"
        Type = "Water"
        print(Astro)
        
    elif (Days[0] >= 23):
        print(messageFire)
        Astro = "Leo"
        Type = "Fire" 
        print(Astro)
        
elif inputMonth == "August":
    
    if (Days[0] <= 22):
        print(messageFire)
        Astro = "Leo"
        Type = "Fire"
        print(Astro)
        
    elif (Days[0] >= 23):
        print(messageEarth)
        Astro = "Virgo"
        Type = "Earth"
        print(Astro)
        
elif inputMonth == "September":
    
    if (Days[0] <= 22):
        print(messageEarth)
        Astro = "Virgo"
        Type = "Earth"
        print(Astro)
          
    elif (Days[0] >= 23):
        print(messageAir)
        Astro = "Libra"
        Type = "Air" 
        print(Astro)
        
elif inputMonth == "October":
    
    if (Days[0] <= 22):
        print(messageAir)
        Astro = "Libra"
        Type = "Air"
        print(Astro)
        
    elif (Days[0] >= 23):
        print(messageWater)
        Astro = "Scorpio"
        Type = "Water" 
        print(Astro)
        
elif inputMonth == "November":
    
    if (Days[0] <= 21):
        print(messageWater)
        Astro = "Scorpio"
        Type = "Water"
        print(Astro)
    
    elif (Days[0] >= 22):
        print(messageFire)
        Astro = "Sagittarius"
        Type = "Fire" 
        print(Astro)
        
elif inputMonth == "December":
    
    if (Days[0] <= 21):
        print(messageFire)
        Astro = "Sagittarius"
        Type = "Fire"
        print(Astro)
        
    if (Days[0] >= 22):
        print(messageEarth)
        Astro = "Capricorn"
        Type = "Earth"
        print(Astro)
        
else:
    
        print("Not a Valid Month")
        sys.exit()
        


print("Your birthday is : ", inputMonth , inputDay, ", And your Zodiac sign is : ", Astro , " , The element of the sign is : ", Type)



    

