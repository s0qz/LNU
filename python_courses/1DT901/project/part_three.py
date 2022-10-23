#!/usr/bin/env python3
import io
import lzma
from time import time
from typing import List

import BstMap as bst
import HashSet as hset


def get_words(path: str, file_name: str) -> List[str]:
    with lzma.open(path + "/" + file_name) as compressed:
        with io.TextIOWrapper(compressed, encoding="utf-8") as text_file:
            return text_file.readlines()


def top_ten(lst: List[str]) -> List[str]:
    items = bst.BstMap()
    for item in lst:
        a = items.get(item)
        if a is None:
            a = 0
        items.put(item, a + 1)

    tree = items
    # Dra ut allting kortare än 4 bokstäver
    items = [item for item in items.as_list() if len(item[0]) > 5]
    # Sortera efter hur ofta det förekommer
    items = sorted(items, key=lambda x: items[x[1]], reverse=True)
    return items[:10], tree


for file_name in ["life_of_brian.txt.xz", "swe_news.txt.xz"]:
    start = time()
    words = get_words("./data", file_name)

    # Unique words/HashSet
    unique_words = hset.HashSet()
    unique_words.init()
    for word in words:
        unique_words.add(word)

    # Top 10 words/BstMap
    tt, tt_tree = top_ten(words)

    print(f"=== {file_name} ===")
    print("\n=== HashSet ===")
    print(f" The total amount of unique words were {unique_words.get_size()}")
    print(f" Bucket list size {unique_words.bucket_list_size()}")
    print(f" Max bucket size {unique_words.max_bucket_size()}")
    print(f" Zero bucket ratio {unique_words.zero_bucket_ratio()}")
    print("\n=== BstMap ===")
    print(f" Nodes in tree {tt_tree.size()}")
    print(f" Trees max depth {tt_tree.max_depth()}")
    print(f" Amount of leafs on tree {tt_tree.count_leafs()}")
    print(" The most used words were")
    for index, value in enumerate(tt):
        print(f"  {index + 1}. {value[0].rstrip()}")
    print(f"\n Elapsed time {round(time() - start, 2)} seconds\n")
