"""This final project is designed to incorporate all the tools learned throughout the course. 
You will need to create a class named ChatSesssion where it will have a constructor that will take in a parameter called filename. 
The constructor will create include the following variables:

        self.numLines = 0
        self.TagsList = []
        self.MembersList = []
        self.TimesList = []
        self.UniqueMembersList = []
        self.UniqueTagsList = []
        self.MessageList = []

It should open the file and begin reading each line and populating the variables above in a for loop

        f = open(filename, "r")
        records = f.readlines()

        for record in records:

                      ............................

The file consists of Tags, Timestamps, Members, Users, and Messages. 
Because there are multiple members you will need to create a Unique members list that hold the name of the unique members as well as unique tags. 
The class should contain the following tags that will return the information above:

    GetNumLines(self):
    GetTagsList(self):
    GetTimesList(self):
    GetMembersList(self):
    GetUserSysList(self):
    GetUniqueMembersList(self):
    GetUniqueTagsList(self):
    GetMessageList(self):

Create an object to test out all the information above as follows:  

sessionObj = ChatSessions('iphone_07_18-1.annot')

** Note: The file data is of the type:

T-1 20816 Eryn * entered the room.

where

T-1 is the tag
20816 is the timestamp
Eryn is the member
*  (asterisk) is the UserSys symbol
entered the room. is the message
Upload the Python Files so that I may be able to test out your code. Do not simply upload an image of the code.

Good luck and enjoy!"""

from ClassSessions import ChatSessions

sessionObj = ChatSessions('iphone_07_18-1.annot')
num = sessionObj.GetNumLines()
tags = sessionObj.GetTagsList()
times = sessionObj.GetTimesList()
members = sessionObj.GetMembersList()
userSys = sessionObj.GetUserSysList()
uniqueMembers = sessionObj.GetUniqueMembersList()
uniqueTags = sessionObj.GetUniqueTagsList()
messages = sessionObj.GetMessageList()

# print(num)
# print(tags)
# print(times)
# print(members)
# print(userSys)
print(uniqueTags)
# print(uniqueMembers)
# print(messages)