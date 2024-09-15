const Sunln = document.getElementById("Sunnum");
const Moonln = document.getElementById("Moonnum");
const Mercuryln = document.getElementById("Mercurynum");
const Venusln = document.getElementById("Venusnum");
const Marsln = document.getElementById("Marsnum");
const Jupiterln = document.getElementById("Jupiternum");
const Saturnln = document.getElementById("Saturnnum");
const Rahuln = document.getElementById("Rahunum");
const Ketuln = document.getElementById("Ketunum");

const result = document.getElementById("Report");

const lagnan = document.getElementById("asc");

//Audio segment
function playAudio() {
    var audio = document.getElementById("myAudio");
    audio.play();
  }
function playAudio2() {
    var audio = document.getElementById("myAudio2");
audio.play();
}
function playAudio3(){
    var audio = document.getElementById("myAudio3");
    audio.play();
}


function Predict()
{playAudio()
    var relatedto = "Unknown";
    var lagnalord = ""
    if(lagnan.innerText == "1"|| lagnan.innerText == "8")
    {
        lagnalord = "Mars"; 
        
    }
    else if(lagnan.innerText == "2"||lagnan.innerText =="7")
    {
        lagnalord = "Venus";  
        
    }
    else if(lagnan.innerText == "3"||lagnan.innerText =="6")
    {
        lagnalord = "Mercury";  
        
    }
    else if(lagnan.innerText == "4")
    {
        lagnalord = "Moon"; 
       
    }
    else if(lagnan.innerText == "5")
    {
        lagnalord = "Sun";  
        
    }
    else if(lagnan.innerText == "9"||lagnan.innerText =="12")
    {
        lagnalord = "Jupiter";  
        
    }
    else if(lagnan.innerText == "10"||lagnan.innerText =="11")
    {
        lagnalord = "Saturn";  
       
    }
//For Career
    if(lagnan.innerText == "4"|| lagnan.innerText == "11")
    {
        lord = "Mars"; 
        result.innerText = lord
    }
    else if(lagnan.innerText == "5"||lagnan.innerText =="10")
    {
        lord = "Venus";  
        result.innerText = lord
    }
    else if(lagnan.innerText == "6"||lagnan.innerText =="9")
    {
        lord = "Mercury";  
        result.innerText = lord
    }
    else if(lagnan.innerText == "7")
    {
        lord = "Moon"; 
        result.innerText = lord 
    }
    else if(lagnan.innerText == "8")
    {
        lord = "Sun";  
        result.innerText = lord
    }
    else if(lagnan.innerText == "12"||lagnan.innerText =="3")
    {
        lord = "Jupiter";  
        result.innerText = lord
    }
    else if(lagnan.innerText == "1"||lagnan.innerText =="2")
    {
        lord = "Saturn";  
        result.innerText = lord
    }

// This is function to get all lord position in chart
    if (true)
    {
    var nameofplanet = result.innerText;
    const idcreated = nameofplanet.concat('num') ;
    var placementplanet = document.getElementById(idcreated);
    result.innerText = placementplanet.innerText + lord
    }

// Creating positional importance or related data
    if (placementplanet.innerText == 1)
    {
        relatedto = "Self ,Personality ,Influencing"
    }
    else if (placementplanet.innerText == 2)
    {
        relatedto = "Family Buisness ,Food ,Finance"
    }
    else if (placementplanet.innerText == 3)
    {
        relatedto = "Marketing ,Enterprenur ,Sales ,Communication"
    }
    else if (placementplanet.innerText== 4)
    {
        relatedto = "Home ,Real-Estate ,Homefurnish ,Automobiles"
    }
    else if (placementplanet.innerText == 5)
    {
        relatedto ="Thrill ,Adventure ,Risk ,Education ,Stockmarket ,Engineering"
    }
    else if (placementplanet.innerText == 6)
    {
        relatedto = "Routined job ,Lawyer ,Medical ,Bank ,Socialwork ,Armed Service"
    }
    else if (placementplanet.innerText == 7)
    {
        relatedto = "Buisness ,Partnership ,Marriage ,Councils"
    }
    else if (placementplanet.innerText == 8)
    {
        relatedto =  "Research ,Investigation ,Farming ,Occult Science"
    }
    else if (placementplanet.innerText == 9)
    {
        relatedto = "Masterdegree ,Phd ,Religion ,Spirituality ,HigherLearning"
    }
    else if (placementplanet.innerText == 10)
    {
        relatedto = "Authority ,Goverment ,Father"
    }
    else if (placementplanet.innerText == 11)
    {
        relatedto= "Big Companies ,Enterprenur ,Humanity ,Huge Organisation"
    }
    else if (placementplanet.innerText == 12)
    {
        relatedto = "Foreign ,Hospital ,Prison ,Spiritual ,Ashrams"
    }
    //this part is for getting type of work field
    if (lord== "Mars")
    {
        fieldof = "Armed Services ,Mechanics ,MartialArts ,Engineering ,Real-Estate ,Land ,Physical-Land-Competetion "
    } 
    else if (lord =="Moon")
    {
        fieldof ="Doctor ,Surgeon ,Accountant ,Psycology ,Writer ,Caretaker ,Water-Milk "
    }
    else if (lord == "Mercury")
    {
        fieldof="Communications ,Sales ,Promoting ,Journalism ,press ,Negotiations ,Computer ,Buisness"
    }
    else if (lord =="Venus")
    {
        fieldof="Arts ,Creativity ,Drama ,Games ,Beauty ,Fashion ,Women-products ,Entertainment ,Finance"
    }
    else if (lord =="Jupiter")
    {
        fieldof="Teaching ,Spirituality ,Religion ,HigherLearning ,Education ,Technology ,Research"
    }
    else if (lord =="Saturn")
    {
        fieldof ="Farming ,Labour ,Hardworking ,Engineering ,Civil-work"
    }
    else if (lord =="Sun")
    {
        fieldof ="Goverment ,Adminsitration ,Law and order ,Politics"
    }
//This part is core logic building
//Checking the core aim of the person
const lagnalordplace = lagnalord.concat('num');
const lagnalordplacement = document.getElementById(lagnalordplace);
    if (lagnalordplacement.innerText == 1)
    {
     aim = "Building personality & Self"
    }
     else if (lagnalordplacement.innerText == 2)
    {
     aim = "Generating Wealth ,Looking in family"
    }
    else if (lagnalordplacement.innerText == 3)
    {
     aim = "Bravery ,Relations with Siblings ,Impacting masses"
    }
    else if (lagnalordplacement.innerText == 4)
    {
     aim = "land ,House ,Cars ,Automobiles ,Mother"
    }
    else if (lagnalordplacement.innerText == 5)
    {
     aim = "Creative self expression ,Kids ,Education"
    }
    else if (lagnalordplacement.innerText == 6)
    {
     aim = "Competetion ,Atorney ,Dealing with Enemies ,Medical"
    }
    else if (lagnalordplacement.innerText == 7)
    {
     aim = "Partner ,Buisness ,Marriage ,Love"
    }
    else if (lagnalordplacement.innerText == 8)
    {
     aim = "Investigation ,Secretplaces ,Sudden moments"
    }
    else if (lagnalordplacement.innerText == 9)
    {
     aim = "Dharma ,Righteosness ,Religion ,Philosophy ,Higherlearning"
    }
    else if (lagnalordplacement.innerText == 10)
    {
     aim = "Career ,Goverment ,Fame ,Father"
    }
    else if (lagnalordplacement.innerText == 11)
    {
     aim = "Social Circle ,Friends ,Organisations ,Gaining income "
    }
    else if (lagnalordplacement.innerText == 12)
    {
     aim = "Foreign ,Spiritual ,Another dimensions"
    }


// Rahu conditions to check for technical education

let n = parseInt(lagnan.innerText);
let k = n-1;
let rahupostin = parseInt(Rahuln.innerText);
let Rahupos = rahupostin + k;

if (Rahupos == 1|| Rahupos ==13) 
{
keywordrahu = "Technical interest related to Engineering ,Mechanics ,Machine Related works ,Metallurgy ,Computer ,IT."
}
else if (Rahupos == 2 || Rahupos == 14)
{
keywordrahu="Technical interest related to creative and Program building ,AIML ,Visual Arts ,Graphics designing ,UI Developement,Game Developement."
} 
else if (Rahupos ==3|| Rahupos == 15) 
{        
keywordrahu ="Technical interest related to IT ,Fintech ,Computer Software ,Online Communication ,Website Developement."
}
else if (Rahupos ==8 || Rahupos == 20)
{
keywordrahu ="This person might get a bit difficult in purusing technical education."
}
else
{
keywordrahu = "..Normal technical knowledge"
}

//This Part Displays the Love Prediction
if(lagnan.innerText == "1"|| lagnan.innerText == "8")
    {
        partlord = "Venus"; 
    }
    else if(lagnan.innerText == "2"||lagnan.innerText =="7")
    {
        partlord = "Mars";    
    }
    else if(lagnan.innerText == "3"||lagnan.innerText =="6")
    {
        partlord = "Jupiter";    
    }
    else if(lagnan.innerText == "4")
    {
        partlord = "Saturn";    
    }
    else if(lagnan.innerText == "5")
    {
        partlord = "Saturn";     
    }
    else if(lagnan.innerText == "9"||lagnan.innerText =="12")
    {
        partlord = "Mercury";  
    }
    else if(lagnan.innerText == "10")
    {
        partlord = "Moon";     
    }
    else if(lagnan.innerText == "11")
    {
        partlord = "Sun";     
    }
    const partlordplace = partlord.concat('num');
    const partlordplacement = document.getElementById(partlordplace);
   
    if (partlordplacement.innerText == 1)
    {
     partner = "Spouse will have most influence on your personality and decision making ,Chances of Early marriage."
    }
     else if (partlordplacement.innerText == 2)
    {
     partner = "Wealth through marriage ,Your spouse will have good family background ,Higher chances the partner will enhance your wealth."
    }
    else if (partlordplacement.innerText == 3)
    {
     partner = "You like your partner will be quite philsophical ,Major influence on your duty ,Your spouse is in association with friends of sibling ,Newspaper ,Travels."
    }
    else if (partlordplacement.innerText == 4)
    {
     partner = "Your partner will help you to gain House/cars ,You may like a partner who has all comfort of life ,Good moraled spouse."
    }
    else if (partlordplacement.innerText == 5)
    {
     partner = "Pretty Romantic relationship ,Knowlegeable ,well-educated partner, Performing arts"
    }
    else if (partlordplacement.innerText == 6)
    {
     partner = "Same career choices ,might be from foreign origin or different cultural background ,spouse can be a doctor/lawyer or a social worker."
    }
    else if (partlordplacement.innerText == 7)
    {
     partner = "Trustworthy and Dependable spouse, Stable married life ,Overall your spouse will help you in good relations with areas in diplomacy and people."
    }
    else if (partlordplacement.innerText == 8)
    {
     partner = "Marriage will bring Transformation ,Secretive/Private married life ,Spouse might be working in the field of Research / Mysticism."
    }
    else if (partlordplacement.innerText == 9)
    {
     partner = "Well-Educated Spouse ,Travelling be a keypoint in your relation ,Can meet when you are travelling long ,Discussion about higher knowledge is base in this relation."
    }
    else if (partlordplacement.innerText == 10)
    {
     partner = "Spouse will be of higher status ,Career will be a adjoin base of your relation ,Spouse can be famous."
    }
    else if (partlordplacement.innerText == 11)
    {
     partner = "What you will desire will be fullfilled after marriage ,Spouse will bring money in your life ,your Partner can be part of huge social organisation ,Working for people ,Fun marriage"
    }
    else if (partlordplacement.innerText == 12)
    {
     partner = "Spouse of foreign origin ,Settling foreign lands after marriage is high ,Spiritual Spouse ,Might be working in Research/Hospital/Spiritual/Airport sectors."
    }
//this part is for motherlord
if(lagnan.innerText == "1")
    {
        motherlord = "moon"; 
    }
    else if(lagnan.innerText == "2")
    {
        motherlord = "Sun";    
    }
    else if(lagnan.innerText == "3"||lagnan.innerText =="12")
    {
        motherlord = "Mercury";    
    }
    else if(lagnan.innerText == "4"||lagnan.innerText =="11")
    {
        motherlord = "Venus";    
    }
    else if(lagnan.innerText == "5"||lagnan.innerText=="10")
    {
        motherlord = "Mars";     
    }
    else if(lagnan.innerText == "6"||lagnan.innerText =="9")
    {
        motherlord = "Jupiter";  
    }
    else if(lagnan.innerText == "7"||lagnan.innerText =="8")
    {
        motherlord = "Saturn";     
    }
    const motherlordplace = motherlord.concat('num');
    const motherlordplacement = document.getElementById(motherlordplace);
//This part is for ayabhav
if(lagnan.innerText == "1"||lagnan.innerText =="12")
    {
        ayalord = "Saturn"; 
    }
    else if(lagnan.innerText == "2"||lagnan.innerText =="11")
    {
        ayalord = "Jupiter";    
    }
    else if(lagnan.innerText == "3"||lagnan.innerText =="10")
    {
        ayalord = "Mars";    
    }
    else if(lagnan.innerText == "4"||lagnan.innerText =="9")
    {
        ayalord = "Venus";    
    }
    else if(lagnan.innerText == "5"||lagnan.innerText=="8")
    {
        ayalord = "Mercury";     
    }
    else if(lagnan.innerText == "6")
    {
        ayalord = "Moon";  
    }
    else if(lagnan.innerText == "7")
    {
        ayalord = "Sun";     
    }

    else if(lagnan.innerText == "11")
    {
        ayalord = "Mercury";     
    }

    const ayalordplace = ayalord.concat('num');
    const ayalordplacement = document.getElementById(ayalordplace);
//this is for bhagyalord
if(lagnan.innerText == "1"||lagnan.innerText =="4")
    {
        bhagyalord = "Jupiter";
    }
    else if(lagnan.innerText == "2"||lagnan.innerText=="3")
    {
        bhagyalord = "Saturn";    
    }
    else if(lagnan.innerText == "12"||lagnan.innerText =="5")
    {
        bhagyalord = "Mars";    
    }
    else if(lagnan.innerText == "11"||lagnan.innerText=="6")
    {
        bhagyalord = "Venus";    
    }
    else if(lagnan.innerText == "10"||lagnan.innerText=="7")
    {
        bhagyalord = "Mercury";     
    }
    else if(lagnan.innerText == "9")
    {
        bhagyalord = "Sun";  
    }
    else if(lagnan.innerText == "8")
    {
        bhagyalord = "Moon";     
    }
    const bhagyalordplace = bhagyalord.concat('num');
    const bhagyalordplacement = document.getElementById(bhagyalordplace);
//this is for sukhlord
if(lagnan.innerText == "1")
    {
        sukhlord = "Sun"
    }
    else if(lagnan.innerText == "12")
    {
        sukhlord = "Moon";    
    }
    else if(lagnan.innerText == "11"||lagnan.innerText =="2")
    {
        sukhlord = "Mercury";    
    }
    else if(lagnan.innerText == "10"||lagnan.innerText =="3")
    {
        sukhlord = "Venus";    
    }
    else if(lagnan.innerText == "9"||lagnan.innerText=="4")
    {
        sukhlord = "Mars";     
    }
    else if(lagnan.innerText == "8"||lagnan.innerText =="5")
    {
        sukhlord = "Jupiter";  
    }
    else if(lagnan.innerText == "7"||lagnan.innerText=="6")
    {
        sukhlord = "Saturn";     
    }
    const sukhlordplace = sukhlord.concat('num');
    const sukhlordplacement = document.getElementById(sukhlordplace);
//This part is for Kundaliyoga


//This part Displays the result
    result.innerText = "The Predictions for the chart is :\n\n\n";
    result.innerText = result.innerText+"*The Work Enviorment and Possible choices*:\n\n";
    result.innerText = result.innerText+ "The Native's work enviorment is in the field of"+" "+fieldof+" "+"which will be related to"+" "+ relatedto;
    result.innerText = result.innerText +"This person will have their major lookout for "+ aim +"\n Apart from this the person has "+ keywordrahu;
    result.innerText = result.innerText + "\n\n\n *The Marriage and Spouse Predictions*:\n\n"
    result.innerText = result.innerText + "The Native's love life would be: "+partner;
    result.innerText = result.innerText + "\n\n *Benefic Yog occuring in your chart are *\n:"+goodyog;
    result.innerText = result.innerText + "\n *Malefic Yog occuring in your chart are *\n:"+badyog;
}

//tHIS PART IS Translation
let isTranslated = false;

document.getElementById('pbutton').addEventListener('click', function() {
    const img = document.getElementById('pbuttonimg');
    const button = document.getElementById('pbutton');
    const panel = document.getElementById('commandpanel');
    const bottomFixed = document.getElementById('bottom-fixed');

    if (!isTranslated) {
        // Translate all elements by 30% on Y-axis
        img.style.transform = 'translateY(-450%)';
        button.style.transform = 'translateY(-450%)';
        panel.style.transform = 'translateY(-90%)';
        bottomFixed.style.transform = 'translateY(-340%)';
    } else {
        // Reset to original position
        img.style.transform = 'translateY(5%)';
        button.style.transform = 'translateY(5%)';
        panel.style.transform = 'translateY(0)';
        bottomFixed.style.transform = 'translateY(0)';
    }

    // Toggle the state
    isTranslated = !isTranslated;
});
