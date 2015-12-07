#!/usr/bin/env python3

import os
import argparse
import pygal

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
      res['problems'].append(l[3:-1].split(','))
    elif l[1:3] == 't ':
      res['teams'].append(l[3:-1].split(','))
    elif l[1:3] == 's ':
      res['submits'].append(l[3:-1].split(','))
    else:
      continue
  return res

def gen_problem_submit_stats(contest_data):
  problem_submits = {}
  for p in contest_data['problems']:
    pid = p[0]
    problem_submits[pid] = []
  for s in contest_data['submits']:
    pid = s[1]
    problem_submits[pid].append(s)
  slice_size = 15 * 60
  total_time = 5 * 60 * 60
  slices = total_time // slice_size
  for p in problem_submits:
    cnt_ac = [0] * slices
    cnt_rj = [0] * slices
    for s in problem_submits[p]:
      t = int(s[3]) // slice_size
      if s[4] == 'OK':
        cnt_ac[t] += 1
      else:
        cnt_rj[t] += 1

    line_chart = pygal.Bar()
    line_chart.title = 'Problem ' + p + ' submission stats'
    line_chart.x_labels = [str(i * slice_size) for i in range(slices)]
    line_chart.add('AC', cnt_ac)
    line_chart.add('RJ', cnt_rj)
    f = open(p + '.stats.svg', 'wb')
    f.write(line_chart.render())
    f.close()

contest_data = contest_parse(open(args.data_fn))
gen_problem_submit_stats(contest_data)
