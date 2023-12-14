#!/bin/bash
if [ ! -e /usr/bin/pipenv ]; then
  sudo apt-get install pipenv -y
fi
pipenv run streamlit run LoginPage.py
