from escpos.printer import File, Dummy
import popen2
import os
import textwrap

class Receipt:

    def __init__(self, uid):
        self.p = Dummy()

        self.id = uid
        self.p.set("center", "b", "NORMAL", 2, 2)
        self.p.text("DO NOT\n")
        self.p.set("center", "b", "NORMAL", 1, 1)
        self.p.text("Participant " + str(uid) + "\n")

    def saveToText(self, fn):
        f = File(fn)
        f._raw(self.p.output)
        f.cut()

    def addQuestionAnswer(self, q, a):
        self.p.set("left","a", "NORMAL")

        qlines = textwrap.wrap(q, 30)
        for line in qlines:
            print line
            self.p.text(line + "\n")

        self.p.set("left","b", "NORMAL")
        alines = textwrap.wrap(a, 40)
        for line in alines:
            self.p.text(line + "\n")

        self.p.text("\n")


def main():
    r = Receipt(239)
    # r.addQuestionAnswer("What is your name? What is your name?", "My name is Jeff Snyder. My name is Jeff Snyder. My name is Jeff Snyder. My name is Jeff Snyder.")
    # r.addQuestionAnswer("What is your name? I would like to ask you something? But what if this cuts something off", "My name is Jeff Snyder. OK.")
    # r.addQuestionAnswer("What is your name?", "OK")

    r.saveToText("out.txt")
    popen2.popen4("lpr -P THERMAL -o raw out.txt")

if __name__ == "__main__":
    main()
