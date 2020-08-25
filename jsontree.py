def jsontree(json, key=None, index=0, dct=False):
    if not isinstance(json, dict) and not isinstance(json, list):
        print(''.join(['\t' for i in range(index)]),
              f'"{key}": "{json}",')
        return True

    if isinstance(json, list):
        if not dct:
            print(''.join(['\t' for i in range(index)]), f'[')
        else:
            if key is None:
                print(''.join(['\t' for i in range(index)]), '{')
            else:
                print(''.join(['\t' for i in range(index)]), f'"{key}": {"{"}')

        for item in json:
            if isinstance(item, tuple):
                jsontree(item[1], key=item[0], index=index + 1)
            else:
                jsontree(item, index=index + 1)
        if not dct:
            print(''.join(['\t' for i in range(index)]), ']')

    elif isinstance(json, dict):
        jsontree(list(json.items()), key=key, index=index, dct=True)
        print(''.join(['\t' for i in range(index)]), '},')
