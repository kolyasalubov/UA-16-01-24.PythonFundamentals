philosophy = """
BEAUTIFUL IS BETTER THAN UGLY.
EXPLICIT IS BETTER THAN IMPLICIT.
SIMPLE IS BETTER THAN COMPLEX.
COMPLEX IS BETTER THAN COMPLICATED.
FLAT IS BETTER THAN NESTED.
SPARSE IS BETTER THAN DENSE.
READABILITY COUNTS.
SPECIAL CASES AREN'T SPECIAL ENOUGH TO BREAK THE RULES.
ALTHOUGH PRACTICALITY BEATS PURITY.
ERRORS SHOULD NEVER PASS SILENTLY.
UNLESS EXPLICITLY SILENCED.
IN THE FACE OF AMBIGUITY, REFUSE THE TEMPTATION TO GUESS.
THERE SHOULD BE ONE-- AND PREFERABLY ONLY ONE --OBVIOUS WAY TO DO IT.
ALTHOUGH THAT WAY MAY NOT BE OBVIOUS AT FIRST UNLESS YOU'RE DUTCH.
NOW IS BETTER THAN NEVER.
"""

philosophy = philosophy.upper()

philosophy_r = philosophy.replace('I', '&')
words_better = philosophy.count('BETTER')
words_never = philosophy.count('NEVER')
words_is = philosophy.count('IS')

print("Uppercase Text: ")
print(philosophy)

print(" Text with 'i' replaced by '&'")
print("Occurrences:")
print(f"Number of 'BETTER': {words_better}")
print(f"Number  of 'NEVER': {words_never}")
print(f"Number of 'IS': {words_is}")
