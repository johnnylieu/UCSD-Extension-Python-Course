import re

class ChatSessions:
    numLines = 0
    TagsList = []
    MembersList = []
    UserSysList = []
    TimesList = []
    UniqueMembersList = []
    UniqueTagsList = []
    MessageList = []

    def __init__(self, file):
        self.file = file

    def GetNumLines(self):
        with open(self.file, 'r') as file:
            for line in file:
                self.numLines += 1
        
        return self.numLines
    
    def GetTagsList(self):
        regex = r'^T-?\d+ '
        """
        ^ asserts the start of the line.
        T-? matches the letter "T" followed by an optional hyphen.
        \d+ matches one or more digits.
        ' ' matches a space character, indicating the end of the series of numbers.
        """

        with open(self.file, 'r') as file:
            for line in file:
                match = re.match(regex, line)
                if match:
                    tag = match.group(0)  # Extract the matched portion
                    self.TagsList.append(tag)
        
        return self.TagsList
    
    def GetTimesList(self):
        regex = r'T-?\d+\s(\d+)'

        with open(self.file, 'r') as file:
            for line in file:
                matches = re.findall(regex, line)
                if matches:
                    self.TimesList.extend(matches)
        
        return self.TimesList

    def GetMembersList(self):
        regex = r'^T-?\d+\s\d+\s(\w+)\s\*'
        """
        this matches the series number "T-1", 
        followed by more than one digit then a space, 
        then captures the name using the parentheses \w+, 
        and finally matches a space followed by an asterisk symbol. 
        """
        with open(self.file, 'r') as file:
            for line in file:
                matches = re.findall(regex, line)
                if matches:
                    self.MembersList.extend(matches)

        return self.MembersList


    def GetUserSysList(self):
        regex = r'T-?\d+\s\d+\s\w+\s([*:])\s'
        """
        matches the series number "T-1", 
        followed by a space, captures the name, 
        then matches either a * or : character, 
        followed by a space.
        """

        with open(self.file, 'r') as file:
            for line in file:
                matches = re.findall(regex, line)
                if matches:
                    self.UserSysList.extend(matches)

        return self.UserSysList

    
    def GetUniqueMembersList(self):
        regex = r'T-\d+\s(\w+)\s\*'

        with open(self.file, 'r') as file:
            for line in self.file:
                if re.match(regex, line) and line == re.match.group(1):
                    self.UniqueMembersList.append(line)

        return self.UniqueMembersList
    
    def GetUniqueTagsList(self):
        regex = r'^T-?\d*$'

        with open(self.file, 'r') as file:
            for line in self.file:
                if re.match(regex, line) and line == re.match.group(1):
                    self.UniqueTagsList.append(line)
        
        return self.UniqueTagsList
    
    def GetMessageList(self):
        regex = r'T-\d+\s\w+\s\* (.*)'
        """
        T-\d+: This part matches "T-" followed by one or more digits.
        \s: This matches a whitespace character.
        \w+: This matches one or more word characters (letters, digits, or underscores) representing the name.
        \s\*: This matches a space followed by an asterisk symbol *.
        (.*): This part captures any characters (except newline characters) after the asterisk symbol *
        """

        with open(self.file, 'r') as file:
            for line in self.file:
                if re.match(regex, line):
                    self.MessageList(line)