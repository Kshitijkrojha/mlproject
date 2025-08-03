## end to end machine learning project
🎓 Student Performance Prediction
This project aims to predict student performance in a subject using a variety of machine learning algorithms. After comparing multiple models, the best-performing one (with 88.98% accuracy) was selected and deployed via a user-friendly HTML/CSS web interface.

📌 Project Objective
To create a predictive system that can estimate student performance based on various academic and personal parameters using Machine Learning, and deploy it with an intuitive frontend.

📊 Features Used
Hours of study

Attendance

Previous grades

Participation in class

Sleep hours

Family support

Internet access

Extra-curricular activities

🔧 ML Algorithms Used
The following models were trained and evaluated:

Linear Regression

Logistic Regression

Decision Tree

Random Forest

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Naive Bayes

Gradient Boosting

XGBoost

Neural Network (MLPClassifier)

✅ Best Model: Random Forest Classifier (Accuracy: 88.98%)

📈 Model Evaluation Metrics
Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Cross-validation

🚀 Deployment
The best model was saved using joblib and deployed via a Flask backend with an HTML/CSS frontend.

🖥️ Web App Features
Simple, responsive UI built with HTML and CSS

User inputs: student-related metrics

Instant prediction on form submission

Display of the performance category (e.g., "Excellent", "Average", "Needs Improvement")

📁 Project Structure
cpp
Copy
Edit
├── model/
│   └── student_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── app.py
├── requirements.txt
└── README.md
▶️ How to Run Locally
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/student-performance-ml
cd student-performance-ml
Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Run the app

nginx
Copy
Edit
python app.py
Open in browser
Visit http://127.0.0.1:5000/

📚 Future Improvements
Add visualization dashboard for insights

Allow batch uploads (CSV) for predictions

Deploy on cloud (Heroku, Render, AWS, etc.)

Include more features (e.g., mental health, peer influence)

🧠 Tech Stack
Python (Pandas, Scikit-learn, Joblib, Flask)

HTML5, CSS3

ML Algorithms

Jupyter Notebooks for model evaluation

📌 Accuracy Snapshot
✅ Final Accuracy of Deployed Model: 88.98%

