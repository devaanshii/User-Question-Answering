import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class KnowledgeBase:
    def __init__(self):
        self.qa_data = self._load_knowledge_base()
        self.vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
        self.question_vectors = None
        self._prepare_vectors()
        
    def _load_knowledge_base(self):
        """Load the general knowledge Q&A database"""
        qa_pairs = [
            # Science
            ("What is the chemical symbol for gold?", "The chemical symbol for gold is Au."),
            ("What is the speed of light?", "The speed of light is approximately 299,792,458 meters per second."),
            ("How many bones are there in an adult human body?", "An adult human body has 206 bones."),
            ("What is the largest planet in our solar system?", "Jupiter is the largest planet in our solar system."),
            ("What gas do plants absorb from the atmosphere during photosynthesis?", "Plants absorb carbon dioxide (CO2) from the atmosphere during photosynthesis."),
            ("What is the hardest natural substance on Earth?", "Diamond is the hardest natural substance on Earth."),
            ("What is the smallest unit of matter?", "The atom is the smallest unit of matter."),
            ("What is the boiling point of water at sea level?", "The boiling point of water at sea level is 100°C or 212°F."),
            
            # Geography
            ("What is the capital of France?", "The capital of France is Paris."),
            ("Which is the longest river in the world?", "The Nile River is the longest river in the world."),
            ("What is the smallest country in the world?", "Vatican City is the smallest country in the world."),
            ("Which continent has the most countries?", "Africa has the most countries with 54 nations."),
            ("What is the highest mountain in the world?", "Mount Everest is the highest mountain in the world."),
            ("Which ocean is the largest?", "The Pacific Ocean is the largest ocean."),
            ("What is the capital of Australia?", "The capital of Australia is Canberra."),
            ("Which desert is the largest in the world?", "The Sahara Desert is the largest hot desert in the world."),
            
            # History
            ("Who was the first person to walk on the moon?", "Neil Armstrong was the first person to walk on the moon."),
            ("In which year did World War II end?", "World War II ended in 1945."),
            ("Who painted the Mona Lisa?", "Leonardo da Vinci painted the Mona Lisa."),
            ("Which ancient wonder of the world was located in Alexandria?", "The Lighthouse of Alexandria was located in Alexandria."),
            ("Who was the first President of the United States?", "George Washington was the first President of the United States."),
            ("In which year did the Berlin Wall fall?", "The Berlin Wall fell in 1989."),
            
            # General Knowledge
            ("How many days are there in a leap year?", "There are 366 days in a leap year."),
            ("What is the largest mammal in the world?", "The blue whale is the largest mammal in the world."),
            ("How many continents are there?", "There are 7 continents in the world."),
            ("What is the currency of Japan?", "The currency of Japan is the Yen."),
            ("How many sides does a hexagon have?", "A hexagon has 6 sides."),
            ("What is the most spoken language in the world?", "Mandarin Chinese is the most spoken language in the world."),
            ("What is the smallest prime number?", "2 is the smallest prime number."),
            ("How many minutes are there in a full day?", "There are 1,440 minutes in a full day."),
            
            # Sports
            ("How often are the Summer Olympic Games held?", "The Summer Olympic Games are held every 4 years."),
            ("In which sport would you perform a slam dunk?", "You would perform a slam dunk in basketball."),
            ("How many players are on a soccer team on the field at one time?", "There are 11 players on a soccer team on the field at one time."),
            ("What is the maximum score possible in ten-pin bowling?", "The maximum score possible in ten-pin bowling is 300."),
            
            # Literature and Arts
            ("Who wrote 'Romeo and Juliet'?", "William Shakespeare wrote 'Romeo and Juliet'."),
            ("What is the first book in the Harry Potter series?", "The first book in the Harry Potter series is 'Harry Potter and the Philosopher's Stone' (or 'Sorcerer's Stone' in the US)."),
            ("Who composed 'The Four Seasons'?", "Antonio Vivaldi composed 'The Four Seasons'."),
            
            # Technology
            ("What does 'WWW' stand for?", "WWW stands for World Wide Web."),
            ("Who founded Microsoft?", "Bill Gates and Paul Allen founded Microsoft."),
            ("What does 'AI' stand for?", "AI stands for Artificial Intelligence."),
            ("In what year was the first iPhone released?", "The first iPhone was released in 2007."),
        ]
        
        return pd.DataFrame(qa_pairs, columns=['question', 'answer'])
    
    def _preprocess_text(self, text):
        """Preprocess text for better matching"""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text
    
    def _prepare_vectors(self):
        """Prepare TF-IDF vectors for all questions"""
        processed_questions = [self._preprocess_text(q) for q in self.qa_data['question']]
        self.question_vectors = self.vectorizer.fit_transform(processed_questions)
    
    def find_best_answer(self, user_question, threshold=0.1):
        """Find the best matching answer for user question"""
        processed_question = self._preprocess_text(user_question)
        question_vector = self.vectorizer.transform([processed_question])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(question_vector, self.question_vectors).flatten()
        best_match_idx = np.argmax(similarities)
        best_score = similarities[best_match_idx]
        
        if best_score > threshold:
            return {
                'answer': self.qa_data.iloc[best_match_idx]['answer'],
                'confidence': round(best_score * 100, 2),
                'matched_question': self.qa_data.iloc[best_match_idx]['question']
            }
        else:
            return {
                'answer': "I'm sorry, I don't have information about that topic in my knowledge base. Please try asking about science, geography, history, sports, technology, or general knowledge topics.",
                'confidence': 0,
                'matched_question': None
            }
    
    def get_random_questions(self, n=5):
        """Get random questions for suggestions"""
        return self.qa_data['question'].sample(n=min(n, len(self.qa_data))).tolist()
    
    def get_all_categories(self):
        """Get example questions by category"""
        categories = {
            "Science": [
                "What is the chemical symbol for gold?",
                "What is the speed of light?",
                "How many bones are there in an adult human body?"
            ],
            "Geography": [
                "What is the capital of France?",
                "Which is the longest river in the world?",
                "What is the smallest country in the world?"
            ],
            "History": [
                "Who was the first person to walk on the moon?",
                "In which year did World War II end?",
                "Who painted the Mona Lisa?"
            ],
            "Sports": [
                "How often are the Summer Olympic Games held?",
                "In which sport would you perform a slam dunk?",
                "How many players are on a soccer team?"
            ]
        }
        return categories
