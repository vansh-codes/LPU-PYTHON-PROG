#ASSISTANT
import random as r
import time as t
from datetime import datetime as dt

def quotes():
    l=["“You do not find the happy life. You make it.” – Camilla Eyring Kimball",
"“The most wasted of days is one without laughter.” – E.E. Cummings",
"“Make each day your masterpiece.” – John Wooden",
"“Happiness is not by chance, but by choice.” – Jim Rohn",
"“Impossible is for the unwilling.” – John Keats",
"“No pressure, no diamonds.” – Thomas Carlyle",
"“Believe you can and you’re halfway there.” – Theodore Roosevelt",
"“Stay foolish to stay sane.” – Maxime Lagacé",
"“Dream big and dare to fail.” – Norman Vaughan",
"“You are enough just as you are.” – Meghan Markle",
"“Every moment is a fresh beginning.” – T.S. Eliot ",
"“No guts, no story.” – Chris Brady",
"“Leave no stone unturned.” – Euripides",
"“The journey of a thousand miles begins with a single step.” – Lao Tzu",
"“Simplicity is the ultimate sophistication.” – Leonardo da Vinci",
"“No one has ever become poor by giving.” – Anne Frank",
"“Try Again. Fail again. Fail better.” – Samuel Becket",
"“Good things happen to those who hustle.” – Anaïs Nin"]
    q=r.choice(l)
    return q

def facts():
    l=["Avocados are a fruit, not a vegetable",
       "Avocados are a fruit, not a vegetable",
       "Human teeth are the only part of the body that cannot heal themselves.",
       "The heart of a shrimp is located in its head.",
       "People are more creative in the shower",
       "The unicorn is the national animal of Scotland.",
       "Venus is the only planet to spin clockwise.",
       "The actors who voiced Mickey and Minnie mouse got married in real life.",
       "The moon has moonquakes. ",
       "An ostrich's eye is bigger than its brain.",
       "You can't hum if you hold your nose.",
       "Your fingernails grow faster when you are cold.",
       "All babies are born with blue eyes.",
       "20% of all the oxygen you breathe is used by your brain.",
       "Your small intestine is the largest internal organ in your body",
       "Some fish cough.  Really.",
       "Cats are not able to taste anything that is sweet."]
    q=r.choice(l)
    return q

def motivation():
    l=["“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein",
       "“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi",
       "“When you change your thoughts, remember to also change your world.”—Norman Vincent Peale",
       "Success is not final; failure is not fatal: It is the courage to continue that counts. — Winston S. Churchill",
       "The road to success and the road to failure are almost exactly the same. — Colin R. Davis",
       "Develop success from failures. Discouragement and failure are two of the surest stepping stones to success. —Dale Carnegie",
       "“I never dreamed about success. I worked for it.” —Estée Lauder",
       "“To know how much there is to know is the beginning of learning to live.” —Dorothy West",
       "“Don’t let yesterday take up too much of today.” — Will Rogers",
       "“Opportunity is missed by most people because it is dressed in overalls and looks like work.” — Thomas Edison",
       "“Setting goals is the first step in turning the invisible into the visible.” — Tony Robbins",
       "“He who conquers himself is the mightiest warrior.” — Confucius",
       "“A man who has committed a mistake and doesn’t correct it is committing another mistake.” – Confucius Kongzi"]
    q=r.choice(l)
    return q

def time():
    q=t.localtime()
    now=t.strftime("%H:%M:%S",q)
    return now

def datetime():
    now=dt.now() 
    q=now.strftime("%d/%m/%Y %H:%M:%S")
    return q
