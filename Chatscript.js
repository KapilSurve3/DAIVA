async function sendMessage() {
    
    let userMessage = document.getElementById("chartcode").value.toLowerCase();
    let replymessage = " "

    if (userMessage == "namaste"){
        replymessage = "Namaste"
        displayMessage(userMessage, "user-message");
        displayMessage(replymessage, "bot-message");
        
    }
    else if (userMessage == "yes"){
        displayMessage(userMessage,"user-message")
    }
    else{
        replymessage = await getBotResponse(userMessage)
        console.log(replymessage) 
        displayMessage(userMessage, "user-message");
        displayMessage(replymessage, "bot-message");
        if (replymessage == "I can help you to find a most suitable career path."){
            replymessage = recommendcareer()
            displayMessage(replymessage, "bot-message");
        }
       
    }
    
}

async function startchat() {
    let id = document.getElementById("id2").value
    if (id == ""){
        displayMessage("You need to enter your ID ! i want to know.", "bot-message");
    }else{
        id = id - 1
    }
   
    
    fetchData(id);
}

// Function to display messages in the chat window
function displayMessage(message, className) {
    const chatScreen = document.getElementById('chat-screen');
    
    // Create a new message element
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', className);
    messageElement.innerText = message;
    
    // Add the message to the chat screen
    chatScreen.appendChild(messageElement);
    // Scroll to the bottom of the chat screen
    chatScreen.scrollTop = chatScreen.scrollHeight;
}


const sheetUrl = "https://script.google.com/macros/s/AKfycbxBqcrxK3qF0MzhgApEzTy_91rszFWNCP44mY-u_yIY1sRgdjqUkAuvRB8KA5ncoqTtLw/exec"; // Replace with your deployed Apps Script URL

