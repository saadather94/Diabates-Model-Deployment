import pandas as pd
import numpy as np
import sklearn 

def get_pred(preg,plgluco,distolicBP,Trithk,insuline,bmi,diapedgr,age):

    values = np.array([[preg,plgluco,distolicBP,Trithk,insuline,bmi,diapedgr,age]], dtype=float)

    df = pd.read_csv("diab.csv")

    feat = df.iloc[:,:-1]
    lab = df.iloc[:,-1:]

    from sklearn.preprocessing import MinMaxScaler

    scaler = MinMaxScaler()
    scaled = scaler.fit(feat)
    feats = scaled.transform(feat)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test=train_test_split(feats,lab,test_size=0.2,train_size=0.8
                                                    ,shuffle=True,stratify=lab,random_state=1)

    from sklearn.neural_network import MLPClassifier

    model = MLPClassifier(random_state=1,max_iter=100)
    model.fit(X_train,y_train)

    return int(model.predict(values))



