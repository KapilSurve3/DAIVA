from js import document
from js import window
import pandas as pd
from pyodide.http import open_url
#main printing function
result = document.getElementById('result')


Rashilords = ("Jupiter","Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn","Saturn")
Rashislist = ("Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces")
FirstH=("Personality","Body","Physique","Self","Nature")
SecondH=("Wealth","Food","Speech","Family","Mouth")
ThirdH=("Siblings","Speech","Conversation","Bravery/Courage","Neck/Collar")
FourthH=("Mother","Home","Estate","Pleasure/Comfort","Chest/Lungs")
FifthH=("Children","Education","Romance","Creativity","Stomach")
SixthH=("Enemies","Competetion","Debt","Disease","Intestine")
SeventhH=("Partner","Buisness","Spouse","Diplomacy","Pelvic/Kidney")
EightH=("Longetivity","Death","OccultScience","Sudden Events","Genitals")
NineH=("Dharma/Duty","Fortune","Ancestor","HigherEducation","Thighs")
TenthH=("Carrier/Profession","Workplace","Father","Authority","Knees")
Eleventh=("Income/Gains","SocialService","Friends","Fulfillment","Shins/Ankle")
TwelthH=("Spirituality","Foreign Lands","Distant/Secluded","Dream/intutions","Feet")
Vimshot=("Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury")
nakshatras = (
    "Ashwini",
    "Bharani",
    "Krittika",
    "Rohini",
    "Mrigashira",
    "Ardra",
    "Punarvasu",
    "Pushya",
    "Ashlesha",
    "Magha",
    "Purva Phalguni",
    "Uttara Phalguni",
    "Hasta",
    "Chitra",
    "Swati",
    "Vishakha",
    "Anuradha",
    "Jyeshtha",
    "Mula",
    "Purva Ashadha",
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha",
    "Purva Bhadrapada",
    "Uttara Bhadrapada",
    "Revati"
)
nakshatra_symbols = (
    "Horse's Head",
    "(Yoni) Female Reproductive Organ",
    "(Knife) or Spear",
    "(Cart) or Chariot",
    "(Deer's Head)",
    "(Teardrop) or Diamond",
    "(Bow and Quiver) of Arrows",
    "(Flower, Circle,) or Cow's Udder",
    "(Coiled Serpent)",
    "(Throne) or Palanquin",
    "(Front of a Couch)",
    "(Back Legs of a Couch)",
    "(Hand) or Fist",
    "(Pearl) or Bright Jewel",
    "(Young Plant Shoot,) Coral",
    "(Arch, Potter's Wheel)",
    "(Lotus Flower) or Triumphal Arch",
    "(Earring, Circular) Talisman",
    "(Roots, Umbrella)",
    "(Fan) or Winnowing Basket",
    "(Elephant's Tusk) or Planks of a Bed",
    "(Ear) or Three Footprints in an Ascending Path",
    "(Drum) or Flute",
    "(Empty Circle) or 1000 Flowers",
    "(Two-Faced Man) or Sword",
    "(Back Legs of a Funeral Cot) or Snake in the Water",
    "(Fish) or Drum"
)


nakshatra_to_vashya = {
    'Ashwini': 'Manav',
    'Bharani': 'Vanchar',
    'Krittika': 'Chatushpad',
    'Rohini': 'Chatushpad',
    'Mrigashira': 'Manav',
    'Ardra': 'Jalchar',
    'Punarvasu': 'Manav',
    'Pushya': 'Manav',
    'Ashlesha': 'Jalchar',
    'Magha': 'Keet',
    'Purva Phalguni': 'Vanchar',
    'Uttara Phalguni': 'Manav',
    'Hasta': 'Manav',
    'Chitra': 'Manav',
    'Swati': 'Manav',
    'Vishakha': 'Vanchar',
    'Anuradha': 'Manav',
    'Jyeshta': 'Keet',
    'Mula': 'Jalchar',
    'Purva Ashadha': 'Chatushpad',
    'Uttara Ashadha': 'Chatushpad',
    'Shravana': 'Manav',
    'Dhanishta': 'Vanchar',
    'Shatabhisha': 'Manav',
    'Purva Bhadrapada': 'Chatushpad',
    'Uttara Bhadrapada': 'Chatushpad',
    'Revati': 'Manav'
}

