import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import adjusted_rand_score
from sklearn import preprocessing
import sys
b=str(sys.argv[1])
genero=str(sys.argv[2])

if(genero=="ninos"):
    data=pd.read_csv("peso_talla.csv")
    data.head()
    x=data.drop(["valoracion"],axis=1)
    y=data.valoracion
    x.head()
elif(genero=="ninas"):
    data=pd.read_csv("peso_talla_ninas.csv")
    data.head()
    x=data.drop(["valoracion"],axis=1)
    y=data.valoracion
    x.head()
else:
    print("error datos generados")

    
prueba=pd.read_csv("./uploads/libro"+b+".csv")
data_user=prueba.drop(["nombre"],axis=1)
prueba.head()


X_train,X_test,y_train,y_test=train_test_split(x,y, test_size=0.05, random_state=3 )
tree=DecisionTreeClassifier()
tree.fit(X_train,y_train)
tree_pred=tree.predict(X_test)
tree_score=adjusted_rand_score(y_test,tree_pred)
print(f"el modelo tree tiene un score de {tree_score}")
print("*"*60)
tree_pred=tree.predict(data_user)
print(tree_pred)
#print(tree_pred)


print("*"*60)
encoder=preprocessing.LabelEncoder()
encoder.fit(["0:Peso adecuado para la talla","1:Riesgo de desnutrición","2:Desnutricion Aguda Moderada",
             "3:Desnutricion aguda severa","4:Obesidad","5:Riesgo de Sobrepeso","6:Sobrepeso"
             ])
valoraciones=list(encoder.inverse_transform(tree_pred))

df=pd.DataFrame(prueba)
df["valoracion"]=valoraciones
df.head()
df.to_csv("Libro"+b+".csv")
