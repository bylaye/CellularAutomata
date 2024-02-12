# Automate cellulaire simple

Les automates de cette famille sont dits élémentaires. On les désigne souvent par un entier entre 0 et 255 dont la représentation binaire est la suite des états pris par l'automate sur les motifs successifs 

```
Motif initial
111  110  101  100  011  010  001  000
```

Il existe 2^8 = 256 regles numerotes de 0 a 255.
Par convention on a une regle en fonction de l'ecriture en binaire sur 8 bits du nombre decimal. A l'etat t+1 le triplet du motif initial sera l'etat de la cellule en fonction de la position du bit du nombre X (8bits).

```
Exemple

regle 0 
111  110  101  100  011  010  001  000
 0    0    0    0    0    0    0    0

regle 10
111  110  101  100  011  010  001  000
 0    0    0    0    1    0    1    0

regle 31
111  110  101  100  011  010  001  000
 0    0    0    1    1    1    1    1
```