nakshatra_to_nadi = {
    'Ashwini': 'Adi',
    'Bharani': 'Adi',
    'Krittika': 'Adi',
    'Rohini': 'Adi',
    'Mrigashira': 'Adi',
    'Ardra': 'Adi',
    'Punarvasu': 'Adi',
    'Pushya': 'Adi',
    'Ashlesha': 'Adi',
    'Magha': 'Madhya',
    'Purva Phalguni': 'Madhya',
    'Uttara Phalguni': 'Madhya',
    'Hasta': 'Madhya',
    'Chitra': 'Madhya',
    'Swati': 'Madhya',
    'Vishakha': 'Madhya',
    'Anuradha': 'Madhya',
    'Jyeshta': 'Madhya',
    'Mula': 'Madhya',
    'Purva Ashadha': 'Antya',
    'Uttara Ashadha': 'Antya',
    'Shravana': 'Antya',    
    'Dhanishta': 'Antya',
    'Shatabhisha': 'Antya',
    'Purva Bhadrapada': 'Antya',
    'Uttara Bhadrapada': 'Antya',
    'Revati': 'Antya'
}
nakshatra_to_yoni = {
        'Ashwini': 'Horse',
        'Bharani': 'Elephant',
        'Krittika': 'Goat',
        'Rohini': 'Snake',
        'Mrigashira': 'Deer',
        'Ardra': 'Dog',
        'Punarvasu': 'Cat',
        'Pushya': 'Sheep',
        'Ashlesha': 'Cat',
        'Magha': 'Rat',
        'Purva Phalguni': 'Rat',
        'Uttara Phalguni': 'Cow',
        'Hasta': 'Buffalo',
        'Chitra': 'Tiger',
        'Swati': 'Buffalo',
        'Vishakha': 'Tiger',
        'Anuradha': 'Deer',
        'Jyeshta': 'Deer',
        'Mula': 'Dog',
        'Purva Ashadha': 'Monkey',
        'Uttara Ashadha': 'Monkey',
        'Shravana': 'Monkey',
        'Dhanishta': 'Lion',
        'Shatabhisha': 'Horse',
        'Purva Bhadrapada': 'Lion',
        'Uttara Bhadrapada': 'Cow',
        'Revati': 'Elephant'
    }
#This is Rolling function
def roll(num):
  house = num % 12
  if (house==0):
    num =  num - 12
  else:
    num = house
  return num

def roll2(num):
  planet = num % 9
  if(planet == 0):
    num = num - 9
  else:
    num = planet
  return num


