# Wild Code School - Correction Assistant
*Français ci-dessous*

AI assistant for correction on  Wild Code School's Odyssey platform.

## Table of Content
[Description](#description)

[Objective](#objective)

[Features](#features)

[Technical limitations](#technical-limitations)

[Warning](#warning)

[Version française](#wild-code-school---assistant-de-correction)


## Description

As part of my training at Wild Code School, I regularly have to correct my colleagues' exercises. This allows me to see other codes, other ways of solving the same problem. But it's also a time-consuming task. In theory, for every exercise I hand in, I have to correct 3.

**That's why I've tried to code a correction bot 🤖**.

## Objective

Create an AI agent that :
1. navigates a web browser to the Odyssey platform login page
2. logs in using my login and password
3. goes to the exercise correction page
4. filters the exercises to be corrected according to parameters defined in arguments
5. scrapes the exercise page to retrieve the instructions and the student's name
6. goes to the answer notebook and scrapes the code
7. analyzes the student's code and checks that the instructions have been respected
8. generates a comment to congratulate the student or suggest an improvement if the code doesn't meet the instruction
9. writes this comment in the dedicated box and sends the correction

Language: Python 🐍 (Object Oriented Programming)

Libraries: 
- web browsing: Helium / Selenium 🌐
- web scraping: Beautiful Soup 🥣
- response analysis and comment generation: Gemini API 🤖 

## Features

- start_engine(): connect to  Wild Code School's Odyssey platform with your id and password
- correct_exercise(): correct first exercice on list based your filter
- correct_all_exercices(): correct all exercices on list based your filter

## Technical limitations

Currently, this assistant can only correct exercises published on Google Colabs notebooks (the vast majority of exercises on the platform).
Exercises whose answers are in a format other than code (screenshots, Power BI .pbix files, etc.) cannot be corrected in this way.

## Warning

Be careful! 
This project is for educational purposes, to put into practice skills acquired with helium and web scraping.
It is not intended to spam the platform.
Correcting other students' exercises yourself and helping them improve their code remains an excellent way to learn.

------

# Wild Code School - Assistant de correction


Assistant de correction sur la plateforme Odyssey de Wild Code School.

## Table des matières

[Description](#description)

[Objectif](#objectif)

[Features](#features)

[Limitations techniques](#limitations-techniques)

[Avertissement](#avertissement)


## Description

Dans le cadre de ma formation à la Wild Code School, je suis régulièrement amené à corriger les exercices de mes collègues. Cela me permet de voir d'autres codes, d'autres façons de résoudre un même problème. Mais c'est aussi une tâche qui prend beaucoup de temps. En théorie, pour chaque exercice que je rends, je dois en corriger 3.

**C'est pourquoi j'ai essayé de coder un bot de correction 🤖**.

## Objectif

Créer un agent d'intelligence artificielle qui :
1. navigue dans un navigateur web jusqu'à la page de connexion de la plateforme Odyssey
2. se connecte en utilisant mon login et mon mot de passe
3. va sur la page de correction des exercices
4. filtre les exercices à corriger selon les paramètres définis en arguments
5. scrape la page de l'exercice pour récupérer les instructions et le nom de l'élève
6. va sur le notebook de réponse et récupère le code
7. analyse le code de l'étudiant et vérifie que les consignes ont été respectées
8. génère un commentaire pour féliciter l'élève ou suggérer une amélioration si le code ne répond pas à la consigne
9. écrit ce commentaire dans la case dédiée et envoie la correction

Langage : Python 🐍 (Programmation Orientée Objet)

Librairies : 
- navigation web : Helium / Selenium 🌐
- web scraping : Beautiful Soup 🥣
- analyse des réponses et génération de commentaires : Gemini API 🤖 

## Features

- start_engine() : se connecter à la plateforme Odyssey de Wild Code School avec votre identifiant et votre mot de passe
- correct_exercise() : corrige le premier exercice de la liste en fonction de votre filtre
- correct_all_exercices() : corrige tous les exercices de la liste en fonction de votre filtre

## Limitations techniques

Actuellement, cet assistant ne peut corriger que les exercices publiés sur les cahiers Google Colabs (la grande majorité des exercices sur la plateforme).
Les exercices dont les réponses sont dans un format autre que du code (captures d'écran, fichiers Power BI .pbix, etc.) ne peuvent pas être corrigés de cette manière.

## Avertissement

Attention ! Ce projet est à but pédagogique, pour mettre en pratique les compétences acquises avec helium et le web scraping. Il n'est pas destiné à spammer la plateforme.
Corriger soi-même les exercices des autres étudiants et les aider à améliorer leur code reste un excellent moyen d'apprendre.


