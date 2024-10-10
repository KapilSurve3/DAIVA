'''from js import document
from js import window
def Chatter(*arg,**kwargs):
    result = document.getElementById('mainoutput')
    text = document.getElementById('chartcode').value
    text = text.lower()
    textlist = text.split()
    resultext = " "   
    
    for text in textlist:
        if text == "hello":
            resultext = resultext + "Hi, "
        elif text == "marriage":
            resultext = resultext + "The potential husband and wife are displayed in predictions"
        elif text == "sad": 
            resultext = resultext +"Yeah sad."
        result.innerText = resultext

from js import document, window

def preprocess_document(doc):
    # This converts the document text to lowercase and splits it into lines
    return doc.lower().split('\n')

# Function to search for a query within the processed document
def search_document(query, processed_document):
    query = query.lower()  # Ensure the query is also in lowercase
    # Loop through each line of the document
    for line in processed_document:
        if query in line:
            return line  # Return the line that matches the query
    return "Sorry, I don't have an answer for that."  # Return if no match is found

# Function to be called when the user interacts (e.g., button click)
def Chatter(*arg, **kwargs):
    # Get the file content from a <textarea> (or other input field)
    document_text = document.getElementById('fileContent').value  # Ensure 'fileContent' is a <textarea> or input with text
    
    # Preprocess the document text into a list of lines
    processed_document = preprocess_document(document_text)
    
    # Get the user's query (text from another input field, e.g., 'chartcode')
    query_text = document.getElementById('chartcode').value
    
    # Search the document for the query
    answer = search_document(query_text, processed_document)
    
    # Display the result in the element with id 'mainoutput'
    result = document.getElementById('mainoutput')
    result.innerText = answer '''

from js import document


# Function to preprocess the document text
def preprocess_document(doc):
    return doc.lower().split('.')

# Function to search for a query within the processed document

# Function to classify the question type
def classify_question(query):
    query = query.lower()
    if query.startswith('what'):
        return 'what'
    elif query.startswith('who'):
        return 'who'
    elif query.startswith('how'):
        return 'how'
    elif query.startswith('when'):
        return 'when'
    return 'general'

# Function to search the document based on query and return the most relevant answer
def search_document(query, processed_document):
    query_type = classify_question(query)  # Classify the type of question
    query_words = query.lower().split(" ")    # Tokenize the query into words
    
    # Basic keyword-based search to find a matching line
    for line in processed_document:
        # If the query type is 'what', look for definitions or explanations
        if query_type == 'what' and any(word in line for word in query_words):
            return line  # Return the first matching line
        
        # If the query type is 'who', you might match people-related keywords
        elif query_type == 'who' and 'who' in line:
            return line
        
        # General keyword matching as fallback
        elif any(word in line for word in query_words):
            return line  # Return the first matching line
    
    # If no match is found, return a default message
    return "Sorry, I couldn't find an answer."

# Function to handle the chat interaction
def Chatter(*arg, **kwargs):
    # Get the content of the hidden textarea (simulating the file content)
    document_text = document.getElementById('fileContent').value
    processed_document = preprocess_document(document_text)
    
    # Get the user's message from the input field
    query_text = document.getElementById('chartcode').value
    
    # Process and search for the answer (only return one relevant line)
    answer = search_document(query_text, processed_document)
    
    # Display the user's message and bot's answer on the chat screen
    display_message(query_text, "user-message")
    display_message(answer, "bot-message")

# Function to display messages in the chat window
def display_message(message, className):
    chat_screen = document.getElementById('chat-screen')
    
    # Create a new message element
    message_element = document.createElement('div')
    message_element.classList.add('chat-message', className)
    message_element.innerText = message
    
    # Add the message to the chat screen
    chat_screen.appendChild(message_element)
    
    # Scroll to the bottom of the chat screen
    chat_screen.scrollTop = chat_screen.scrollHeight


