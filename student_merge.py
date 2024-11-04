from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    merge_dict = defaultdict(lambda:0)
    for dict in dicts:
        for key, value in dict.items():
            merge_dict[key]+=value
    
    return merge_dict


def merge_with_counter(*dicts):
    merge_dict = Counter()
    for dict in dicts:
        for key, value in dict.items():
            merge_dict[key]+=value
    
    return merge_dict