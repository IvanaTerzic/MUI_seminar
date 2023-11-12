# QSAR_Kristina_topljivost
QSAR - zadatci koje je Kristina zadala

1. proci Marijev tutorial - Kemija u Industriji
2. izracunati rdkit 2d deskriptore, istrenirati XGBoost regression model
3. izracunati fingerprints, izbaciti kojima je varijanca 0, ubaciti u model, usporediti rezultate s prijasnjima
4. izbaciti feature koji koreliraju vise od 99%, drugi scenarij izbaciti gdje je vise od 95% --> usporediti rezultate, uzeti bolji scenarij
5. mijenjati parametre modela s GridSearch kako bi se optimizirao, ne zaboraviti kod train_test_split definirati random_state
6. umjesto random train/test splita se poigrati da su u test setu zastupljene vrijednosti topljivosti iz cijelog rangea molekula, ali 
prvo imati kontrolu tj histogram topljivosti --> zelimo da nam je model dobar u cijelom rangeu topljivosti za koje imamo podatke
 
