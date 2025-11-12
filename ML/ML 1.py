import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# Load the dataset
data = pd.read_csv(r"C:\Users\Jay Thorat\Downloads\uber\uber.csv")

# 1. Pre-process the dataset 
data["pickup_datetime"] = pd.to_datetime(data["pickup_datetime"]) 
data.dropna(inplace=True) 

# 2. Identify outliers 
Q1 = data["fare_amount"].quantile(0.25)
Q3 = data["fare_amount"].quantile(0.75)
IQR = Q3 - Q1
threshold = 1.5
lower_bound = Q1 - threshold * IQR
upper_bound = Q3 + threshold * IQR
data_no_outliers = data[(data["fare_amount"] >= lower_bound) & (data["fare_amount"] <= upper_bound)]    

# Visualize the 'fare_amount' distribution without outliers
sns.boxplot(x=data_no_outliers["fare_amount"])
plt.title("Fare Amount Distribution without Outliers")
plt.show()

# 3. Check the correlation 
# Drop non-numeric columns before calculating correlation
data_no_outliers = data_no_outliers.select_dtypes(include=[np.number])

correlation_matrix = data_no_outliers.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 4. Implement linear regression and random forest regression models 
X = data_no_outliers[['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']] 
y = data_no_outliers['fare_amount']  # Target 

# Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Create and train the linear regression model 
lr_model = LinearRegression() 
lr_model.fit(X_train, y_train) 

# Create and train the random forest regression model 
rf_model = RandomForestRegressor(n_estimators=1, warm_start=True, random_state=42)

n_trees = 15  # Limit the number of trees to 15
for i in range(1, n_trees + 1):
    rf_model.n_estimators = i  # Update number of trees
    rf_model.fit(X_train, y_train)  # Fit one more tree
    print(f"Tree {i} trained")  # Print after each tree

# 5. Evaluate the models 
# Predict the values for Random Forest
y_pred_rf = rf_model.predict(X_test) 
r2_rf = r2_score(y_test, y_pred_rf) 
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf)) 

# Output evaluation metrics
print("Random Forest Regression R2:", r2_rf) 
print("Random Forest Regression RMSE:", rmse_rf) 
