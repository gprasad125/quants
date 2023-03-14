# Adding AI Models to Django

If you took part in AI Camp’s L2 curriculum, you may have learnt how to add an AI model to your Flask backend in order to process user-inputted data. The same idea can be accomplished in Django — let’s learn how! 

---

## 🥒 Saving an AI Model with `Pickle`

The `pickle` Python package is a way to serialize and deserialize Python objects. It allows Python objects to persist beyond the codebase where they were first initialized. In other words, pickle will allow us to save an AI model we create in one `.py` file and have it appear in separate `.py` file. Let’s see how to do just that: 

```python
# import packages
import pickle
import pandas as pd

# import AI model packages
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# load in data
df = pd.read_csv("path/to/data.csv")

# split into training/testing
features = df.drop(columns = ["target"])
target = df["target"]

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.25)

# train the model on training data
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# save the trained model as a Pickle-serialized object
pickle.dump(model, open("model.pkl", "wb"))
```

This bit of code creates a bytestream file called `model.pkl` that contains the serialized version of our trained Decision Tree classifier. We can open it in a entirely separate `.py` file like so:

```python
import pickle
import pandas as pd

# load pickled model file and test data 
# (or any other predictable data for this model)
pickled_model = pickle.load(("model.pkl"), "rb")
test_data = pd.read_csv("path/to/test/data.csv")

# identify x and y variables
features = test_data.drop(columns = ["target"])
target = test_data["target"]

# predict and evaluate 
predictions = pickled_model.predict(features)
accuracy = (predictions == target).mean()
```

## 🕶️ Adding Models to Views

We now know how to add AI models from one file to the other, so adding them to Django files is pretty much the same exact idea. We can see an example view function like so:

```python
def predict_view(request):
	
	# pull all user-inputted data 
	feature_1 = request.POST["feature_1"]
	feature_2 = request.POST["feature_2"]
	feature_3 = request.POST["feature_3"]
	...
	...
	
	# load into pandas dataframe
	data = {"feature_1":feature_1, ...}
	df = pd.DataFrame(data = data, index = [0])
	
	# load AI model file and predict
	pickled_model = pickle.load(("model.pkl"), "rb")
	prediction = pickled_model.predict(df)

	# return value
	return prediction 
```

This view is assuming you have some kind of form for the user to input data in the frontend. You will need to adjust how you structure the data based on what the actual user input form is like or if you are using a different AI model, etc. but this should give you an idea of how to use views and AI models! 

---

## 🤔 Reading On

There are many other ways to creatively use `pickle`-serialized objects, AI models, and Django. Furthermore, keep in mind how to use the frontend structure as well, whether you’re using Django templates or a React app. Here are some resources you may find helpful as you continue to tinker with your code:

### Resources

[📌 `pickle` Documentation](https://docs.python.org/3/library/pickle.html)

[📎 Tutorial for AI Models & Pickle w/ Django](https://www.mlq.ai/django-machine-learning/)