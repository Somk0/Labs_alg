from collections import deque

def build_finite_automaton(pattern):
    
    alphabet = set(pattern) 
    m = len(pattern)
    transition_table = [{} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != (pattern[:state] + char)[-next_state:]:
                next_state -= 1
            transition_table[state][char] = next_state
    
    return transition_table

def finite_automaton_search(haystack, needle):
    
    if not needle:
        return []
    
    transition_table = build_finite_automaton(needle)
    m = len(needle)
    n = len(haystack)
    state = 0
    occurrences = []
    
    for i in range(n):
        char = haystack[i]
        if char in transition_table[state]:
            state = transition_table[state][char]
        else:
            state = 0
        
        if state == m:
            start_index = i - m + 1
            occurrences.append(start_index)
    
    return occurrences
