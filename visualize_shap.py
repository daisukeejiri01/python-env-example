
import shap
from sklearn.datasets import load_iris
from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split

def visualize_shap_values():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, random_state=42)
    tpot.fit(X_train, y_train)
    
    # Use the best pipeline to compute SHAP values
    best_pipeline = tpot.fitted_pipeline_
    explainer = shap.Explainer(best_pipeline.predict, X_train)
    shap_values = explainer(X_train)
    
    # Visualize the SHAP values
    shap.summary_plot(shap_values, X_train)

if __name__ == "__main__":
    visualize_shap_values()