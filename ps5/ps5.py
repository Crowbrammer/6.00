# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
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
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):

    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_subject(self):
        return self.subject

    def get_summary(self):
        return self.summary

    def get_link(self):
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

    def __init__(self, word):
        self.word = word

    def is_word_in(self, word, text):
        """
        Checks if the words is in the text.
        """
        word = self.word.lower()
        text = text.lower()

        for punc in string.punctuation:
            text = text.replace(punc, " ")
        splittext = text.split(" ")

        return word in splittext

        # if word.lower() in text.lower():
        #     return True
        # else:
        #     return False

# TODO: TitleTrigger

class TitleTrigger(WordTrigger):

    # def _init_(self, word):
    #     WordTrigger().__init__(**kwargs)
        #self.title = title

    def evaluate(self, story):
        return self.is_word_in(self.word, story.get_title())

# TODO: SubjectTrigger

class SubjectTrigger(WordTrigger):

    # def __init__(self, word):
    #     super(SubjectTrigger, self).__init__(**kwargs)

    def evaluate(self, story):
        return self.is_word_in(self.word, story.get_subject())

# TODO: SummaryTrigger

class SummaryTrigger(WordTrigger):

    # def __init__(self, word):
    #     super(SummaryTrigger, self).__init__(**kwargs)

    def evaluate(self, story):
        return self.is_word_in(self.word, story.get_summary())

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger

class NotTrigger(Trigger):

    # def __init__(self, T, x):
    #     return not T.evalute(x)
    # def __init__(self, t):
    #     self.trigger = t
    def __init__(self, trigger):
        self.t = trigger

    def evaluate(self, story):
        return not self.t.evaluate(story)

# TODO: AndTrigger

class AndTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) and self.t2.evaluate(story)

# TODO: OrTrigger

class OrTrigger(Trigger):

    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2

    def evaluate(self, story):
        return self.t1.evaluate(story) or self.t2.evaluate(story)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger

class PhraseTrigger(Trigger):

    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        #phrase = self.phrase

        return self.phrase in story.get_title() or \
                self.phrase in story.get_summary() or \
                self.phrase in story.get_subject() or \
                self.phrase in story.get_link()

# class PhraseTrigger(Trigger):
#
#     def __init__(self, phrase):
#         self.phrase = phrase
#
#     def evaluate(self, story):
#         return self.phrase in self.is_word_in(self.phrase, story.get_title()) or \
#             self.is_word_in(self.phrase, story.get_summary())


#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    # Feel free to change this line!
    accepted_stories = []
    # print(stories)
    #print("f_s triggerlist:", triggerlist)
    for story in stories:
        for trigger in triggerlist:
            #print(">>> f_s trigger", trigger)
            if trigger.evaluate(story):
                accepted_stories.append(story)
                break

    print([story for story in accepted_stories])
    return accepted_stories

#======================
# Part 4
# User-Specified Triggers
#======================

# def makeTrigger(tigger_type, trigger_map, params, name):
#
#     if trigger_type = "TITLE":
#         pass
#     elif trigger_type = "SUBJECT":
#         pass
#     elif trigger_type = "SUMMARY":
#         pass
#     elif trigger_type = "PHRASE":
#         pass
#     elif trigger_type = "AND":
#         pass
#     elif trigger_type = "NOT":
#         pass
#     elif trigger_type = "OR":
#         pass
#     else:
#         return None
#
#     trigger_map

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
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones
    triggers = {}
    active_triggers = []
    for each in lines:
        separate_words = each.split(" ")
        # print(">>> separate_words[1]:", separate_words[1])
        if separate_words[0].upper() != "ADD":
            if separate_words[1].upper() == "TITLE":
                # print("TITLE")
                # Make sure there's only one word...
                triggers[separate_words[0]] = TitleTrigger(separate_words[2])
            elif separate_words[1].upper() == "SUBJECT":
                triggers[separate_words[0]] = SubjectTrigger(separate_words[2])
            elif separate_words[1].upper() == "PHRASE":
                #phrase =
                # print(phrase)
                triggers[separate_words[0]] = PhraseTrigger(" ".join(separate_words[2:]))
            elif separate_words[1].upper() == "AND":
                triggers[separate_words[0]] = AndTrigger(triggers[separate_words[2]], triggers[separate_words[3]])
        else:
            print("separate_words:", separate_words)
            for trigger_name in separate_words[1:]:
                print(">>> triggers:", triggers)
                active_triggers.append(triggers[trigger_name])
                #print(">>> active_triggers:", active_triggers)
        print("active_triggers:", active_triggers)
    return active_triggers

#readTriggerConfig("triggers.txt")

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # # this with something more configurable in Problem 11
    # t1 = SubjectTrigger("Obama")
    # t2 = SummaryTrigger("MIT")
    # t3 = PhraseTrigger("Supreme Court")
    # t4 = OrTrigger(t2, t3)
    # triggerlist = [t1, t4]

    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []

    while True:
        print("Polling...")

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)

        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)

        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print("Sleeping...")
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()
