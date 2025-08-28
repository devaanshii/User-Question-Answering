# 🧠 User Question Answering System

A smart AI-powered question-answering system built with Python and Streamlit that can answer general knowledge questions across multiple categories including Science, Geography, History, Sports, Technology, and Literature.

## 🌟 Features

- **Intelligent Question Matching**: Uses TF-IDF vectorization and cosine similarity for accurate question matching
- **Multi-Category Knowledge Base**: Covers Science, Geography, History, Sports, Technology, and Literature
- **Confidence Scoring**: Shows how confident the system is about each answer
- **Interactive Web Interface**: Clean, user-friendly Streamlit interface
- **Random Question Suggestions**: Get random questions to explore the knowledge base
- **Category-wise Question Browser**: Browse questions by specific categories
- **Real-time Processing**: Fast response times with cached knowledge base

## 🚀 Live Demo

![Q&A System Demo](https://via.placeholder.com/800x400/1f77b4/ffffff?text=General+Knowledge+Q%26A+System)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Features Overview](#features-overview)
- [Knowledge Base Categories](#knowledge-base-categories)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/general-knowledge-qa-system.git
cd general-knowledge-qa-system
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download NLTK Data

The application will automatically download required NLTK data on first run, but you can also do it manually:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage

### Running the Application

1. Navigate to the project directory
2. Activate your virtual environment (if using one)
3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Open your web browser and go to `http://localhost:8501`

### Using the Q&A System

1. **Ask a Question**: Type your question in the input box
2. **Get Answer**: Click "Get Answer" or press Enter
3. **View Results**: See the answer, confidence score, and matched question
4. **Explore Categories**: Use the sidebar to browse questions by category
5. **Try Random Questions**: Click "Get Random Questions" for inspiration

### Example Questions

- "What is the capital of France?"
- "Who was the first person to walk on the moon?"
- "What is the chemical symbol for gold?"
- "How many players are on a soccer team?"
- "What does AI stand for?"

## Project Structure

```
general-knowledge-qa-system/
│
├── app.py                 # Main Streamlit application
├── knowledge_base.py      # Knowledge base and AI logic
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file (optional)
```

### File Descriptions

- **`app.py`**: Main Streamlit application with UI components and user interaction logic
- **`knowledge_base.py`**: Core logic for question matching, text processing, and answer retrieval
- **`requirements.txt`**: List of Python packages required to run the application

## 🔍 How It Works

### 1. Text Preprocessing
- Converts text to lowercase
- Removes punctuation and extra whitespace
- Tokenizes questions for better matching

### 2. TF-IDF Vectorization
- Uses scikit-learn's TfidfVectorizer
- Creates numerical representations of questions
- Supports n-gram analysis (1-2 grams)

### 3. Similarity Matching
- Calculates cosine similarity between user question and knowledge base
- Finds the best matching question
- Returns confidence score based on similarity

### 4. Response Generation
- Returns the answer for the best matched question
- Provides confidence percentage
- Shows the original matched question for transparency

## Features Overview

### 🎯 Smart Question Matching
- Advanced text preprocessing and normalization
- TF-IDF vectorization for semantic understanding
- Cosine similarity for accurate matching
- Configurable similarity threshold

### 📊 Confidence Scoring
- **High Confidence (>70%)**: Green indicator
- **Medium Confidence (40-70%)**: Orange indicator  
- **Low Confidence (<40%)**: Red indicator

### 🔄 Interactive Elements
- Real-time question processing
- Auto-complete suggestions
- Category-wise question browsing
- Random question generator

### 📱 User-Friendly Interface
- Clean, modern design
- Responsive layout
- Loading indicators
- Helpful tooltips and guidance

## Knowledge Base Categories

### 🧪 Science & Technology
- Chemistry symbols and formulas
- Physics constants and laws
- Biology facts
- Technology terminology
- Space and astronomy

### 🌍 Geography
- Country capitals
- Geographic landmarks
- Continents and oceans
- Natural wonders
- Political geography

### 📜 History
- Historical events and dates
- Famous personalities
- Ancient civilizations
- Wars and conflicts
- Cultural milestones

### ⚽ Sports
- Olympic Games
- Popular sports rules
- Records and achievements
- Team compositions
- Sporting terminology

### 🎨 Literature & Arts
- Famous authors and works
- Classical compositions
- Art history
- Cultural references
- Literary classics

## Technical Details

### Dependencies

```python
streamlit>=1.28.0    # Web application framework
pandas>=1.5.0        # Data manipulation
numpy>=1.24.0        # Numerical computing
scikit-learn>=1.3.0  # Machine learning algorithms
nltk>=3.8.0          # Natural language processing
```

### Key Technologies

- **Streamlit**: Web application framework
- **TF-IDF**: Text vectorization technique
- **Cosine Similarity**: Similarity measurement
- **NLTK**: Natural language processing
- **Pandas**: Data manipulation
- **NumPy**: Numerical operations

### Performance Optimizations

- **Caching**: Knowledge base is cached using `@st.cache_resource`
- **Vectorization**: Pre-computed TF-IDF vectors for fast similarity calculation
- **Text Preprocessing**: Optimized text cleaning and normalization

## Contributing

We welcome contributions to improve the User Q&A System! Here's how you can contribute:

### Ways to Contribute

1. **Add More Questions**: Expand the knowledge base with new Q&A pairs
2. **Improve Algorithms**: Enhance the matching algorithms
3. **UI/UX Improvements**: Make the interface more user-friendly
4. **Bug Fixes**: Report and fix bugs
5. **Documentation**: Improve documentation and examples

### Contribution Steps

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Add tests if applicable
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Create a Pull Request

### Adding New Questions

To add new questions to the knowledge base, edit the `qa_pairs` list in `knowledge_base.py`:

```python
qa_pairs = [
    # Existing questions...
    ("Your new question?", "Your detailed answer here."),
    # More questions...
]
```

## 📈 Future Enhancements

- [ ] **Database Integration**: Store questions in a database for better scalability
- [ ] **User Authentication**: Allow users to save favorite questions
- [ ] **Question History**: Track previously asked questions
- [ ] **Multiple Languages**: Support for questions in different languages
- [ ] **Admin Panel**: Interface for adding/editing questions
- [ ] **API Endpoint**: REST API for integration with other applications
- [ ] **Fuzzy Matching**: Better handling of typos and variations
- [ ] **Question Categories**: Automatic categorization of questions

## Troubleshooting

### Common Issues

1. **NLTK Data Error**:
   ```bash
   # Solution: Download NLTK data manually
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

2. **Port Already in Use**:
   ```bash
   # Solution: Use a different port
   streamlit run app.py --server.port 8502
   ```

3. **Module Not Found Error**:
   ```bash
   # Solution: Ensure virtual environment is activated and dependencies are installed
   pip install -r requirements.txt
   ```

### Getting Help

If you encounter any issues:

1. Check the [Issues](https://github.com/your-username/general-knowledge-qa-system/issues) page
2. Search for existing solutions
3. Create a new issue with detailed information
4. Include error messages and system information

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2024 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Contact

- **Developer**: Devanshi Mathan
- **Email**: devanshiimathan@gmail.com
- **GitHub**: https://github.com/devaanshii
- **LinkedIn**: https://linkedin.com/in/devanshimathan

## Acknowledgments

- Thanks to the Streamlit team for the amazing web app framework
- Scikit-learn contributors for the machine learning algorithms
- NLTK team for natural language processing tools
- The open-source community for inspiration and support

---

## Show Your Support

If you found this project helpful, please consider:

- ⭐ Starring the repository
- 🍴 Forking the project
- 📢 Sharing with others
- 🐛 Reporting issues
- 💡 Suggesting improvements

**Made with ❤️ and Python**