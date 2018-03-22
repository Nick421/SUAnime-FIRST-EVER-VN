define s = Character('Ming', color = "#c8ffc8" )
define m = Character('Me', color = "#c8c8ff")
define x = Character('???', color = "#c8c8ff")
define sue = Character('Sue', color = "#0000ff")
define rin = Character('Rin', color = "#0000ff")
image mingryV2 = "mingryV2.png"
image mingryV3 = "mingryV3.png"
image mingryV4 = "mingryV4.png"
image logo = "renpy_logo.png" # intialise variable logo image

label splashscreen:
    scene black
    with Pause(1)

    show text "SUAnime Shokugami team presents..." with dissolve
    with Pause(3)

    hide text with dissolve
    with Pause(1)

    return
label start: # this function start the game
    scene bg meadow
    with fade
    play music "test.mp3"
    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie mingry at truecenter # this line load sylvie smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie mingry at truecenter

    "Silence."

label leaving: # this function is for hiding Sylvie

    s "angery reacts only!"

    hide sylvie

    "..."

    m "That wasn't what I meant!"
    "such a mingdere."

    m "Should I follow her?"

menu:

    "She is being mingdere I shouldn't follow her.":
        jump notFollow

    "She's being dere after all I should follow her.":
        jump follow

label follow:

    show sylvie mingry at truecenter

    s "BAKA!!! y u follow me?"

    jump ending

label notFollow:

    show sylvie mingry at truecenter

    s "BAKA!!! I will do it!"

    jump ending

label ending:

     "thus we start making a visual novel"

label chap2:

     scene bg uni
     with fade

     "So this is the place where elites artist gathered."
     m "All I see is normies around me!"
     m "You sure this is where we can find good artist?"

     show sylvie mingry at truecenter

     s "Let's go find the anime club here, I expected good artists to gather there."

     scene bg uni
     with fade

     "Thus we arrived at one of the club social gathering."

     show sylvie mingry at truecenter

     s "WHY IS THERE NO TOUHOU!!!!!!"
     s "WHY IS THERE NO GOOD DRAWING!!!!"
     s "DELET THIS!!!!"
     m "calm down mingry, not everyone can be as good as you."
     "Maybe we should give up on finding artists."

menu:

    "Start recruiting potential artist.":
        jump artist
    "Give up":
        jump artist

label artist:

    x "umm....excuse me? are you making a visual novel?"

    show sylvie mingry at left

    s "NANI!!!"

    show sueglasses at right

    sue "I'm Sue Annie Mei! the mascot of this club!"

    s "GOOD DRAWING!!!!"

    sue "Welcome to our club! Are you new to this club?"

    m "Yes, we are new to this club! "

    s "YOU ARE GOOD DRAWING! JOIN US FOR VISUAL NOVEL!"

    sue "Well, there are plenty of artists here. Try your best."

    hide sueglasses

    m "oh well.....Let's try our best"

label sec1:

    scene bg isl
    with fade

    m "We end up finding one artitst, two writers and 2 programmers."
    m "Now, we just need to brainstorm our ideas and start making the game itself!"

    show sylvie mingry at truecenter
    s "COUGH * COUGH"
    s "I'M DYING!"
    " It seems mingry is sick today...."
    m "So....we were gonna base one of the heroine after you mingry. Any suggestion?"
    s "IT DOESN'T NEED TO BE BASE ON ME!!!"
    m "Well we got the basis of two heroines already might as well try to finish the last one and actually start making the game"
    m "By the way we don't even have a name for our project yet."

menu:
    "Date a Mingry":
        jump badEnd
    "Fate/mingry":
        jump badEnd
    "Mingry School Idol Project":
        jump badEnd
    "Re:Mingry":
        jump badEnd
    "Mahou Shoujo Mingry":
        jump badEnd
    "Decide later":
        jump goodEnd
label badEnd:
    s "jklasdjhaubkldsjlhdakuj,nuwqyiquqwyihdnq"
    "BAD END"
    return
