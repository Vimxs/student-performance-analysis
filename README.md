# student-performance-analysis
A Python &amp; Streamlit project analyzing student performance data.
#Student Performance Analysis

This project analyzes how different factors influence student academic performance using **Python, Pandas, Matplotlib/Seaborn, Scikit-learn, and Streamlit**.  
It includes data cleaning, exploratory analysis, a trained ML model, and an optional Streamlit app.

---

#Project Structure
student-performance-analysis/
│
├── app.py
├── data_check.py
│
├── data/
│ └── StudentsPerformance.csv
│
├── models/
│ ├── model_columns.pkl
│ └── student_performance_model.pkl
│
├── notebooks/
│ ├── 1data_preparation.ipynb
│ ├── 2model_training.ipynb
│
└── README.md


---

## Project Highlights
- Cleaned and preprocessed real-world student performance data  
- Performed detailed **Exploratory Data Analysis (EDA)**  
- Visualized trends across gender, parental education, test preparation, and lunch type  
- Trained a predictive ML model  
- Optional **Streamlit dashboard** interface  
- Organized using a clean, professional folder structure  

---

## Key Insights Explored
- Impact of **test preparation courses**  
- Score differences by **gender**  
- Influence of **parental education**  
- Effect of **lunch type** on performance  
- Correlation patterns across all subjects  

---

## Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- Scikit-learn  
- Streamlit  

---

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt

Run Streamlit app
streamlit run app.py

📁 Dataset

Dataset: Students Performance in Exams
Source: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

🛠 Future Improvements

Deploy the Streamlit app

Add more interactive visualizations

Add feature importance & SHAP explanations

Train a stronger predictive model

👩‍💻 Author

Vimla Pandey (Vimxs)
Feel free to connect or collaborate on LinkedIn.
