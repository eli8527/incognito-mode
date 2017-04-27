from escpos.printer import File, Dummy
import popen2
import os
import textwrap

class Receipt:

    def __init__(self, uid):
        self.p = Dummy()

        self.id = uid
        # self.p.set("center", "b", "NORMAL", 2, 2)
        # self.p.text("DO NOT\n")
        # self.p.set("center", "b", "NORMAL", 1, 1)
        # self.p.text("Participant " + str(uid) + "\n")

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
    r.addQuestionAnswer("", "What the fuck did you just fucking say about me, you little shit? Ill have you know I graduated top of my class in the Navy Seals, and Ive been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and Im the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. Youre fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and thats just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little clever comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldnt, you didnt, and now youre paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. Youre fucking dead, kiddo.")

    r.saveToText("out.txt")
    popen2.popen4("lpr -P THERMAL -o raw out.txt")

if __name__ == "__main__":
    main()
