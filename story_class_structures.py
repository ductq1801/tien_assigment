class Character:
    """
    Store:
        name of character
        attribute scores (acumen, body, charm)
        proficient skill
    """

    max_attribute_score = 4
    min_attribute_score = 1
    attribute_fullname = {
        "A": 'acumen',
        "B": 'body',
        "C": 'charm'
    }
    skill_fullname = {
        "Di": "diplomacy",
        "In": "investigation",
        "Me": "medicine",
        "La": "language",
        "Ac": "acrobatics",
        "Cr": "craft"
    }
    total_attribute_score = 7
    skill_sequence_no_asterisk = 'Di In Me La Ac Cr'

    def __init__(self, string_input):
        """
        :param string_input:
            format:
                [Character name]
                A[num] B[num] C[num]
                Di In Me La Ac Cr
            valueError (Use raise ValueError):
                + out range score: invalid value for {}; {} is not in the range {} to {}
                + total 3 skill's scores: A{} B{} C{} is invalid, sum of attributes does not equal {}
                + One proficient skill only: {} is invalid; exactly one proficiency asterisk expected
                + format skills input: {} is invalid; unexpected skill name given
        """
        self.character_name = self.generate_character_name(string_input[0])
        self.attributes_with_scores = self.generate_attributes_with_score(string_input[1])
        self.proficient_skill = self.generate_proficient_skill(string_input[2])

    @staticmethod
    def generate_character_name(string_input):
        """
        :param string_input: [name]
        :return:
            name of character
        """
        return string_input

    def generate_attributes_with_score(self, string_input):
        """
        :param string_input: A[num] B[num] C[num]
        :return: a dict with pair key:value, "A":4
        """
        dict_of_attributes = {}
        sum_of_attributes = 0
        for attribute in string_input.split():
            attribute_short_name = attribute[0]
            attribute_score = int(attribute[1])  # assume no error at this

            # If score is out of range from min_score to max_score
            if attribute_score not in (self.min_attribute_score, self.max_attribute_score +1):
                message = 'invalid value for {}; {} is not in the range {} to {}'.format(self.attribute_fullname[attribute_short_name],
                                                                                         attribute_score,
                                                                                         self.min_attribute_score,
                                                                                         self.max_attribute_score)
                raise ValueError(message)
            else:
                # No attribute have score > 2 digits then add to the dict
                sum_of_attributes += attribute_score
                dict_of_attributes[attribute_short_name] = attribute_score
        # In case total score not as expected
        if sum_of_attributes != self.total_attribute_score:
            message = '{} is invalid, sum of attributes does not equal {}'.format(string_input, self.total_attribute_score)
            raise ValueError(message)
        return dict_of_attributes

    def generate_proficient_skill(self, string_input):
        """
        :param string_input: Di[*] In[*] Me[*] La[*] Ac[*] Cr[*]
        :return: 2 letters go even with *
        """
        # In case not 1 asterisk
        if string_input.count("*") != 1:
            message = '{} is invalid; exactly one proficiency asterisk expected'.format(string_input)
            raise ValueError(message)
        # In case not match given skill's names
        elif string_input.replace("*", "") != self.skill_sequence_no_asterisk:
            message = '{} is invalid; unexpected skill name given'.format(string_input)
            raise ValueError(message)
        else:
            asterisk_index = string_input.index("*")  # this return the index of first *
            # a bit tricky here cuz only 2 letters for all skill's name
            return self.skill_fullname[string_input[asterisk_index-2:asterisk_index]]

    def get_acumen(self):
        return self.attributes_with_scores["A"]

    def get_body(self):
        return self.attributes_with_scores["B"]

    def get_charm(self):
        return self.attributes_with_scores["C"]

    def get_name(self):
        return self.character_name

    def get_proficient(self):
        return self.proficient_skill

    def make_check(self, skill_or_attribute_name, difficulty, override_random):
        pass

    def __str__(self):
        """
        :return: {name} [{attribute_score}] is proficient in {proficient}
        -->  Marian Croak [A4 B1 C2] is proficient in investigation
        """
        return '{} [{}] is proficient in investigation'.format(0, 0)


class Story:
    """
    Store:

    """
    def __init__(self):
        pass


class Scene:
    """
    Store:
    ID
    Description
    List of choices depend on skill/attribute, each choice could be list of possible continue scene
       when compare the skill/attribute
    """
    def __init__(self):
        pass


