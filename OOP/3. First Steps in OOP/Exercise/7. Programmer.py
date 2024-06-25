class Programmer:

    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):

        if self.language == language:
            self.skills += skills_earned
            return '{} watched {}'.format(self.name, course_name)
        return '{} does not know {}'.format(self.name, language)

    def change_language(self, new_language, skills_needed):

        if new_language != self.language and skills_needed <= self.skills:
            previous_language = self.language
            self.language = new_language
            return '{} switched from {} to {}'.format(self.name, previous_language, new_language)

        elif skills_needed <= self.skills and self.language == new_language:
            return '{} already knows {}'.format(self.name, new_language)

        needed_skills = self.skills - skills_needed
        return '{} needs {} more skills'.format(self.name, needed_skills)
class Programmer:

    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):

        if self.language == language:
            self.skills += skills_earned
            return '{} watched {}'.format(self.name, course_name)
        return '{} does not know {}'.format(self.name, language)

    def change_language(self, new_language, skills_needed):

        if new_language != self.language and skills_needed <= self.skills:
            previous_language = self.language
            self.language = new_language
            return '{} switched from {} to {}'.format(self.name, previous_language, new_language)

        elif skills_needed <= self.skills and self.language == new_language:
            return '{} already knows {}'.format(self.name, new_language)

        needed_skills = self.skills - skills_needed
        return '{} needs {} more skills'.format(self.name, needed_skills)
