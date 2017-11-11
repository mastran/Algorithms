def kmp_table(w):
    t = [-1] * len(w)
    p, c = 1, 0
    l = len(w)
    while p < l:
        if w[p] == w[c]:
            t[p] = t[c]
            p, c = p+1, c+1
        else:
            t[p] = c
            c = t[c]
            while c >= 0 and w[p] != w[c]:
                c = t[c]

            p, c = p+1, c+1

    return t


def kmp_search(w, s, single_match=False):
    """

    :param w: The input string to search
    :param s: Input text to be searched
    :param single_match: True if only single match is to returned.
    :return:
    """
    t = kmp_table(w)
    p = []
    i, m = 0, 0
    l, z = len(w), len(s)

    while (m + i) < z:
        if w[i] == s[m + i]:
            i += 1
            if i == l:
                p.append(m)
                if single_match:
                    return p

                m, i = m + i, 0

        else:
            if t[i] > - 1:
                m, i = m + i - t[i], t[i]
            else:
                m, i = m + i + 1, 0

    return p

if __name__ == '__main__':
    print kmp_search('ABCDABD','ABC ABCDAB ABCDABCDABDE ABCDABD')

