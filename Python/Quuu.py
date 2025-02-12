st = 'The quick brown fox jumps over the lazy dog.'

def is_pangram(st):
    st.lower()
    pan_st = set()
    
    for ch in st:
        if ch.isalpha():
            pan_st.add(ch)
            
    if len(pan_st) == 26:
        return True
    else:
        return False


is_pangram(st)

