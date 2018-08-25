from unittest import TestCase
from txtStat import *


class txtStat(TestCase):
    custom_text = """Narration is telling a story from a certain viewpoint, and there is usually a reason for the telling. All narrative essays will have characters, setting, climax, and most importantly, a plot. The plot is the focus of the story and is usually revealed chronologically, but there are sometimes flash forwards and flash backs."""
    c = txtStat(custom_text)

    def test_get_character_count(self):
        text = self.c.get_average_sentence_length();
        print("test_get_character_count")
        assert (self.c)
