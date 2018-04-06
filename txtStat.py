__author__ = 'Suresh Melvin Sigera'

import re


class txtStat():
    strr = ""

    def __init__(self, fulltext):
        """
        ReadabilityScore(fulltext)
        """
        self.fulltext = fulltext
        print(fulltext)

    def get_character_count(self, include_spaces=True):
        """
        :param include_spaces
        :type True: include spaces in the character count (default)
        :type False:exclude spaces in the character count
        """
        character_count = list
        if include_spaces:
            # Characters (including spaces)
            character_count = len(re.sub(r'([0-9]+)\s+(st|nd|rd|th)\b', '\\1\\2', self.fulltext))
            return character_count
        else:
            # Characters (without spaces)
            character_count = len(re.findall("(\S)", self.fulltext))
            return character_count

    def get_word_count(self):
        """
        """
        # word_count = list
        # word_count = len(re.findall("(\S)", self.fulltext))
        # return word_count
        word_count = len(re.split("\s+", self.fulltext.lower()))
        return word_count

    def get_sentence_count(self):
        sentence_count = len(re.split(r'\s*[!?.]\s*', self.fulltext.lower()))
        return sentence_count

    def get_average_sentence_length(self):
        asl = float(self.get_word_count() / self.get_sentence_count())
        return round(asl, 2)

    def get_average_number_of_syllable_per_word(self):
        asw = float(self.get_syllable_count() / self.get_word_count())
        return round(asw, 2)

    def get_syllable_count(self, isName=True):
        """
        """
        vowels = "aeiouy"
        # single syllables in words like bread and lead, but split in names like Breanne and Adreann
        specials = ["ia", "ea"] if isName else ["ia"]
        # seperate syllables unless ending the word
        specials_except_end = ["ie", "ya", "es", "ed"]
        currentWord = self.fulltext.lower()
        numVowels = 0
        lastWasVowel = False
        last_letter = ""

        for letter in currentWord:
            if letter in vowels:
                # don't count diphthongs unless special cases
                combo = last_letter + letter
                if lastWasVowel and combo not in specials and combo not in specials_except_end:
                    lastWasVowel = True
                else:
                    numVowels += 1
                    lastWasVowel = True
            else:
                lastWasVowel = False
                last_letter = letter

            # remove es & ed which are usually silent
            if len(currentWord) > 2 and currentWord[-2:] in specials_except_end:
                numVowels -= 1

            # remove silent single e, but not ee since it counted it before and we should be correct
            elif len(currentWord) > 2 and currentWord[-1:] == "e" and currentWord[-2:] != "ee":
                numVowels -= 1
        return numVowels

    def get_flesch_reading_ease_score(self):
        """
        fres = (0.39 x ASL) + (11.8 x ASW) - 15.59
        Where,FKRA = Flesch-Kincaid Reading Age
        ASL = Average Sentence Length (i.e., the number of words divided by the number of sentences)
        ASW = Average number of Syllable per Word (i.e., the number of syllables divided by the number of words)
        """
        school_levels = ('5th grade', '6th grade', '7th grade', '8th & 9th grade', '10th to 12th grade', 'College',
                         'College Graduate')
        school_level = ""
        # fres = round(206.835 - (1.015 * self.rs_average_sentence_length()) - (
        # 84.6 * self.rs_average_number_of_syllable_per_word()),2)
        fres = round(206.835 - (1.015 * self.get_average_sentence_length()) - (
                84.6 * self.get_average_number_of_syllable_per_word()), 2)

        if fres < 30.0 and 0.0:
            return (school_levels[0], fres)
        elif fres < 50.0 and 30.0:
            return (school_levels[1], fres)
        elif fres < 60.0 and 50.0:
            return (school_levels[2], fres)
        elif fres < 70.0 and 60.0:
            return (school_levels[3], fres)
        elif fres < 80.0 and 70.0:
            return (school_levels[4], fres)
        elif fres < 90.0 and 80.0:
            return (school_levels[5], fres)
        elif fres > 90.00 and 100.00:
            return (school_levels[6], fres)

    def get_flesch_kincaid_grade_level(self):
        fkgl = 0.39 * self.get_average_sentence_length() + (11.8
                                                            * self.get_average_number_of_syllable_per_word() - 15.59)
        return round(fkgl, 2)

    def get_gunning_fogscore(self):
        """

        """
        pass

    def get_coleman_liau_index(self):
        """

        """
        pass

    def get_smog_index(self):
        """

        """
        pass

    def get_linsear_write_formula(self):
        pass


if __name__ == "__main__":
    custom_text = """Word Counter can do more than just count words and characters. It can improve word choice and writing style, and, optionally, help you to detect grammar mistakes and plagiarism. To check word count, simply place your cursor into the box above and start typing. You'll see the number of characters and words increase or decrease as you type, delete, and edit them. You can also copy and paste text from another program over into the box above. The Auto-Save feature will make sure you won't lose any changes while editing, even if you leave the site and come back later.

Knowing the word count of a text can be important. For example, if an author has to write a minimum or maximum amount of words for an article, essay, report, story, book, paper, you name it. Word Counter will help to make sure its word count reaches a specific requirement or stays within a certain limit.

In addition, Word Counter shows you the top 10 keywords and keyword density of the article you're writing. This allows you to know which keywords you use how often and at what percentages. This can prevent you from over-using certain words or word combinations and check for best distribution of keywords in your writing.

In the Details overview you can see the average speaking and reading time for your text, while Reading Level is an indicator of the education level a person would need in order to understand the words you’re using.

Disclaimer: We strive to make our tools as accurate as possible but we cannot guarantee it will always be so."""
    r = txtStat(custom_text)
    s = r.get_average_number_of_syllable_per_word()
    s = r.get_flesch_kincaid_grade_level()
    s = r.get_flesch_reading_ease_score()
    print(s)