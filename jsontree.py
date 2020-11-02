def get_tabs(n, symbol):
    return ''.join([symbol for i in range(n)])


def jsontree(json, symbol='\t', depth=0):
    tabs = get_tabs(depth, symbol)

    if depth == 0:
        print(jsontree(json, symbol, depth + 1))

    if isinstance(json, dict):
        items = ['{' + '\n']
        for k, v in json.items():
            items.append('{}"{}": {},\n'.format(tabs, k, jsontree(v, symbol, depth + 1)))
        items.append(get_tabs(depth - 1, symbol) + '}')
        return ''.join(items)
    elif isinstance(json, list):
        items = ['[' + '\n']
        for v in json:
            items.append('{}{},\n'.format(tabs, jsontree(v, symbol, depth + 1)))
        items.append(get_tabs(depth - 1, symbol) + ']')
        return ''.join(items)
    else:
        if isinstance(json, str):
            return '"{}"'.format(json)
        return str(json)
