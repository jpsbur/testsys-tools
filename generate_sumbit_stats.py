#!/usr/bin/env python3

import os
import argparse

from common import contest_data_parser
from submit_stats import submit_stats

parser = argparse.ArgumentParser()
parser.add_argument(
  "data_fn",
  help="contest data file in Testsys format",
)
args = parser.parse_args()

contest_data = contest_data_parser.parse(open(args.data_fn))
submit_stats.gen_problem_submit_stats(contest_data)

