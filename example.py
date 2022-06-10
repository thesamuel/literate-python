@lp
def is_palindrome(s: str):
    ## Heading 1
    ### Heading 2
    # Paragraph
    #- Bullet 1
    for i in range(len(s) // 2):
        # Next we check each character blah blah
        if not s[i] == s[len(s) - i]:
            return False

    return True
