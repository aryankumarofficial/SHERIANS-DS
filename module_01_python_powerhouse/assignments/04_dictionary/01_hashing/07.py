from typing import List, Dict


def sort_people(names: List[str], height: List[int]) -> List[str]:
    mp: Dict[int, str] = {}
    for i in range(len(names)):
        mp[height[i]] = names[i]
    sorted_names = dict(sorted(mp.items(), key=lambda x: x[0], reverse=True))
    names.clear()
    for i in sorted_names:
        names.append(sorted_names.get(i))
    return names


print(sort_people(["Mary", "John", "Emma"], [180, 165, 170]))
