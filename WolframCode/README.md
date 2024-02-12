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

# Simulation
```
git clone https://github.com/bylaye/CellularAutomata && cd CellularAutomata/WolframCode
```

```
python
```
ou
```
python3
```
```
from SimpleCellular import SimpleCellular
```
```
max_line = 20
```
```
sc = SimpleCellular(rule=101, state_0=' ', state_1 = 'o', max_x=max_line, max_y=120)
```
```
>>> for _ in range(20):
...     sc.update()
... 
```
```
print(sc)
```

>output\
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo o oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                          oooo                                                          \
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo    o ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                        o oo oo                                                         \
ooooooooooooooooooooooooooooooooooooooooooooooooooooooo oo oo o oooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                      oo oo oooo                                                        \
ooooooooooooooooooooooooooooooooooooooooooooooooooooo  oo oo   o ooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                    o   oo o o oo                                                       \
ooooooooooooooooooooooooooooooooooooooooooooooooooo o o  oooooo o oooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                  ooooo       oooo                                                      \
ooooooooooooooooooooooooooooooooooooooooooooooooo     o ooooo    o ooooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                                o ooo oo    o oo oo                                                     \
ooooooooooooooooooooooooooooooooooooooooooooooo oo  oo o oo oo oo o oooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                              oo o   oooo oo oo oooo                                                    \
ooooooooooooooooooooooooooooooooooooooooooooo  ooo o    oo oo oo   o ooooooooooooooooooooooooooooooooooooooooooooooooooo\
                                            o    ooo oo  oo oo o o oo                                                   \
ooooooooooooooooooooooooooooooooooooooooooo o oo   oo o   oo oooooo o oooooooooooooooooooooooooooooooooooooooooooooooooo\
                                          oooo o o  ooo o  oo     oooo                                                  \
ooooooooooooooooooooooooooooooooooooooooo    ooooo    ooo   o ooo    o ooooooooooooooooooooooooooooooooooooooooooooooooo\