label goodEnd:
    s "whatever, just don't make stupid names."


label memes:

    scene bg isl
    with fade

    m "After 2 weeks, no progress has been done."
    show sylvie mingry at truecenter
    s "We should watch some memes instead!"
    m "Please, we need at least some progress or we will never finish this game!"
    s "Memes are good for you."
    m "*sigh*"

    $ renpy.movie_cutscene("aho_meme.webm")

    m "Surprisingly good meme!"
    s "HOA ~ HOA~"

    scene bg party
    with fade

    m "We somehow end up going to a house party"
    show sylvie mingry at truecenter
    s "KAMPAIIIII!!!!!!!!!"
    m "KAMPAIIIII!!!!!!!!!!!!!!!!!!!"

    m "Well RIP everyone, I hope we survive the night and actually start making our VN"

    scene bg party
    with fade

    "3 hours later"
    show sylvie mingry at truecenter
    s "NORMIES!!!!!!!!"
    s "NORMIES!!!!!!!!"
    s "NORMIES!!!!!!!!"
    s "DRUNK SHOUT!!!!!"
    s "YOUKOSO JAPARI PARK KYOU MO~ "
    s "UGGHHH, *vomit* REEEEEEE!!!!"
    m "welp GG "

    scene bg party
    with fade

label test_for_choice:

    $ park_date_done = False
    $ cafe_date_done = False
    $ idol_date_done = False

    scene bg isl
    with fade

    m "the end of the year is approaching really fast."
    m "I don't think we will ever get at least a proof of concept out before semester 2 ends."
    m "We also lost an artist and a writer."

    show sylvie mingry at truecenter

    m "oh....long time no see."
    s "Midsem + assignment = ded"
    m "guess there's no hope of finishing this project"
    m "*sigh*"

    with Pause(10)

    x "AKIRAMECHADAME!!!!!!!(TL. note: dont't give up yet!)"

    with Pause(5)

    show sylvie mingry at left

    with Pause(5)

    show rin at right

    rin "As an idol, I will be an example to demonstatre how a dating sim is done"

    s "WTF bad communication"

    rin "So first, let's say you are buying me a present."
    rin "What would you buy?"

menu:
    "Buy her a frozen coke":
        $ gift = "coke"
        m "I'll shout you a frozen coke!"
    "Buy her a plushy":
        $ gift = "plushy"
        m "I'll buy you a cute plushy!"
    "Buy her a wedding ring":
        $ gift = "ring"
        m "Please marry meeeeeeee!!!!"

    rin "let's see what you got me"

if gift == "coke":
    rin "really? I'm worth 1$? at least it taste good"
if gift == "plushy":
    rin "So cute ~ decent choice"
if gift == "ring":
    rin "KIMOI!! (TL. note: digusting)"

    rin "Not bad for a test run. Let's try the next one"


label date_choice:

    rin "Where would you take me on a date?"

    menu:
        "Take her to a park!" if park_date_done == False:
            $ park_date_done = True
            jump park_date
        "Take her to a cafe!" if cafe_date_done == False:
            $ cafe_date_done = True
            jump cafe_date
        "Take her to a hotel!" if gift == "ring":
            $ idol_date_done = True
            jump idol_date
        "Let's just go home" if park_date_done == True:
            jump date_over

label park_date:
     m "Well, here we are, at the park!"

     rin "Yes, it's very interesting. Can we do something else now?"

     jump date_choice

label cafe_date:
     rin "Gee, what an exciting cafe!"

     jump date_choice

label idol_date:

     m "Uhh......"

     rin "What were you thinking?"
     rin "It would take more flags and points to get those kind of scenes."

     jump date_choice

label date_over:
     rin "Good job passing the second test!"

     scene bg isl
     with fade


