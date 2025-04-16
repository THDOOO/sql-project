import seaborn as sns

# Titanic-Daten laden
titanic = sns.load_dataset('titanic')


# Zeige fehlende Werte
print(titanic.isnull().sum())

# Beispielsweise: Fehlende Werte für 'age' mit dem Median füllen
titanic['age'].fillna(titanic['age'].median(), inplace=True)

# Fehlende Werte in 'embarked' mit dem häufigsten Wert füllen
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# Überprüfen, ob noch fehlende Werte vorhanden sind
print(titanic.isnull().sum())


