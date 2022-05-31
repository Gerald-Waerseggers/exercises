
import json
from datetime import datetime
from statistics import mean


with open('input.txt') as f:
    data = [ (datetime.strptime(date, '%d/%m/%Y'), temps) for date, temps in json.load(f).items()]

with open('output.txt', 'w') as out:
    for _, temps in sorted(data, key=lambda p: p[0]):
        out.write(f'{(round(mean(temps)))}\n')