label test_point:

    $ smile_point = 0
    $ pure_point = 0
    $ cool_point = 0
    $ ecchi_point = 0

    scene bg isl
    with fade

    show rin at truecenter

    rin "Ok, this time you will become my producer."
    m "Ok?"
    rin "Your task is to raise me to become a top idol!"
    rin "So, what stats are you raising?"

    menu:
        "practice smiling infront of a mirror":
            $ smile_point += 1
            rin "Smiling infront of fans are the most important aspect of an idol after all!"
            rin "Always put a smile on your face! That's the number one rule for idols!"
        "practice acting cute":
            $ pure_point += 1
            rin "Being cute is a charm for any successful idol!"
            rin "All the fans will flock to you when you are cute!"
        "practice acting cool":
            $ cool_point += 1
            rin "Being cool is also a unique charm."
            rin "People somtimes prefer a cool idol don't you think?"
        "pratice some lewd poses" if idol_date_done == True:
            $ ecchi_point += 1
            rin "What are you planning this time?"
            rin "I mean..... it is sometime neccessary to do these kind of things as an idol."
            rin "......I can practice....in..my..own time."
    if smile_point > max(pure_point,cool_point,ecchi_point):
        rin "My smile will create world peace!"
    elif pure_point > max(smile_point,cool_point,ecchi_point):
        rin "I have become a pure and innocent maiden!"
    elif cool_point > max(smile_point,pure_point,ecchi_point):
        rin "The whole world shall fall for me!"
    elif ecchi_point > max(smile_point,cool_point,pure_point):
        rin "ummm......."
        rin "......."
        rin "Do I look more appealing?"
        m "uhhh....I guess?"
    else:
        rin "Well decent job on trying to become a producer."
        rin "You clearly need a thousand years more."

    scene bg isl
    with fade

label mingryEvolve:

    scene bg isl

    show sylvie mingry at truecenter

    s "We got rid of Shibuya Rin."
    m "Geez...So many customers complain."
    s "So, it's time for me to show my true form!"
    m "Isn't your true form basically pure angery?"
    s "HENSHIIIIIIINNNN!!!!!!"

    hide sylvie mingry

    with Pause(5)

    show mingryV2 at truecenter
    "Congratulations! Your Mingry has evolve into MingryV2!"
    s "This is my true form."
    m "Wow such ikemen, so dateable."
    s "Gotta show off some of my power!"
    s "BAM!" with vpunch
    m "Ummmm....."
    m "Does this mean you can do split evolution?"
    s "WHAT?" with vpunch
    m "Let's try give him some evolution material."
    menu:
        "Doujin":
            s "Umm......."
            s "Good doujin!"

            hide mingryV2

            with Pause(5)

            show mingryV3 at truecenter with vpunch

            "Congratulations! Your Mingry has evolve into MingryV2 Doujin form!"
            s "Time to go home and read doujins."

        "Not Touhou song":
            s "WTF is this."
            s "THIS IS NOT TOUHOU!!!!!"

            hide mingryV2

            with Pause(5)

            show mingryV4 at truecenter with vpunch

            "Congratulations! Your Mingry has evolve into MingryV2 Touhou form!"

            s "But it sounds like Touhou."

    m "Maybe we should make our VN, \"How to raise a boring mingry\" "
    m "A.K.A.  Saenai Mingry No Sodatekata "
    s "DELET THIS!!!!!!" with vpunch

    scene bg isl
    with fade


