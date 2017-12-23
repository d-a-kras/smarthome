#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
with open("html/1.html", "r") as file:
    text = file.read()
   

print("Content-type: text/html")
print()
print( text )