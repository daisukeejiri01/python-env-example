from sklearn.datasets import load_iris
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split

def train_and_evaluate_classifier():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
    tpot.fit(X_train, y_train)
    
    print(f"Accuracy score: {tpot.score(X_test, y_test)}")

    return tpot

if __name__ == "__main__":
    tpot = train_and_evaluate_classifier()
