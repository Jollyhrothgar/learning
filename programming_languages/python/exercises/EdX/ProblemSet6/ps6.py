# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 6

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    '''
    Usage: NewsStory(guid, title, subject, summary, link)
    NewsStory stores important elements of a RSS feed news story as python strings
    guid: a string, representing a globally unique identifier (GUID), must be 'unique'
    title: a string which is the title of a news story
    subject: a string which is the subject of a news story
    summary: a string which is summarizes the news story
    link: a string containing a link to more content

    This class stores these data internally, which can be accessed via get methods, ie
    getGuid, getTitle, getSubject, getSummary, getLink
    '''
    def __init__(self, RSSguid, RSStitle, RSSsubject, RSSsummary, RSSlink):
        self.guid = RSSguid
        self.title = RSStitle
        self.subject = RSSsubject
        self.summary = RSSsummary
        self.link = RSSlink
    def getGuid(self):
        return self.guid
    def getTitle(self):
        return self.title
    def getSubject(self):
        return self.subject
    def getSummary(self):
        return self.summary
    def getLink(self):
        return self.link
#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    '''
    Word Trigger derives from Trigger and takes a string as an argument
    Usage: WordTrigger(word)
    word: a string representing a trigger word.

    Member methods:
        clearPunctuation: takes a string, recursively replaces all punctuation found in
        string.punctuation with a single space

        isWordIn: checks to see if word is in text
        Contains member method to recursively wipe punctuation characters from
        word
    '''
    def __init__(self, TriggerWord):
        self.word = TriggerWord.lower()
    def isWordIn(self, text):
        clearText = self.clearPunctuation(text)
        clearText = clearText.lower()
        lowerCaseWords = clearText.split()
        foundFlag = False
        for checkWord in lowerCaseWords:
            if self.word.lower() == checkWord:
                foundFlag = True
        return foundFlag
    
    def clearPunctuation(self,text):
        if len(text) == 0:
            return text
        elif text[0] in string.punctuation:
            return " "+self.clearPunctuation(text[1:len(text)])
        else:
            return text[0]+self.clearPunctuation(text[1:len(text)])

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    '''
        We inherit wholly the structure of WordTrigger. This class only need contain a flag
        as to whether or not self.word was contained in the text. Therefore, we call the inherited
        checker giving it the story.getTitle() as a searchable string
    '''
    def evaluate(self, story):
        '''
            story: a newsStory Object
        '''
        if self.isWordIn(story.getTitle()):
            return True
        else:
            return False
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        '''
            story: a newsStory Object
        '''
        if self.isWordIn(story.getSubject()):
            return True
        else:
            return False
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        '''
            story: a newsStory Object
        '''
        if self.isWordIn(story.getSummary()):
            return True
        else:
            return False

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, Trigger):
        self.T = Trigger
    def evaluate(self,story):
        return not self.T.evaluate(story)
    
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, aTrigger, bTrigger):
        self.T1 = aTrigger
        self.T2 = bTrigger
    def evaluate(self,story):
        return self.T1.evaluate(story) and self.T2.evaluate(story)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, T1, T2):
        self.T1 = T1
        self.T2 = T2
    def evaluate(self,story):
        return self.T1.evaluate(story) or self.T2.evaluate(story)
# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    def evaluate(self,story):
        if self.phrase in story.getSubject():
            return True
        elif self.phrase in story.getTitle():
            return True
        elif self.phrase in story.getSummary():
            return True
        else:
            return False
      

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    filteredStories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) is True and story not in filteredStories:
                filteredStories.append(story)
    return filteredStories

#======================
# Part 4
# User-Specified Triggers
#======================

# http://pastebin.com/CFP9w99K

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns: None
    """
    for param in params:
        triggerMap[triggerType](param)
    # TODO: Problem 11
    # This method is called within readTriggerConfig, after we read in the config file.

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    # all is a special iterative function, rstrip is a memberfunction for strings.
    # it looks like all fills itself with lines, after stripping trailing characters according to
    # the iteration rule (for line in triggerfile.readlines())
    # .readlines() reads until EOF using readline (keeping trailing characters) storing each line in
    # a list
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []

    # why do we need all? I guess this is short-hand?
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:
        
        linesplit = line.split(" ")

        # Making a new trigger
        # here, we obtain triggers which are not added
        if linesplit[0] != "ADD":
            # Args: triggerMap: an empty dict
            # linesplit[1]: Trigger Type
            # linesplit[2:]: All words which will fire the trigger (in list form)
            # linesplit[0]: the name of the trigger
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # from here is about drawing
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

