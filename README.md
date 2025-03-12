# LRU_Cache
Overview

This repository contains an efficient implementation of an LRU (Least Recently Used) Cache using a doubly linked list and a hash map (dictionary) in Python. The LRU Cache follows the LRU eviction policy, where the least recently used items are removed first when the cache reaches its capacity.

Features

O(1) Time Complexity for get() and put() operations using a hash map and a doubly linked list.

Supports dynamic capacity (between 0 and 50).

Includes cache miss tracking and miss rate calculation.

Implements custom error handling for invalid input values.

Provides a print_cache() function to visualize the cache state.

Implementation Details

The implementation consists of the following key components:

1. Node Class

A class to represent each node in the doubly linked list:

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

2. LRU_Cache Class

This class implements the LRU Cache logic, including:

Insertion and Removal of nodes from the doubly linked list.

Hash Map (Dictionary) for O(1) lookup time.

Cache eviction when the limit is exceeded.

Miss Rate Calculation

Key Methods:

get(key): Retrieves the value of a given key if present, otherwise returns -1.

put(key, value): Inserts a key-value pair into the cache.

calc_miss_rate(): Computes the cache miss rate.

print_cache(): Displays the current state of the cache.

Constraints

Cache Capacity: Between 0 and 50 (inclusive).

Key and Value Range: Between 0 and 100 (inclusive).