def calculate_astakoot_milan(nakshatra1, nakshatra2,pada1,pada2,asc1,asc2,moonplacement1,moonplacement2):

  def Varnamilan(nakshatra1,pada1,nakshatra2,pada2):
    if pada1 == pada2:
      score = int(1)
    else:
      score = int(0)
    return score


  def Vashyamilan(nakshatra1,nakshatra2):
    nakshatra_to_vashya = {
    'Ashwini': 'Manav',
    'Bharani': 'Vanchar',
    'Krittika': 'Chatushpad',
    'Rohini': 'Chatushpad',
    'Mrigashira': 'Manav',
    'Ardra': 'Jalchar',
    'Punarvasu': 'Manav',
    'Pushya': 'Manav',
    'Ashlesha': 'Jalchar',
    'Magha': 'Keet',
    'Purva Phalguni': 'Vanchar',
    'Uttara Phalguni': 'Manav',
    'Hasta': 'Manav',
    'Chitra': 'Manav',
    'Swati': 'Manav',
    'Vishakha': 'Vanchar',
    'Anuradha': 'Manav',
    'Jyeshta': 'Keet',
    'Mula': 'Jalchar',
    'Purva Ashadha': 'Chatushpad',
    'Uttara Ashadha': 'Chatushpad',
    'Shravana': 'Manav',
    'Dhanishta': 'Vanchar',
    'Shatabhisha': 'Manav',
    'Purva Bhadrapada': 'Chatushpad',
    'Uttara Bhadrapada': 'Chatushpad',
    'Revati': 'Manav'
    }
    def get_vashya(nakshatra):
      return nakshatra_to_vashya.get(nakshatra, "Invalid Nakshatra")

    # Example usage
    nakshatra_name = nakshatra1
    vashya1 = get_vashya(nakshatra_name)
    nakshatra_name = nakshatra2
    vashya2 = get_vashya(nakshatra_name)
    if vashya1 == vashya2:
      score = 2
    elif (vashya1 == "Vanachar" and vashya2 != "Vanachar") or (vashya1 == "Keet" and vashya2 =="Vanachar") or (vashya1 == "Manav" and vashya2 == "Vanchar"):
      score = 0
    else:
      score = 1
    return score


  def Taramilan(nakshatra1,nakshatra2):
    Nakscount1 = 0
    Nakscount2 = 0
    for i in nakshatras:
      Nakscount1 = Nakscount1 + 1
      if nakshatra1 == i:
        break
    for j in nakshatras:
      Nakscount2 = Nakscount2 + 1
      if nakshatra2 == j:
        break
    diff = Nakscount1 - Nakscount2
    if diff == 3 or diff == 4 or diff == 5 or diff == 7 or diff == 9:
      score = 3
    elif diff == 2 or diff == 6 or diff == 8 or diff == 12:
      score = 2
    else:
      score = 1
    return score


  def Yonimilan(nakshatra1,nakshatra2):
    def get_yoni(nakshatra):
    # Dictionary mapping Nakshatras to their respective Yonis
      nakshatra_to_yoni = {
          'Ashwini': 'Horse',
          'Bharani': 'Elephant',
          'Krittika': 'Goat',
          'Rohini': 'Snake',
          'Mrigashira': 'Deer',
          'Ardra': 'Dog',
          'Punarvasu': 'Cat',
          'Pushya': 'Sheep',
          'Ashlesha': 'Cat',
          'Magha': 'Rat',
          'Purva Phalguni': 'Rat',
          'Uttara Phalguni': 'Cow',
          'Hasta': 'Buffalo',
          'Chitra': 'Tiger',
          'Swati': 'Buffalo',
          'Vishakha': 'Tiger',
          'Anuradha': 'Deer',
          'Jyeshta': 'Deer',
          'Mula': 'Dog',
          'Purva Ashadha': 'Monkey',
          'Uttara Ashadha': 'Monkey',
          'Shravana': 'Monkey',
          'Dhanishta': 'Lion',
          'Shatabhisha': 'Horse',
          'Purva Bhadrapada': 'Lion',
          'Uttara Bhadrapada': 'Cow',
          'Revati': 'Elephant'
      }

      if nakshatra in nakshatra_to_yoni:
          return nakshatra_to_yoni[nakshatra]
      else:
          return "Nakshatra not found or invalid input"

    yoni1 = get_yoni(nakshatra1)
    yoni2 = get_yoni(nakshatra2)

    if yoni1 == yoni2 :
      score = 4
    elif (yoni1 in ["Cat", "Buffalo", "Monkey", "Horse", "Cow","Deer","Elephant"] and yoni2 in ["Cat", "Buffalo", "Monkey", "Horse", "Cow","Deer","Elephant"]) and yoni1 != yoni2:
      score = 2
    elif (yoni1 in ["Lion","Dog","Rat","Snake"]and yoni2 in ["Lion","Dog","Rat","Snake"]and yoni1!=yoni2):
      score = 2
    else: score = 1
    return score

  def Grahamaitrimilan(asc1,asc2,moonplacement1,moonplacement2):
    def chandras(Ascendant,lord):
      tofind = Ascendant + lord
      place = roll(tofind)
      placed = place - 1
      chandrashi = Rashilords[placed]
      return chandrashi
    chandrashi1 = chandras(asc1,moonplacement1)
    chandrashi2 = chandras(asc2,moonplacement2)
    if (chandrashi1  in ["Moon","Mars","Mercury","Jupiter"]) and (chandrashi2 in ["Moon","Mars","Mercury","Jupiter"]):
      score = 5
    elif (chandrashi1 in ["Saturn","Venus","Mercury","Jupiter"]) and (chandrashi2 in ["Saturn","Venus","Mercury","Jupiter"]):
      score = 5
    else:
      score = 3
    return score
  def Ganamilan(nakshatra1,nakshatra2):
    nakshatra_gana = {
    'Ashwini': 'Deva',
    'Bharani': 'Manushya',
    'Krittika': 'Rakshasa',
    'Rohini': 'Manushya',
    'Mrigashira': 'Manushya',
    'Ardra': 'Rakshasa',
    'Punarvasu': 'Deva',
    'Pushya': 'Manushya',
    'Ashlesha': 'Rakshasa',
    'Magha': 'Rakshasa',
    'Purva Phalguni': 'Manushya',
    'Uttara Phalguni': 'Manushya',
    'Hasta': 'Deva',
    'Chitra': 'Rakshasa',
    'Swati': 'Deva',
    'Vishakha': 'Rakshasa',
    'Anuradha': 'Rakshasa',
    'Jyeshta': 'Rakshasa',
    'Mula': 'Rakshasa',
    'Purva Ashadha': 'Manushya',
    'Uttara Ashadha': 'Manushya',
    'Shravana': 'Deva',
    'Dhanishta': 'Rakshasa',
    'Shatabhisha': 'Rakshasa',
    'Purva Bhadrapada': 'Rakshasa',
    'Uttara Bhadrapada': 'Rakshasa',
    'Revati': 'Deva'
    }
    def get_nakshatra_gana(nakshatra):
      return nakshatra_gana.get(nakshatra, "Invalid Nakshatra")

    gana1 = get_nakshatra_gana(nakshatra1)
    gana2 = get_nakshatra_gana(nakshatra2)

    if gana1 == gana2:
      score = 6
    elif gana1 == "Rakshasa" and gana2 == "Deva":
      score = 1
    elif gana1 == "Deva" and gana2 == "Rakshasa":
      score = 0
    elif gana1 == "Deva" and gana2 == "Manushya":
      score = 5
    elif gana1 == "Manushya" and gana2 == "Deva":
      score = 3
    else:
      score = 0
    return score

  def Bhakootmilan(nakshatra1,nakshatra2):
    Nakscount1 = 0
    Nakscount2 = 0
    for i in nakshatras:
      Nakscount1 = Nakscount1 + 1
      if nakshatra1 == i:
        break
    for j in nakshatras:
      Nakscount2 = Nakscount2 + 1
      if nakshatra2 == j:
        break
    diff = abs(Nakscount1 - Nakscount2)
    if diff == 5 or diff == 9 :
      score = 0
    elif diff == 2 or diff == 12:
      score = 0
    elif diff == 6 or diff == 8:
      score = 0
    else:
      score = 7
    return score

  def Nadimilan(nakshatra1,nakshatra2):
    nakshatra_to_nadi = {
    'Ashwini': 'Adi',
    'Bharani': 'Adi',
    'Krittika': 'Adi',
    'Rohini': 'Adi',
    'Mrigashira': 'Adi',
    'Ardra': 'Adi',
    'Punarvasu': 'Adi',
    'Pushya': 'Adi',
    'Ashlesha': 'Adi',
    'Magha': 'Madhya',
    'Purva Phalguni': 'Madhya',
    'Uttara Phalguni': 'Madhya',
    'Hasta': 'Madhya',
    'Chitra': 'Madhya',
    'Swati': 'Madhya',
    'Vishakha': 'Madhya',
    'Anuradha': 'Madhya',
    'Jyeshta': 'Madhya',
    'Mula': 'Madhya',
    'Purva Ashadha': 'Antya',
    'Uttara Ashadha': 'Antya',
    'Shravana': 'Antya',
    'Dhanishta': 'Antya',
    'Shatabhisha': 'Antya',
    'Purva Bhadrapada': 'Antya',
    'Uttara Bhadrapada': 'Antya',
    'Revati': 'Antya'
    }
    def get_nadi(nakshatra):
      return nakshatra_to_nadi.get(nakshatra, "Invalid Nakshatra")
    nadi1 = get_nadi(nakshatra1)
    nadi2 = get_nadi(nakshatra2)

    if nadi1 != nadi2 :
      score = 8
    else:
      score = 0
    return score



  Varnascore = int(Varnamilan(nakshatra1,pada1,nakshatra2,pada2))
  Vashyascore = int(Vashyamilan(nakshatra1,nakshatra2))
  Taramilanscore = int(Taramilan(nakshatra1,nakshatra2))
  Yonimilanscore = int(Yonimilan(nakshatra1,nakshatra2))
  Grahamilanscore = int(Grahamaitrimilan(asc1,asc2,moonplacement1,moonplacement2))
  Ganamilanscore = int(Ganamilan(nakshatra1,nakshatra2))
  Bhakootmilanscore = int(Bhakootmilan(nakshatra1,nakshatra2))
  Nadimilanscore = int(Nadimilan(nakshatra1,nakshatra2))
  score = Varnascore + Vashyascore + Taramilanscore + Yonimilanscore + Grahamilanscore + Ganamilanscore + Bhakootmilanscore + Nadimilanscore

  print(score)

  return score






