def get_all_combinations(source, size):
    if size > len(source):
        raise ValueError('size is greater than source')
    if size <= 1 or len(source) <= 2:
        return source

    if not isinstance(source, list):
        source = list(source)

    def build_combinations(source, size):
        if size == len(source):
            return [list(source)]

        result = []
        if size == 2:
            for i in xrange(len(source) - 1):
                for j in xrange(i + 1, len(source)):
                    result.append([source[i], source[j]])
        else:
            for i in xrange(len(source) - size + 1):
                i_result = build_combinations(source[i + 1:], size - 1)
                for c in i_result:
                    c.insert(0, source[i])
                result.extend(i_result)
        return result

    return build_combinations(source, size)
