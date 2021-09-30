

import re

target_string = "Jessa loves Python and pandas"
# Match six-letter word
pattern = r"\w{5}"

# match() method
result = re.match(pattern, target_string)
print(result)