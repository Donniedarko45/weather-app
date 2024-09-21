# app/models/hyperparameter_optimization.py

from sklearn.model_selection import GridSearchCV

# Example using scikit-learn for hyperparameter tuning (for simpler models)
def optimize_hyperparameters(model, param_grid, X_train, y_train):
    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid.best_params_, grid.best_score_
