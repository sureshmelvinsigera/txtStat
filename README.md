# txtStat

The txtStat tool calculates the readability indicators such as Flesch Kincaid Reading Ease, Flesch Kincaid Grade Level.

## Usage

```python
from txtStat import *

if __name__ == '__main__':
    custom_text = """
    Narration is telling a story from a certain viewpoint, and there is usually a reason for the
    telling. All narrative essays will have characters, setting, climax, and most importantly, a plot. The plot is the
    focus of the story and is usually revealed chronologically, but there are sometimes flash forwards and flash backs.
    """
    content = txtStat(custom_text)
    c = content.get_average_sentence_length()
    print(c)
```