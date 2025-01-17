# Wild Code School - Correction Assistant

AI assistant for correction on  Wild Code School's Odyssey platform.


## Description

As part of my training at Wild Code School, I regularly have to correct my colleagues' exercises. This allows me to see other codes, other ways of solving the same problem. But it's also a time-consuming task. In theory, for every exercise I hand in, I have to correct 3.

**That's why I've tried to code a correction bot 🤖**.

Language: Python 🐍

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
