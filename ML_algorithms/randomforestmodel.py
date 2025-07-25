import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV

# Load and prepare dataset
df = pd.read_csv('/Users/aishwaryarkoujalgi/Docs/Coding Exercises/healthcareanalytics101/ML_algorithms/Fitabase Data 4.12.16-5.12.16/dailyActivity_merged.csv')

# Drop missing values
df = df.dropna(subset=['TotalSteps', 'Calories'])

# Define features (X) and target (y)
X = df[['TotalSteps']]
y = df ['Calories']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

## A. Mean Baseline (for all test samples)
baseline_pred = [y_train.mean()] * len(y_test)

baseline_mse = mean_squared_error(y_test, baseline_pred)
baseline_rmse = np.sqrt(baseline_mse)
baseline_mae = mean_absolute_error(y_test, baseline_pred)

## B. Simple Linear Regression model
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

y_lin_pred = lin_model.predict(X_test) # Predict on test data

lin_mse = mean_squared_error(y_test, y_lin_pred) # Evaluation
lin_rmse = np.sqrt(lin_mse)
lin_mae = mean_absolute_error(y_test, y_lin_pred)
lin_r2 = r2_score(y_test, y_lin_pred)

### C. Random Forest Regression model

# Using GridSearchCV to tune systematically and automatically search the optimal hyperparameters.
param_grid = {
    'n_estimators': [100, 200, 300, 400, 500],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2']
}

model = RandomForestRegressor(random_state=0)

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,  # 5-fold cross-validation
    n_jobs=-1,  # use all cores
    scoring='neg_mean_squared_error',
    verbose=2
)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"""Mean Squared Error: {mse:.2f}
Optimal Hyperparameters: {grid_search.best_params_}""")

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print all metrics
print(f"""Baseline Performance (Mean Predictor):
  Mean Squared Error (MSE): {baseline_mse:.2f}
  Root Mean Squared Error (RMSE): {baseline_rmse:.2f}
  Mean Absolute Error (MAE): {baseline_mae:.2f}

Simple Linear Regression:
  Mean Squared Error (MSE): {lin_mse:.2f}
  Root Mean Squared Error (RMSE): {lin_rmse:.2f}
  Mean Absolute Error (MAE): {lin_mae:.2f}
  R^2 Score: {lin_r2:.3f}

Random Forest Model Performance:
  Mean Squared Error (MSE): {mse:.2f}
  Root Mean Squared Error (RMSE): {rmse:.2f}
  Mean Absolute Error (MAE): {mae:.2f}
  R^2 Score: {r2:.2f}
""")

# Visualization
metrics = ['MSE', 'RMSE', 'MAE']
baseline_scores = [baseline_mse, baseline_rmse, baseline_mae]
linear_regression_model_scores = [lin_mse, lin_rmse, lin_mae]
random_forest_model_scores = [mse, rmse, mae]

#print("Model scores:", model_scores)
#print("Baseline scores:", baseline_scores)

# Bar graph comparing errors: Baseline vs Linear Regression vs Random Forest Model
for i, metric in enumerate(metrics):
    plt.figure(figsize=(5,4))
    plt.bar(['Baseline', 'Simple Linear Regression', 'Random Forest'], 
            [baseline_scores[i], linear_regression_model_scores[i], random_forest_model_scores[i]], 
            color=['red', 'green', 'blue'])
    plt.title(f'{metric} Comparison')
    plt.ylabel(metric)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Scatter plot of Linear Regression vs Random Forest
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, alpha=0.6, label='Random Forest', color='dodgerblue', edgecolor='k') #(Random Forest)
plt.scatter(y_test, y_lin_pred, alpha=0.6, label='Linear Regression', color='orange', edgecolor='k') #(Linear Regression)

min_val = min(y_test.min(), y_pred.min(), y_lin_pred.min()) # Identity line (perfect prediction)
max_val = max(y_test.max(), y_pred.max(), y_lin_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', label='Perfect Prediction')

plt.xlabel('Actual Calories')
plt.ylabel('Predicted Calories')
plt.title('Actual vs Predicted (Random Forest vs Linear Regression)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Residual plot
residuals = y_test - y_pred
plt.figure(figsize=(8,5))
plt.scatter(y_pred, residuals, alpha=0.6, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Calories')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residual Plot')
plt.grid(True)
plt.tight_layout()
plt.show()