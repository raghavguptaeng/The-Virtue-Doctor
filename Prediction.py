
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
def check_for_disease(dis):
    disease = []
    disease.append(dis)
    print(disease)
    data = pd.read_csv(r'D:\Projets\websites\virtue_Docrtor_Final\static\Dataset.csv')
    x = data[['FEVER', 'COUGH', 'DIARRHEA',
              'HEADACHE', 'CHEST PRESSURE',
              'NASAL CONGESTION', 'SWEATING',
              'MUSCLE ACHE', 'NAUSEA', 'ABDOMINAL PAIN',
              'ITCHY EYES/BLURRED VISION','VOMITING','HEARTBURN','WHEEZING','THROAT IRRITATION'
              ,'TIREDNESS']].values
    y = data[['NAME']]
    X = preprocessing.StandardScaler().fit(x).transform(x.astype(float))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)
    k = 1
    neigh = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train.values.ravel())
    ans = neigh.predict(disease)
    print(ans[0])
#-17
arr=['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '2', '2', '0']
check_for_disease(arr)