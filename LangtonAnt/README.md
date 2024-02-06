# La Fourmi de Langton
## 1. les régles d'application

Les cases d'une grille bidimensionnelle peuvent être blanches ou noires. 
On considère arbitrairement l'une de ces cases comme étant l'emplacement 
initial de la fourmi. Dans l'état initial, toutes les cases sont de la 
même couleur.

La fourmi peut se déplacer à gauche, à droite, en haut ou en bas d'une 
case à chaque fois selon les règles suivantes :

* Si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, 
change la couleur de la case en blanche et avance d'une case.
  
* Si la fourmi est sur une case blanche, elle tourne de 90° vers la droite, 
change la couleur de la case en noire et avance d'une case.
