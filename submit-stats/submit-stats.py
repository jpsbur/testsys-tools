#!/usr/bin/env python3

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "data_fn",
    help="contest data file in Testsys format",
)
args = parser.parse_args()

# Parse contest.dat file
def contest_parse(data_fn):
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
      res['problems'].append(l)
    elif l[1:3] == 't ':
      res['teams'].append(l)
    elif l[1:3] == 's ':
      res['submits'].append(l)
    else:
      continue
  return res

contest_data = contest_parse(open(args.data_fn))

print(str(contest_data))
for p in contest_data['problems']:
  pass
