import streamlit as st
import time
from knowledge_base import KnowledgeBase

# Page configuration
st.set_page_config(
    page_title="General Knowledge Q&A System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}

.question-box {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #1f77b4;
    color: #1f77b4;
}

.answer-box {
    background-color: #e8f4fd;
    padding: 1rem;
    border-radius: 10px;
    border-left: 5px solid #2ecc71;
    color: #2ecc71;
}

.confidence-high {
    color: #2ecc71;
    font-weight: bold;
}

.confidence-medium {
    color: #f39c12;
    font-weight: bold;
}

.confidence-low {
    color: #e74c3c;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    background-color: #1f77b4;
    color: white;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_knowledge_base():
    """Load knowledge base (cached for performance)"""
    return KnowledgeBase()

def main():
    # Load knowledge base
    kb = load_knowledge_base()
    
    # Header
    st.markdown('<h1 class="main-header">🧠 General Knowledge Q&A System</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📚 About")
        st.write("This AI-powered Q&A system can answer general knowledge questions about:")
        st.write("• Science & Technology")
        st.write("• Geography")
        st.write("• History")
        st.write("• Sports")
        st.write("• Literature & Arts")
        
        st.header("💡 How it works")
        st.write("1. Type your question in the input box")
        st.write("2. Click 'Get Answer' or press Enter")
        st.write("3. The AI finds the best matching answer")
        st.write("4. Confidence score shows match quality")
        
        st.header("📊 Statistics")
        st.metric("Questions in Database", len(kb.qa_data))
        st.metric("Categories", 6)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Ask Your Question")
        
        # Question input
        user_question = st.text_input(
            "Enter your question:",
            placeholder="e.g., What is the capital of France?",
            help="Ask any general knowledge question!"
        )
        
        # Submit button
        if st.button("🔍 Get Answer", type="primary"):
            if user_question.strip():
                with st.spinner("🤖 Finding the best answer..."):
                    time.sleep(1)  # Add slight delay for better UX
                    result = kb.find_best_answer(user_question)
                
                # Display question
                st.markdown(f'<div class="question-box"><strong>❓ Your Question:</strong><br>{user_question}</div>', unsafe_allow_html=True)
                st.write("")
                
                # Display answer
                st.markdown(f'<div class="answer-box"><strong>💡 Answer:</strong><br>{result["answer"]}</div>', unsafe_allow_html=True)
                
                # Display confidence and matched question
                if result['confidence'] > 0:
                    confidence_class = "confidence-high" if result['confidence'] > 70 else "confidence-medium" if result['confidence'] > 40 else "confidence-low"
                    st.markdown(f'<p class="{confidence_class}">🎯 Confidence: {result["confidence"]}%</p>', unsafe_allow_html=True)
                    
                    if result['matched_question']:
                        with st.expander("🔍 See matched question"):
                            st.write(f"**Matched question:** {result['matched_question']}")
                
            else:
                st.warning("⚠️ Please enter a question!")
        
        # Auto-answer on Enter key (using form)
        with st.form(key='question_form', clear_on_submit=True):
            question_form = st.text_input(
                "Or press Enter after typing:",
                placeholder="Quick question input...",
                label_visibility="visible"
            )
            
            if st.form_submit_button("Submit"):
                if question_form.strip():
                    with st.spinner("🤖 Finding the best answer..."):
                        result = kb.find_best_answer(question_form)
                    
                    st.markdown(f'<div class="question-box"><strong>❓ Your Question:</strong><br>{question_form}</div>', unsafe_allow_html=True)
                    st.write("")
                    st.markdown(f'<div class="answer-box"><strong>💡 Answer:</strong><br>{result["answer"]}</div>', unsafe_allow_html=True)
                    
                    if result['confidence'] > 0:
                        confidence_class = "confidence-high" if result['confidence'] > 70 else "confidence-medium" if result['confidence'] > 40 else "confidence-low"
                        st.markdown(f'<p class="{confidence_class}">🎯 Confidence: {result["confidence"]}%</p>', unsafe_allow_html=True)
    
    with col2:
        st.header("💭 Need Ideas?")
        
        # Random questions
        if st.button("🎲 Get Random Questions"):
            random_questions = kb.get_random_questions(5)
            st.write("**Try asking these questions:**")
            for i, q in enumerate(random_questions, 1):
                st.write(f"{i}. {q}")
        
        st.write("---")
        
        # Categories
        st.subheader("📋 Example Questions by Category")
        categories = kb.get_all_categories()
        
        for category, questions in categories.items():
            with st.expander(f"🔸 {category}"):
                for q in questions:
                    if st.button(q, key=f"cat_{category}_{q[:20]}"):
                        # Auto-fill the question
                        st.session_state.auto_question = q
                        st.experimental_rerun()
    
    # Handle auto-filled questions
    if 'auto_question' in st.session_state:
        st.info(f"Selected question: {st.session_state.auto_question}")
        with st.spinner("🤖 Finding the answer..."):
            result = kb.find_best_answer(st.session_state.auto_question)
        
        st.markdown(f'<div class="answer-box"><strong>💡 Answer:</strong><br>{result["answer"]}</div>', unsafe_allow_html=True)
        
        if result['confidence'] > 0:
            confidence_class = "confidence-high" if result['confidence'] > 70 else "confidence-medium" if result['confidence'] > 40 else "confidence-low"
            st.markdown(f'<p class="{confidence_class}">🎯 Confidence: {result["confidence"]}%</p>', unsafe_allow_html=True)
        
        # Clear the auto question
        del st.session_state.auto_question
    
    # Footer
    st.write("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🚀 Built with Python, Streamlit, and AI • Perfect for learning and testing general knowledge!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
