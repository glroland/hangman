#! /bin/bash

PROJECT_ENV=hangman

conda remove -y -n $PROJECT_ENV --all
conda env create -f environment.yml

source ~/anaconda3/bin/activate $PROJECT_ENV
conda activate $PROJECT_ENV
