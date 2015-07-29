#!/usr/bin/env python

from __future__ import print_function
from rediscluster import StrictRedisCluster

"""
  NOTE: You should make sure redis-py-cluster is available in your system.
        pip install redis-py-cluster

  redis-py-cluster : https://github.com/Grokzen/redis-py-cluster/tree/1.0.0
"""


startup_nodes = [{"host": "127.0.0.1", "port": "6379"}]

# This line initialize a redis cluster client obj.
# Will raise RedisClusterException on connection failed.
# The 'decode_responses=True' is needed for Python3
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# For Redis command per call, please refer: 
#   https://redis-py.readthedocs.org/en/latest/
maxacc = rc.get('UniqueID:Account')
print('Maximum Account ID is ' + maxacc)

# Demo of pipeline (batch) usage
rcp = rc.pipeline(transaction=False)
rcp.command_stack = []

curacci = 133589
maxacci = int(maxacc)
for acc in range(curacci, maxacci+1):
  rcp.command_stack.append((['HGETALL', 'Account:-' + str(acc)], {}))

print('Pipelining ' + str(len(rcp.command_stack)) + ' Redis queries.')
# A list of dict. One dict is a HGETALL result of an account.
result = rcp.execute()

print('Query finished.')
print(result)

