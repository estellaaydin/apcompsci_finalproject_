import turtle
import random
t = turtle.Turtle()
t.speed(0)

word_list = ['hi','by','an','la','so','bye','caw','run','moo','low','rex','try','moon','bray','gate','sock','sole','code','dino','mouse','teach','learn','grass','python','turtle','abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker','jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak','kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury','lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw','psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied','subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy','unzip','uptown','vaporize','vixen','vodka','voodoo','vortex', 'walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern','xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie' 'pooey']



def draw_gallows():
  #draw the gallows for the hangman
  #draw stright line going up
  t.color('brown')
  t.width(5)

  #down to the right
  #draw line going right
  t.fd(50)
  t.pu()
  t.goto(25,0)
  t.pd()
  t.lt(90)
  t.fd(150)
  t.lt(90)
  t.fd(50)
  t.lt(90)
  t.fd(25)

  t.stamp()
def draw_head():
  #draw the head for the hangman
  t.pencolor('black')
  t.width(1)
  #t.lt(90)
  t.pu()
  t.goto(-40,110)
  t.pd()
  
  # t.fd(15)
  t.rt(90)
  t.circle(15)
  #t.stamp()

def draw_back():
  #draw the back for the hangman

  #move to bottom of head
  #t.circle(15,180)
  #t.lt(90)
  t.pu()
  t.goto(-24,95)
  #t.stamp()
  t.pd()
  #t.rt(90)
  t.fd(50)


def draw_arm1():
  #draw the arm for the hangman
  t.pu()
  t.goto(-22,75)
  t.pd()
  #t.bk(40)
  #t.stamp()
  t.lt(95)
  t.fd(30)


def draw_arm2():
  #draw the second arm for the hangman
  t.bk(25)
  # t.pu()
  # t.goto(-22,75)
  
  # t.pd()
  
  t.rt(200)
  t.fd(30)


def draw_leg1():
  #draw the leg for the hangman
  #get to the bottom of the back
  #draw a slanted line
  t.pu()
  t.goto(-22,50)
  t.pd()
  
  t.lt(30)
  t.fd(40)
  # t.rt(45)
  # t.fd(40)

def draw_leg2():
  #draw the second leg for the hangman
  t.bk(40)
  t.lt(90)
  t.fd(40)

def setup():
  #setup
  lives = 6
  draw_gallows()
  #choose random word
  randIndex = random.randint(0, len(word_list))
  word = word_list[randIndex]
  #choose a random number to use as the index for the word list

  # use that index number to choose the word


  print("Welcome to Hangman!")
  print("Your secret word is "+ str(len(word))+" letters long")


 #where the letters go
  
  t.width(1)
  t.color('orange')
  t.pu()
  t.goto(-30,-50)
  t.lt(90)

  for i in range(len(word)):
    t.pd()
  
    t.fd(20) 
    
    t.pu()
    t.fd(5) 

  t.goto(0,0)
  t.pd()

  return lives, word
  

def game_over(guesses, letters, lives):
  #no lives left
  if lives <= 0:
    return True
  #word guessed correctly
  if letters <= guesses:
    return True
  
  
  return False

def draw(lives):
  
  t.pu()
  t.goto(-52,165)
  t.pd()
  if lives == 5:
    draw_head()
  elif lives == 4:
    draw_back()
  elif lives == 3:
    draw_arm1()
  elif lives == 2:
    draw_arm2()
  elif lives == 1:
    draw_leg1()
  elif lives == 0:
    draw_leg2()

def play_game():
  lives, word = setup()
  guesses = set()
  letters = set(word)

  while not game_over(guesses, letters, lives):
    guess = input("Guess a letter ")
    if guess in guesses:
      print("you already guessed that one!")
    else:
      if guess in word:
        guesses.add(guess)
        #draw letter
        for count,v in enumerate(list(word)):
         
          if v == guess:
            # go to the right line and write the letter
            t.pu()
            #t.goto(-30,-80)
            
            t.goto(-25+(count*25), -55)
            t.pd()
            style = ("Courier", 16, 'bold', 'italic')
            t.write(v, font = style)
            
        t.pu()
        t.home()
        t.stamp()
        t.pd()
        print("good job!")
      else:
        guesses.add(guess)
        
        lives = lives - 1
        
        draw(lives)

  print("Game over")
  print("Your word was " + word)


play_game()


# draw_gallows()
# draw_head()
# draw_back()
# draw_arm1()
# draw_arm2()
# draw_leg1()
# draw_leg2()
