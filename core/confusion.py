import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, classification_report

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("balanced_dataset.csv")

X = df["total_volume"]
y_true = df["gender"]

# =========================
# THRESHOLD MODEL
# =========================
THRESHOLD = 14500

def predict(volume):
    if volume < THRESHOLD:
        return 0   # Female
    else:
        return 1   # Male

y_pred = X.apply(predict)

# =========================
# CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_true, y_pred)

disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=["Female (0)", "Male (1)"])

disp.plot(cmap="Blues")
plt.title("Confusion Matrix - Threshold Model")
plt.show()

# =========================
# ACCURACY
# =========================
accuracy = accuracy_score(y_true, y_pred)
print("\nAccuracy:", round(accuracy * 100, 2), "%")

# =========================
# CLASSIFICATION REPORT
# =========================
print("\nClassification Report:\n")
print(classification_report(y_true, y_pred))