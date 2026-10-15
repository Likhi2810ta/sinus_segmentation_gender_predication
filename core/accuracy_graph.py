import matplotlib.pyplot as plt

# Accuracy
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

# Loss
train_loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(10,4))

# Accuracy subplot
plt.subplot(1,2,1)
plt.plot(train_acc, label="Train Accuracy")
plt.plot(val_acc, label="Val Accuracy")
plt.title("Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()

# Loss subplot
plt.subplot(1,2,2)
plt.plot(train_loss, label="Train Loss")
plt.plot(val_loss, label="Val Loss")
plt.title("Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

plt.show()