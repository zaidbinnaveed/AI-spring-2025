from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

emails = pd.read_csv('emails.csv')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails['content'])
y = emails['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

new_email = ["Congratulations! You have won a prize. Click here to claim."]
new_email_transformed = vectorizer.transform(new_email)
new_email_prediction = model.predict(new_email_transformed)
