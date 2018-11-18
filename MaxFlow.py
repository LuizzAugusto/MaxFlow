# It's distributed under the MIT license (https://choosealicense.com/licenses/mit/)

import copy

state = {'json': None, 'value': None}

def start(start_vertex, finish_vertex):
    ways = state['json']

    if ways:
        _algorithm(ways, start_vertex, finish_vertex)
    else:
        print('open a JSON file first.')

def _algorithm(ways, key, finish_vertex):
    result = {'not_empty':'not_false'}
    counter = 10

    while result and counter > 0:
        result = _maxFlow(ways, key, finish_vertex, {'path':[],'max_values':[]})

        if result:
            value = dict(result)
            min_value = min(value['max_values'])
            previous_vertex = None

            for vertex in value['path']:
                if previous_vertex:
                    ways[previous_vertex][vertex] -= min_value
                    ways[vertex][previous_vertex] += min_value

                previous_vertex = str(vertex)

        counter -= 1

    print(ways)

def _maxFlow(ways, vertex_key, finish_vertex, result):
    if vertex_key == finish_vertex:
        _addVertexToPath(vertex_key, result['path'])
        return result

    temp_result = None
    ways_copy = copy.deepcopy(ways)

    while not temp_result and ways_copy[vertex_key]:
        vertex = ways_copy[vertex_key]
        _addVertexToPath(vertex_key, result['path'])
        max_value = _maxValue(vertex, result['path'])

        if max_value == 0:
            return None

        next_vertex_key = _nextVertex(vertex, max_value)
        ways_copy = _removeVertexKey(ways_copy, next_vertex_key)
        temp_result = _maxFlow(ways_copy, next_vertex_key, finish_vertex, result)
        _persistResultOrRemoveLastPath(max_value, temp_result, result)

    return result

def _maxValue(vertex, path):
    vertex_copy = copy.deepcopy(vertex)
    keys = tuple(vertex_copy.keys())
    
    for key in keys:
        if key in path:
            del vertex_copy[key]

    try:
        max_value = max(tuple(vertex_copy.values()))
    except:
        max_value = 0
    
    return max_value

def _nextVertex(vertex, max_value):
    vertex_keys = tuple(vertex.keys())
    index = _valueIndex(vertex, max_value)

    return str(vertex_keys[index])

def _valueIndex(vertex, max_value):
    vertex_values = tuple(vertex.values())

    for index, value in enumerate(vertex_values):
        if(value == max_value):
            return index

def _removeVertexKey(ways, key):
    for vertex in ways.values():
        if key in vertex:
            del vertex[key] 
    
    return ways

def _removeLastPath(path):
    del path[-1]

def _addVertexToPath(vertex_key, path):
    if vertex_key not in path:
        path.append(vertex_key)

def _persistResultOrRemoveLastPath(max_value, temp_result, result):
    if temp_result:
            result['max_values'].append(max_value)
    else:
        _removeLastPath(result['path'])