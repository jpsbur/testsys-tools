#!/usr/bin/env python3

import pygal

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
    cnt_fz = [0] * slices
    for s in problem_submits[p]:
      t = int(s[3]) // slice_size
      if s[4] == 'OK':
        cnt_ac[t] += 1
      elif s[4] == 'FZ':
        cnt_fz[t] += 1
      else:
        cnt_rj[t] += 1

    line_chart = pygal.Bar()
    line_chart.title = 'Problem ' + p + ' submission stats'
    line_chart.x_labels = [str(i * slice_size) for i in range(slices)]
    line_chart.add('AC', cnt_ac)
    line_chart.add('RJ', cnt_rj)
    line_chart.add('FZ', cnt_fz)
    f = open(p + '.stats.svg', 'wb')
    f.write(line_chart.render())
    f.close()

