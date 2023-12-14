#!/bin/bash
source .direnv/python-3.11.2/bin/activate
pip install -r requirements.txt
streamlit run LoginPage.py
