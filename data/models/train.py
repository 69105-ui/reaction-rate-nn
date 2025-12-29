# ----------------------------
# src/train.py
# ----------------------------

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import json
import os

# TensorFlow/Keras imports
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# ----------------------------
# Step 1: Load Dataset
# ----------------------------
df = pd.read_csv("../data/raw/dataset.csv")

# Features and target
X = df[["A", "Ea_J_mol", "T_K"]].values
y = df["k"].values

# ----------------------------
# Step 2: Train/Test Split
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----------------------------
# Step 3: Scale Features
# ----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ----------------------------
# Step 4: Build Baseline NN
# ----------------------------
n_features = X_train_scaled.shape[1]

model = Sequential([
    Dense(64, activation='relu', input_shape=(n_features,)),
    Dense(64, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# ----------------------------
# Step 5: Callbacks
# ----------------------------
os.makedirs("../models", exist_ok=True)

checkpoint_cb = ModelCheckpoint("../models/model.h5", save_best_only=True)
earlystop_cb = EarlyStopping(patience=10, restore_best_weights=True)

# ----------------------------
# Step 6: Train Model
# ----------------------------
history = model.fit(
    X_train_scaled, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=32,
    callbacks=[checkpoint_cb, earlystop_cb],
    verbose=2
)

# Save training history
with open("../models/history.json", "w") as f:
    json.dump(history.history, f)

# ----------------------------
# Step 7: Evaluate Model
# ----------------------------
y_pred = model.predict(X_test_scaled).flatten()

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R^2: {r2:.4f}")

