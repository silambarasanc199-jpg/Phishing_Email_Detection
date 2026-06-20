import pickle

model = pickle.load(open("model.pkl","rb"))

email = input("Enter email: ")

result = model.predict([email])

if result[0] == 1:
    print("Phishing Email")
else:
    print("Safe Email")