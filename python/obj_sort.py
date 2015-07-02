#!/usr/bin/env python

# Required for Python2.6/2.7 to handle Python3 print syntax
from __future__ import print_function

class MyScoreReccord:
  def __init__(self, accid, score):
    self.accid = accid
    self.score = score
    self.atkwin = 0
    self.defwin = 0

  def __cmp__(self, other):
    if self.score > other.score:
      return 1
    elif self.score < other.score:
      return -1
    elif self.atkwin > other.atkwin:
      return 1
    elif self.atkwin < other.atkwin:
      return -1
    elif self.defwin > other.defwin:
      return 1
    elif self.defwin < other.defwin:
      return -1
    elif self.accid > other.accid:
      return 1
    elif self.accid < other.accid:
      return -1
    return 0

def score_objs(input_score_file):
  try:
    with open(input_score_file, 'rb') as rf:
      it = iter(rf)
      try:
        objs = {}
        while True:
          line = it.next()
          line = line.strip('\n')
          accid = int(line)
          line = it.next()
          line = line.strip('\n')
          score = int(line)
          r = MyScoreReccord(accid, score)
          objs[accid] = r
      except StopIteration:
        pass
      return objs
  except IOError as err:
    print ('score_objs(): Failed on opening ' + input_score_file + ' for reading. Error: ' + str(err))
  return {}

def bind_atk(objs, input_atk_file):
  try:
    with open(input_atk_file, 'rb') as rf:
      it = iter(rf)
      try:
        while True:
          line = it.next()
          line = line.strip('\n')
          accid = int(line)
          line = it.next()
          line = line.strip('\n')
          atkwin = int(line)
          objs[accid].atkwin = atkwin
      except StopIteration:
        pass
  except IOError as err:
    print ('bind_atk(): Failed on opening ' + input_atk_file + ' for reading. Error: ' + str(err))

def bind_def(objs, input_def_file):
  try:
    with open(input_def_file, 'rb') as rf:
      it = iter(rf)
      try:
        while True:
          line = it.next()
          line = line.strip('\n')
          accid = int(line)
          line = it.next()
          line = line.strip('\n')
          defwin = int(line)
          objs[accid].defwin = defwin
      except StopIteration:
        pass
  except IOError as err:
    print ('bind_def(): Failed on opening ' + input_def_file + ' for reading. Error: ' + str(err))

def obj_sort(input_score_file, input_atk_file, input_def_file, output_file):
  objs = score_objs(input_score_file)
  bind_atk(objs, input_atk_file)
  bind_def(objs, input_def_file)
  vals = objs.values()
  sorted_vals = sorted(vals, reverse=True)
  with open(output_file, 'wb') as wf:
    for v in sorted_vals:
      print(str(v.accid) + ',' + str(v.score) + ',' + str(v.atkwin) + ',' + str(v.defwin), file=wf)
    

obj_sort("input/pvp_score.txt", "input/pvp_atk.txt", "input/pvp_def.txt", "out.txt")

