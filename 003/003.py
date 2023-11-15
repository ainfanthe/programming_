#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# 002: Calculate Age

from datetime import datetime, timedelta

def calculate(age):
    today = datetime.today()
    birthdate = today - timedelta(days = 365 * age + 5)
    return birthdate

def calculateSeconds(age):
    ageSeconds = age * 365 * 24 * 3600
    return ageSeconds
    
age = int(input('age: '))
birth_date = calculate(age)
seconds = calculateSeconds(age)
print(birth_date.strftime('%d/%m/%Y'))
print(seconds)