import re
regEx1 = re.compile(r'\d{3}-\d{3}-\d{4}')
m = regEx1.search('111-111-1111')

print(m.group(0))
# | >>> from Text_Manipulation.regex import *
# | 111-111-1111

#---------------------------------------------------------------

regEx2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
m = regEx2.search('111-111-1111')

print(m.group(0))
# | 111-111-1111

print(m.group(1))
# | 111

print(m.group(2))
# | 111-1111

print(m.groups())
# | >>> print(m.groups())
# | ('111', '111-1111')

areacode, mainnumber = m.groups()

print(areacode)

print(mainnumber)
# | >>> areacode, mainnumber = m.groups()
# | >>> print(areacode)
# |
# | 111
# | >>> print(mainnumber)
# | 111-1111
# |

phoneNumberRegEx = re.compile(r'(\d{3})-(\d{3}-\d{4})')

mo = phoneNumberRegEx.findall('Cell: 111-123-4567 Work: 555-567-9878')

print(mo)
# [('111', '123-4567'), ('555', '567-9878')]

# | >>> for group in mo:
# | ...     print(group)
# | ...
# | ('111', '123-4567')
# | ('555', '567-9878')


# | >>> for i in range(len(mo)):
# | ...     for j in range(len(mo[i])):
# | ...         print(mo[i][j])
# | ...
# | 111
# | 123-4567
# | 555
# | 567-9878

# | \d any numeric digit from 0 - 9
# | \D any character that is not a numeric digit 0 - 9
# |
# | \w any letter, numeric digit, ot the underscore
# | \W any character that is not a letter, numeric digit, ot the underscore
# |
# | \s any space, tab, newline
# | \S any character that is not a any space, tab, newline

# |  Character Class
# |  [0-5]
# | Only matches the numbers 0,1,2,3,4,5

# | [aeiouAEIOU]
# | [^aeiouAEIOU] not version or Inverse
# | [a-zA-Z0-9]
# | [^a-zA-Z0-9]