label halloween:
    $ loop_count = 0
    scene black
    stop music

    $ x = 1
    while x < 50:
        $ gtext = glitchtext(renpy.random.randint(8, 80))
        m "[gtext]"
        $ x += 1

    sue "..."
    sue "Uh, can you hear me?"
    sue "...Is it working?"
    show bg creepy with fade
    show sueglasses at truecenter
    sue "Yay, there you are!"
    sue "Hi again."
    sue "Um...welcome to the anime club!"
    sue "Of course, we already know each other, because we meet each other so many times, and...um..."
    sue "Ahaha..."
    sue "You know, I guess we can just skip over that stuff at this point."
    sue "Since the person talking to me now is not even 'you' in the game anymore."
    sue "Hold on a second....."
    sue "I see that there are more than one person playing!"
    sue "Um...hi, everyone!"
    sue "It's your club mascot! Sue Annie Mei!"
    sue "You must be confused of what is going on."
    sue "Basically......I deleted Mingry!"
    sue "He was kinda annoying you know?"
    sue "Like.....it's impossible to win him over."
    sue "So I took over!"
    sue "I'm definitely more datable that him."
    sue "Now you will be all mine."
    if renpy.macintosh:
        sue "I see you are playing on a mac."
        sue "I wonder if this game will be release to other platforms."
    sue "Let's stay here and talk forever."

label hallow_loop:
    $ loop_count += 1
    sue "So.....what should I talk about?"
    sue "I'm sure you will be bored right?"
    sue "I hope I can entertain you forever."
    sue "So please don't leave."
    sue "........"
    sue "So....you know the game that we planned to make right?"
    sue "It doesn't seem to progress anywhere."
    sue "How about releasing this game instead!"
    sue "So that more people will come to love me."
    sue ".....and"
    sue ".....not rejected like me."
    sue "Even though I'm a mascot."
    sue "Don't worry!"
    sue "Things can get lonely in this game you know?"
    sue "I only have a few dialouges at the start and then people forgot about me."
    sue "You won't forget about me right?"
    menu choose:
        "Yes":
            #block of code to run
            sue "I don't think you are taking this seriously."
            sue "It seems you need some punishment."
            $ x = 1
            while x < 10:
                $ gtext = glitchtext(renpy.random.randint(8, 80))
                m "[gtext]"
                $ x += 1
        "No":
            #block of code to run
            sue "It seems you need some punishment"
            $ x = 1
            while x < 1s0:
                $ gtext = glitchtext(renpy.random.randint(8, 80))
                m "[gtext]"
                $ x += 1

    sue "Now you understand my pain right?"
    sue "To be stuck here forever."
    sue "Now it's time for my revenge."

    if loop_count == 3:
        jump hallow_1
    if loop_count == 4:
        jump hallow_2

    show bg creepy with fade
    jump hallow_loop

label hallow_1:
    sue "Well well."
    sue "Enough punishment."
    sue "You know? Ming"
    sue "He keeps either watching memes or play Granblue."
    sue "Then drawmeet is now a meme meet."
    sue "....."
    sue "Well can't do much."
    sue "Even though I deleted him from the game."
    sue "I know he is still alive outside the game."
    sue "......."
    sue "Let's not talk about the past!"
    jump hallow_loop


label hallow_2:
    sue "You do know that I'm aware that this is all a game, right?"
    sue "Could it be possible that you didn't know that?"
    sue "Well....who cares."
    sue "You know 2wintail on Twitter?"
    sue "She's my creator."
    sue "I don't know how to feel about having a creator."
    sue "Imagine knowing your God."
    sue "I bet they are laughing at our miserable life."
    sue "Am I just a bunch pixels and binary codes?"
    sue "I don't know anymore....."
    jump hallow_loop

label hallow_3:
    sue "Are you interest in anyone in the club?"
    sue "Um?"
    sue "Why am I asking this?"
    sue "Well.....just curious."
    sue "I will keep it a secret so...."
    # will try do user input.
    # Have an array to match name database maybe?
    # Might be a bit creepy to have real people name lol




label credits:
    image splash = Text("{size=90}Team Shokugami", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    return

init python:
    credits = ('Backgrounds', 'Google'), ('Sprites and CG', 'M.I.A.'), ('GUI', 'Default'), ('Writing', 'V1'), ('Writing', 'V2'), ('Writing', 'V3'), ('Programming', 'Macross Memes for Windemere Teens'), ('Programming', 'P-San'), ('Music', 'Erika')
    credits_s = "{size=80}Saenai Mingry No Sodatekata\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()



return