async function fetchData(id) {
    try {
        let response = await fetch(sheetUrl);
        let data = await response.json();

        console.log(data); // Check the entire data structure
        console.log(data[0]); // Check the first record
        console.log(data[0].value); // Check the object inside value
        console.log("First record:", data[0]);
        console.log("Type of first record:", typeof data[0]);
        function convertToCSV(data) {
            if (!data || data.length === 0) {
                console.error("No data available to convert.");
                return '';
            }
        
            console.log("First record:", data[0]);
            console.log("Type of first record:", typeof data[0]);
        
            const headers = Object.keys(data[0]);
            console.log("Headers:", headers);
        
            const rows = data.map(record => {
                console.log("Current record:", record);
                return headers.map(header => {
                    const value = record[header] ?? '';
                    console.log(`Value for ${header}:`, value);
                    return value;
                });
            });
        
            console.log("Rows:", rows);
        
            const csv = [
                headers.join('~'), // Header row
                ...rows.map(row => row.join('~')) // Data rows
            ].join('|');
        
            console.log("Final CSV:", csv);
            console.log(typeof(csv))
            return csv;
        }
        const csvfile = convertToCSV(data)
        const dataofpeople = document.getElementById('datasetsofpeople')
        dataofpeople.innerText = csvfile

        if (Array.isArray(data) && id >= 0 && id < data.length) {
            let record = data[id]; // Ensure id is valid
            let recordEntries = Object.entries(record);
            
            console.log("Headers:", Object.keys(record));
            console.log("Record:", recordEntries);

            const backdata = document.getElementById('output');
            backdata.innerText = JSON.stringify(record, null, 2); // Pretty print JSON
            


           




        } else {
            console.error("Invalid ID or no data found");
        }
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}





//This part is entire chatbot which include tokenization response processing etc

async function getBotResponse(userMessage) {
    // Load the intents JSON file
    const response = await fetch('intents.json');
    const data = await response.json();
    
    if (data.intents) {
        let maxSimilarity = 0;
        let bestResponse = "Sorry, I didn't understand that. Can you please ask something else?";

        // Loop through each intent to check similarity with the user message
        for (let i = 0; i < data.intents.length; i++) {
            let similarityScore = 0;
            let tag = data.intents[i].tag;
            let patterns = data.intents[i].patterns;
            
            // Calculate similarity for each pattern
            for (let pattern of patterns) {
                similarityScore = checkPatternMatch(userMessage, pattern);
                
                // Log the similarity score for debugging
                console.log(`Comparing: ${userMessage} with pattern: ${pattern}`);
                console.log(`Similarity Score: ${similarityScore}`);

                // If the current pattern has a higher similarity score, update the best response
                if (similarityScore > maxSimilarity) {
                    maxSimilarity = similarityScore;
                    bestResponse = data.intents[i].responses[Math.floor(Math.random() * data.intents[i].responses.length)];
                }
            }
        }
        
        // Return the best response with the highest similarity
        return bestResponse;
    }
    
    // Default response if no match is found
    return "Sorry, I didn't understand that. Can you please ask something else?";
}

// Function to calculate similarity using Jaccard index
function checkPatternMatch(userMessage, pattern) {
    // Tokenize the user message and pattern properly, excluding stopwords
    let messageTokens = cleanAndTokenize(userMessage);
    let patternTokens = cleanAndTokenize(pattern);

    console.log("Message Tokens:", messageTokens);
    console.log("Pattern Tokens:", patternTokens);

    // Find the intersection between the message and the pattern tokens
    let intersection = messageTokens.filter(token => patternTokens.includes(token));

    // Calculate the union of the two sets
    let union = new Set([...messageTokens, ...patternTokens]);  // Union of the two sets

    console.log("Intersection:", intersection);
    console.log("Union:", [...union]);

    // Calculate the Jaccard similarity score
    let similarity = intersection.length / union.size;

    console.log("Jaccard Similarity:", similarity);

    // Return the similarity score
    return similarity;
}

// List of stopwords to exclude
const stopwords = new Set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", 
    "aren't", "aren", "as", "at", "be", "because", "been", "before", "being", "below", "between", 
    "both", "but", "by", "can't", "cannot", "could", "couldn't", "couldnt", "can't", "did", "didn't", 
    "do", "does", "doesn't", "don't", "doing", "don't", "during", "each", "few", "for", "from", "further", 
    "had", "hadn't", "hadnt", "has", "hasn't", "have", "haven't", "having", "here", "here's", "hereafter", 
    "hereby", "herein", "here's", "hereupon", "how", "how's", "how", "how's", "however", "i", "i'm", "i've", 
    "if", "if's", "in", "in", "into", "is", "isn't", "isn't", "isn't", "isn't", "it", "it's", "it'd", "it'll",
    "isn't", "hasn't", "it", "it's", "it's", "no", "nor", "not", "of", "off", "on", "on", "onto", "or", "other", 
    "ought", "our", "ours", "ourselves", "over", "own", "same", "so", "so", "such", "than", "that", "that", "that", 
    "the", "the's", "than", "that", "that's", "that", "theirs", "them", "they", "they're", "they've", "this", "this", 
    "that", "those", "themselves"
]);

function cleanAndTokenize(text) {
    // Convert to lowercase, remove punctuation, and split by spaces
    return text.toLowerCase()
               .replace(/[^\w\s]/g, '')  // Remove punctuation
               .split(/\s+/)  // Split by spaces
               .filter(Boolean)  // Remove empty strings
               .filter(token => !stopwords.has(token));  // Remove stopwords
}


//This part start for all the career recommendation stuff

function recommendcareer() {
    let patternText = document.getElementById("output").innerText;

    if (!patternText) {
        console.error("No data available in output!");
        return "";
    }

    try {
        let record = JSON.parse(patternText); // Parse JSON correctly
        let jobs = Object.entries(record)
            .filter(([key, value]) => key.startsWith("Job_") && value)
            .map(([key, value]) => `${key}: ${value}`);

        return jobs.length ? jobs.join(", ") : "No jobs found.";
    } catch (error) {
        console.error("Error processing data:", error);
        return "";
    }
}
