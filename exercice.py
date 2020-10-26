#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
from os.path import getsize


# TODO: Définissez vos fonction ici
def compare_files(fname1, fname2):
    #if getsize(fname1) != getsize(fname2):
        #print('Les fichiers ont des tailles différentes...')
    f.seek(0, 2) #dernier caractère
    p.seek(0, 2)
    print(f.tell(), p.tell()) #la position du dernier caractère est égale à la taille du fichier
    f.seek(0)
    p.seek(0)
    
    with open(fname1, "r") as f, open(fname2, "r") as p:
    c = f.read(1)
    k = p.read(1)
    while c != '' and k != '':
        if c != k:
            position = f.tell()
            print(f"la diffrerence est à la position {position} entre {c} et {k}")
            print(f"la difference est {c} entre {k}")
            break
        c = f.read(1)
        k = p.read(1)
   

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_files(fname1='exemple.txt', fname2='exemple2.txt')

    
