🏏 CricketRAG: IPL Q&A App Using RAG + FAISS
CricketRAG is a Generative AI-powered question-answering system for IPL cricket data (2008–2023), built using a Retrieval-Augmented Generation (RAG) pipeline.

It enables users to ask natural language questions like:

"Who won CSK vs MI in Wankhede in 2019?"

"Who was POTM for RCB vs KKR in 2023 at Chinnaswamy?"

🚀 Features
✅ RAG-based architecture using FAISS for semantic retrieval

✅ Fast embeddings using SentenceTransformers (MiniLM)

✅ Query understanding with team abbreviations (CSK, MI, RCB…)

✅ Filters by city, venue, and season

✅ Clean and responsive Streamlit UI

✅ Uses real Kaggle IPL data from 2008 to 2023

📁 Project Structure
bash
Copy
Edit
cricket_rag/
├── backend/
│   ├── app.py               # Streamlit UI app
│   ├── retriever.py         # FAISS index creation
│   ├── rag_pipeline.py      # Embedding + Retrieval logic
│   ├── utils.py             # Abbreviation & normalization
│
├── data/
│   ├── match_info_data.csv  # IPL dataset (from Kaggle)
│
├── faiss_store/
│   ├── cricket.index        # FAISS index
│   ├── texts.txt            # Indexed match descriptions
│
├── venv/                    # Python virtual environment
├── requirements.txt
├── .gitignore
└── README.md
📦 Installation
1️⃣ Clone Repo & Create Virtual Environment
Open CMD and run:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/cricket_rag.git
cd cricket_rag
python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
nginx
Copy
Edit
pip install -r requirements.txt
📂 Download Dataset
Download from Kaggle: https://www.kaggle.com/datasets/utkarshtomar736/ipl-mens-cricket-matches-data-2008-2023

Place match_info_data.csv inside the data/ folder.

⚙️ Build FAISS Index
Run the following to process the data and create the FAISS index:

bash
Copy
Edit
cd backend
python retriever.py
🚀 Launch the Streamlit App
arduino
Copy
Edit
streamlit run app.py
Now open the app in your browser: http://localhost:8501

💬 Example Queries You Can Ask
Who won the match between CSK and GT in 2023?

RCB vs MI winner in 2020 at Dubai

Who was Player of the Match in CSK vs KKR at Chennai in 2021?

MI KKR 2019 Eden Gardens result

Who won LSG vs DC 2022?

🛠️ Tech Stack
Python 3.10+

Streamlit

Pandas

FAISS

Sentence Transformers (MiniLM)

Regex/NLP (for query normalization)

🧠 How It Works (RAG Flow)
Data Preprocessing: Extract match details from IPL CSV

Embedding: Convert match text into dense vectors using all-MiniLM-L6-v2

Indexing: Store embeddings using FAISS

Query: User types a natural language question

Retriever: FAISS finds the closest matches

Answer Formatter: Formats the top result with a clean layout in UI

📌 Future Improvements
Support full generative answers using LLMs (e.g., LLaMA or Mistral)

Add scorecard and team stats view

Integrate international cricket dataset

Chat memory (conversation context)

🧑‍💻 Author
Ajay M S
Email: msajay2866@gmail.com
GitHub: AJAY-M-S

