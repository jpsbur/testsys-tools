#!/usr/bin/env python3

# Parse contest.dat file
def parse(data_fn):
  res = {}
  res['problems'] = []
  res['teams'] = []
  res['submits'] = []
  for l in data_fn:
    if len(l) < 3:
      continue
    if l[0] != '@':
      continue
    if l[1:3] == 'p ':
      res['problems'].append(l[3:-1].split(','))
    elif l[1:3] == 't ':
      res['teams'].append(l[3:-1].split(','))
    elif l[1:3] == 's ':
      res['submits'].append(l[3:-1].split(','))
    else:
      continue
  return res
