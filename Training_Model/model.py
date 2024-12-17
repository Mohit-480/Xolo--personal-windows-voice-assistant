from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load  training dataset from qna_logbook
def load_dataset(file_path):
    dataset = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if ':' in line:
                    q, a = line.strip().split(':', 1)
                    dataset.append({'question': q, 'answer': a})
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except Exception as e:
        print(f"Error loading dataset: {e}")
    return dataset


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)


# Training  the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(corpus)
    return vectorizer, x


def get_answer(question, vectorizer, x, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, x)
    best_match_index = similarities.argmax()
    # Check if similarity is above a threshold
    if similarities[0, best_match_index] < 0.6:
        return None
    return dataset[best_match_index]['answer']


def mind(text):
    dataset_path = r'C:\Users\mohit\OneDrive\Desktop\xolo2.0\Data\brain_data\qna_logbook.txt'
    dataset = load_dataset(dataset_path)

    if not dataset:
        return None

    vectorizer, x = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, x, dataset)

    # Return a fallback response or None if no match
    return answer if answer else None
