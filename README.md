# codefactory-sandbox

A lightweight Python text statistics library. No external dependencies required.

## Usage

```python
from text_stats import count_words, count_chars, count_lines
from text_stats_advanced import top_words, avg_word_length

text = "The quick brown fox jumps over the lazy dog.\nThe dog barked back."

# Count words
count_words(text)
# => 13

# Count characters (with and without spaces)
count_chars(text)
# => 65
count_chars(text, with_spaces=False)
# => 54

# Count lines
count_lines(text)
# => 2

# Most frequent words
top_words(text, n=3)
# => [('the', 3), ('dog', 2), ('quick', 1)]

# Average word length
avg_word_length(text)
# => 3.92
```
