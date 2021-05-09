#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:24:07 2021

@author: pauloeduardosampaio
"""

from whatsapp_api import WhatsApp
import pandas as pd
from datetime import datetime

agenda = pd.read_csv("agenda.csv")
agenda["Timestamp"] = None
wp = WhatsApp()

input("Enter quando ler o QR code")

for contato in agenda["Nome"].values:
    mensagem = agenda.loc[agenda["Nome"]==contato, "Mensagem"].values
    agenda.loc[agenda["Nome"]==contato, "Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(contato, mensagem)
    wp.search_contact(contato)
    wp.write_message(mensagem)

agenda.to_csv("mensagens_enviadas.csv", index=False)