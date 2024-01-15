def ExtractPaths(content:list, key:str):

    all_paths = []
    for _content in content:
        for _key , _value in _content.items():
            if _key == key:
                all_paths.append(_value)

    return all_paths