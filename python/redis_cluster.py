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
data = rc.hgetall('#Data:RedeemCode:22:Prize')
print(data)


