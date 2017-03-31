def is_palindrome_permutation(str):
    count = {}
    for c in list(str):
        if c.isalpha():
            c = c.lower()
            count[c] = count.get(c, 0) + 1

    odd_appearance_count = 0
    for c, count in count.iteritems():
        if count % 2 == 1:
            odd_appearance_count = odd_appearance_count + 1

        if odd_appearance_count > 1:
            return False

    return True

print is_palindrome_permutation('Tact Coa')
print is_palindrome_permutation('TCC atao')
print is_palindrome_permutation('TCC ata')
print is_palindrome_permutation('tct')
print '-----'
print is_palindrome_permutation('tc')
print is_palindrome_permutation('tcctaaabbb')
