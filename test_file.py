from jinevra import nd_parser as nd
from nltk import word_tokenize as wt

es = '"I think that\'s a great idea, Bob," I said with a smile.  "Really smart!".'
print("It is %s that the text is s string." % isinstance(es, str))
print("text is s string")
print("Test #1 - string with nd")
n = nd.narrative_dialog(es, "“", "“")

print("tokenized string")
m = ['``', 'I', 'think', 'that', "'s", 'a', 'great', 'idea', ',', 'Bob', ',', "''", 'I', 'said', 'with', 'a', 'smile', '.', '``', 'Really', 'smart', , '!', '"']
o = nd.narrative_dialog(m, '``', "''")
print(o)
