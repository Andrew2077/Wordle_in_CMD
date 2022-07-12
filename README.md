
## **Wordle game in CMD**
**Wordle** is a famous word-guessing game. And for whom doesn't know the game, here's a simple **[tutorial](https://archive.ics.uci.edu/ml/datasets/PAMAP2+Physical+Activity+Monitoring)** for the game.

You can try [**Wordle**](https://wordlegame.org) yourself before hitting my project.


___
## **Table Of Contents**
- [**Wordle game in CMD**](#wordle-game-in-cmd)
- [**Table Of Contents**](#table-of-contents)
- [**The Idea of the project**](#the-idea-of-the-project)
- [**How to play**](#how-to-play)
- [**Project Guideline**](#project-guideline)
- [**Cheat**](#cheat)
- [**Planned improvements**](#planned-improvements)

___
## **The Idea of the project**
copy and modify the known game worlde.
It's almost the same game but with fewer words to predict and less fancy animation. because I'm not using CSS or Qt yet.

There are 2400+ words to guess from where you find them in **[valid_words_5](valid_words_5.py)** You can add your own words and try guessing them.
___


## **How to play**
- All wordle games are the same, just guess words known to the game.
  
- Your goal is to guess a word of **5 letters** in **6 attempts** at most. If you can't guess the word in 6 attempts, then you lose.

- After winning or losing, the game will shut itself down in **10 seconds**, and you can start a new game by reopening **Wordle.exe** again.
   
- Here, give [my wordle](Wordle.exe) a try.

- Here's an example of winning the game. 
  
![guide lines](winning.gif)

-Here's an example of me losing the game. 

![guide lines](losing.gif)



___
## **Project Guideline**  

  1. Create a file **[[valid_words_5.py]](valid_words_5.py)** to be your data set of words to guess.
  2. Creating a file **[[wordle_game.py]](wordle_game.py)** to be your game.
  3. Creating a file **[[main.py]](main.py)** your game initialization in cmd.
  4. **[[Wordle.py]](wordle.py)** is a file modified to contain all the files above so that the game can be in 1 file project. 
  5. Converting worlde.py to worlde.exe to run the game in cmd.


---
## **Cheat**
Once you open the game **[Cheat](cheat.txt)** is created where it stores the random word that you are trying to guess, so you can use it to cheat. And finish the game quickly.

It's very helpful for debugging. Or you can edit this snippet to your own words.

```python
# * choose a random word from the list of valid words
CHOOSEN_WORD = random.choice(valid_words)
# or this for easier debugging
CHOOSEN_WORD = "trunk"
```
---
## **Planned improvements**

- Adding more words
- Guessing different lenghtes words
- Website
- QT GUI
- AI model to solve the game

---