#Dasha time in years
vimshottara=(7,20,6,10,7,18,16,19,17)
#Planet time percentage
Suntime = 6/120*100
Moontime = 10/120*100
Marstime = 7/120*100
Mercurytime = 17/120*100
Venustime = 20/120*100
Jupitertime = 16/120*100
Saturntime = 19/120*100
Rahutime = 18/120*100
ketutime = 7/120*100

def Compato(*arg,**kwargs):
     def roll(num):
          house = num % 12
          if (house==0):
               num =  num - 12
          else:
               num = house
          return num

     def roll2(num):
          planet = num % 9
          if(planet == 0):
           num = num - 9
          else:
           num = planet
          return num
     
     def Nakshatracalculator(nakshatranum):
          nakshatraname = nakshatras[nakshatranum - 1]
         
          if nakshatraname == "Ashwini" or nakshatraname == "Magha" or nakshatraname == "Moola":
               Nlord = "Ketu"
          elif nakshatraname == "Bharani" or nakshatraname == "Purva Phalguni" or nakshatraname == "Purva Ashadha":
               Nlord = "Venus"
          elif nakshatraname == "Krittika" or nakshatraname == "Uttara Phalguni" or nakshatraname == "Uttara Ashadha":
               Nlord = "Sun"
          elif nakshatraname == "Rohini" or nakshatraname == "Hasta" or nakshatraname == "Shravana":
               Nlord = "Moon"
          elif nakshatraname == "Mrigashīrsha" or nakshatraname == "Chitra" or nakshatraname == "Dhanishta":
               Nlord = "Mars"
          elif nakshatraname == "Ardra" or nakshatraname == "Swati" or nakshatraname == "Shatabhisha":
               Nlord = "Rahu"
          elif nakshatraname == "Punarvasu" or nakshatraname == "Vishakha" or nakshatraname == "Purva Bhadrapada":
               Nlord = "Jupiter"
          elif nakshatraname == "Pushya" or nakshatraname == "Anuradha" or nakshatraname == "Uttara Bhadrapada":
               Nlord = "Saturn"
          elif nakshatraname == "Ashlesha" or nakshatraname == "Jyeshtha" or nakshatraname == "Revati":
               Nlord = "Mercury"
         
          return Nlord,nakshatraname
     def Vimshotcalculator(Wanted_Dasha):
          Counter = 0
          for i in Vimshot:
               Counter = Counter + 1
               print(i)
               Planet = i
               if Planet == Wanted_Dasha:
                    print("Match found at",Counter)
                    break
               else:
                    print("Not found")
          return Counter
     def Vimshottaracalculator(Counter):
          Years = 0
          Counter1 = 0
          Total = 0
          for i in vimshottara:
               Counter1 = Counter1 + 1
               if Counter1 == Counter :
                    Years = int(i)
          return Years
     
     def Jyotantar(Rashinamedb,moondeg):

          moondeg,moonmin = map(int,moondeg.split("."))
          Rashcounter = 0
          for Rashiname in Rashislist:
               Rashcounter = Rashcounter + 1
               if Rashiname == Rashinamedb:
                    break
          Degrees = moondeg
          Minute = moonmin
          Rashinumber = Rashcounter - 1
          cras = Rashinumber * 30
          cdega = cras + Degrees
          cdeg = cdega * 60
          cmin = cdeg + Minute
          print(cmin)
          rashi = float(cmin / 800)
          nakshatranum = int(cmin / 800 + 1)
          print("The Nakshatra number is", nakshatranum)
          rashika = str(rashi)
          rashi, deg = map(int, rashika.split("."))
          diff = cmin - (800 * rashi)
          print(diff)
          if diff <= 200:
               pada = 1
          elif 200 < diff <= 400:
               pada = 2
          elif 400 < diff <= 600:
               pada = 3
          elif 600 < diff <= 800:
               pada = 4
          print("The Nakshatra pada is", pada)
          bhogya = 800 - diff
          print("The Bhogya remaining is", bhogya)
          Nlord, nakshatraname = Nakshatracalculator(nakshatranum)
          Counter = Vimshotcalculator(Nlord)
          Kalah = Vimshottaracalculator(Counter)
          print(Kalah)
          Bhogyakalah = Kalah / 800 * bhogya
          print(Bhogyakalah)
          Salmah = str(Bhogyakalah)
          Sal, mah = map(int, Salmah.split("."))
          if Sal == 0:
               Mah = 0
          else:
               Mah = int(Bhogyakalah % Sal * 12)
          print(
               "The Person born in",
               nakshatraname,
               "Nakshatra of planet",
               Nlord,
               "Remaining bhogyakalh is",
               Sal,
               "years and",
               Mah,
               "months that sum up the person will have ",
               Nlord,
               "Mahadasha First From",
          )


          # Arrays to store values
          dashalist = []
          kallist = []

          Counter2 = Counter - 1
          Counter3 = Counter - 1

          for i in Vimshot:
               Counter4 = roll2(Counter3 + 1)
               if Counter4 == 0:
                    Counter4 = 9
               nextkal = Vimshottaracalculator(Counter4)
               nextdasha = Vimshot[roll2(Counter2)]

               # Store values in arrays
               dashalist.append(nextdasha)
               kallist.append(nextkal)

               print(nextdasha)
               print(nextkal)

               Counter2 = Counter2 + 1
               Counter3 = Counter3 + 1

          print(dashalist)
          print(kallist)

          return Sal,Mah,nakshatraname,pada,Nlord,dashalist,kallist
     moondegbychart = (document.getElementById('Moondeg').innerText)
     genderofchart = str(Element('gender').value)
     rashibychart = int(document.getElementById('asc').innerText)
     moonplacebychart = int(document.getElementById('Moonnum').innerText)
     def rashifinder(rashibychart,moonplace):      
               Ascendant = rashibychart
               lord = moonplace
               tofind = Ascendant + lord
               #Calling Function roll to get place
               place = roll(tofind)
               placed = place - 1
               return placed
     placed = rashifinder(rashibychart,moonplacebychart)
    

     
     rashiname = Rashislist[placed-1]
     
     def gendasign(genderofchart):
        if genderofchart == "Male":
            return "Female"
        elif genderofchart =="Female":
            return "Male"
        elif genderofchart == None:
           return "X"

     Sal,Mah,nakshatraname,pada1,Nlord,dashalist,kallist = Jyotantar(rashiname,moondegbychart)   
     
     username = document.getElementById('id2').innerText
     gender = gendasign(genderofchart)
     ascendant = int(document.getElementById('asc2').innerText)
     moon_placement = int(document.getElementById('Moonnum').innerText)
     moon_deg = (document.getElementById('Moondeg').innerText)
     print(f"Username: {username}, Gender: {gender}, Ascendant: {ascendant}, Moon Placement: {moon_placement}, Moon Degree: {moon_deg}")
     if genderofchart == "Female":
        recordnumber = username
        lagnar = int(ascendant)
        placedr = rashifinder(ascendant,moon_placement)
        rashinamer = Rashislist[placedr-1]
        Sal,Mah,nakshatranameofrecord,pada2,Nlord,dashalist,kallist = Jyotantar(rashinamer,str(moon_deg))
        nakshatranameofrecord 
        
        astakoot_milan_result = calculate_astakoot_milan(nakshatraname, nakshatranameofrecord,pada1,pada2,rashibychart,lagnar,moonplacebychart,moon_placement)
        astakoot_milan_result = int((int(astakoot_milan_result)/36) * 100 )
        result.innerText=(f"Your Birth Nakshatra is {nakshatraname} and Person's is {nakshatranameofrecord} Compaitibility is: {astakoot_milan_result}%" )
        

     elif genderofchart == "Male":
        recordnumber = username
        lagnar = int(ascendant)
        placedr = rashifinder(ascendant,moon_placement)
        rashinamer = Rashislist[placedr-1]
        Sal,Mah,nakshatranameofrecord,pada2,Nlord,dashalist,kallist = Jyotantar(rashinamer,str(moon_deg))
        nakshatranameofrecord 
        
        astakoot_milan_result = calculate_astakoot_milan( nakshatranameofrecord,nakshatraname,pada2,pada1,lagnar,rashibychart,moon_placement,moonplacebychart)
        astakoot_milan_result = int((int(astakoot_milan_result)/36) * 100 )
        result.innerText=(f"Your Birth Nakshatra is {nakshatraname} and Person's {nakshatranameofrecord} Compaitibility is: {astakoot_milan_result}%" )
     else:
        recordnumber = username
        lagnar = int(ascendant)
        placedr = rashifinder(ascendant,moon_placement)
        rashinamer = Rashislist[placedr-1]
        Sal,Mah,nakshatranameofrecord,pada2,Nlord,dashalist,kallist = Jyotantar(rashinamer,str(moon_deg))
        nakshatranameofrecord 
        
        astakoot_milan_result = calculate_astakoot_milan( nakshatranameofrecord,nakshatraname,pada2,pada1,lagnar,rashibychart,moon_placement,moonplacebychart)
        astakoot_milan_result = int((int(astakoot_milan_result)/36) * 100 )
        result.innerText= (f"Assign Gender please - Your Birth Nakshatra is {nakshatraname} and Person's {nakshatranameofrecord} Compaitibility is: {astakoot_milan_result}%" )

           
  
     
     
            