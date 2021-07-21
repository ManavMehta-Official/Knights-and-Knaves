## Understanding the riddle of Knights and Knaves!

Knights and Knaves is a type of logic puzzle where some characters can only answer questions truthfully, and others only falsely. The name was coined by Raymond Smullyan in his 1978 work What Is the Name of This Book? <br>

The puzzles are set on a fictional island where all inhabitants are either knights, who always tell the truth, or knaves, who always lie. The puzzles involve a visitor to the island who meets small groups of inhabitants. Usually the aim is for the visitor to deduce the inhabitants' type from their statements, but some puzzles of this type ask for other facts to be deduced. The puzzle may also be to determine a yes-no question which the visitor can ask in order to discover a particular piece of information.


## AI for Knights and Knaves!

AI can be implemented for problem solving tasks such as riddles and puzzles. To train the AI to solve the riddle of **"Knights and Knaves"** was the main objective of this project. In the main directory of this project is a file called `logic.py`. This particular file functions as the Logical Reasoning of the AI. With the help of this particular module, we were able to train our AI to solve such puzzles. <br>

The project directory also has a file called`puzzle.py` which containes the questions to the riddles and the basic rules on how to solve such riddles. Few the basic rules were:
- A knight always says the truth
- A knave always lies
- A person can either be a Knight or a Knave

## In-Depth view on the Project

**The original puzzles for this project that were used to train and test the AI were: <br>**
<br>
<br>

> **Puzzle0**, This puzzle contain of a single character `A`.<br>
> |---------  `A` says **“I am both a knight and a knave.”**
<br>
<br>
> **Puzzle1**, has two characters: A and B. <br>
> |---------  `A` **says “We are both knaves.”** <br>
> |---------  `B` says nothing.
<br>
<br>
> **Puzzle2**, has two characters: A and B. <br>
> |---------  `A` says **“We are the same kind.”** <br>
> |---------  `B` says **“We are of different kinds.”** <br>
<br>
<br>
> **Puzzle3**, has three characters: A, B, and C. <br>
> |---------  `A` says either **“I am a knight.” or “I am a knave.”, but you don’t know which.** <br>
> |---------  `B` says **“`A` said ‘I am a knave.’”** <br>
> |---------  `C` says **“`A` is a knight.”** <br>
<br>
<br>

**NOTE:** All of the puzzles are different i.e. they are not connected to each other in any way. Example: `A` might be a knight in `Puzzle0` but in `Puzzle1` `A` might be a knave.
<br>
<br>


##### Here is the code for the `puzzle.py` module:

```
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
sentence = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(Not(AKnight), AKnave),
    Implication(Not(AKnave), AKnight),
    Biconditional(AKnight, sentence)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
a_sentence = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(Not(AKnight), AKnave),
    Implication(Not(AKnave), AKnight),
    Implication(Not(BKnight), BKnave),
    Implication(Not(BKnave), BKnight),
    Implication(Not(CKnight), CKnave),
    Implication(Not(CKnave), CKnight),
    Biconditional(AKnight, sentence)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
sentence_a = Or(And(AKnave,BKnave), And(AKnight, BKnight))
sentence_b = Or(And(AKnave,BKnight), And(AKnight, BKnave))
knowledge2 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(Not(AKnight), AKnave),
    Implication(Not(AKnave), AKnight),
    Implication(Not(BKnight), BKnave),
    Implication(Not(BKnave), BKnight),
    Implication(Not(CKnight), CKnave),
    Implication(Not(CKnave), CKnight),
    Biconditional(AKnight, sentence_a),
    Biconditional(BKnight, sentence_b)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
sentence_a = Biconditional(Not(AKnight), AKnave)
sentence_b = And(Biconditional(AKnave, BKnight), CKnave)
sentence_c = Biconditional(Not(AKnight), CKnave)
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Implication(Not(AKnight), AKnave),
    Implication(Not(AKnave), AKnight),
    Implication(Not(BKnight), BKnave),
    Implication(Not(BKnave), BKnight),
    Implication(Not(CKnight), CKnave),
    Implication(Not(CKnave), CKnight),
    Biconditional(AKnight, sentence_a),
    Biconditional(BKnight, sentence_b),
    Biconditional(CKnight, sentence_c)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()

```
##### To run the project hover over to puzzle.py and run the program! or you can use terminal or command prompt to run the project. (You would need logic.py to run the project. The link to ddownload is below under the `Project Installation Category`) <br>

#### Running through Terminal

Open the terminal/command prompt on your computer and change the directory to the project directory. <br>
When in the project directory, run the following command:

```
python3 puzzle.py
```

After running the command the AI will share its answers with you in the terminal. The answer would look like the following:
![AI Answers]()


### Project Installation

This project is open to all and is free of cost. All my source code is available in the [Project Repository]().<br> 
You can either download from there or you can [Click here]() to directly download. <br>
<br>
Once you download, unzip the file. You will find a folder named `Knights and Knaves`, that is the project directory. In the project directory you will find 2 files, `logic.py` and `puzzle.py`.

### Understanding the modules and the files

> **logic.py** <br>
<br>
This python file is basically the logic module for our AI. This file is responsible for the Logical Reasoning of the program. **DO NOT CHANGE ANYTHING IN THE FILE!** as this can cause some problems for the AI. `logic.py` contains functions that are used in `puzzle.py`. These functions help the AI to solve and determine who is a knight and who is a knave.
<br>
<br>
> **puzzle.py** <br>
<br>
This file is where all the questions and the rules to solve the puzzles are written. You are free to make changes and cutomize this file. You can make you own riddles and set the rules for the AI to solve it! To understand how to use these functions, you can go through the `logic.py` module.


### Support or Contact

Having trouble with our website or a problem related to the project? Contact me via my [Github Account](https://github.com/ManavMehta-Official) or check the [Github Status](https://www.githubstatus.com/). <br>
<br>

**Contact us here:** <br>
`cs50` official website: [cs50 website](https://cs50.harvard.edu/college/2021/fall/). <br>
`ManavMehta-Official` [Github](https://github.com/ManavMehta-Official) and [Instagram](https://www.instagram.com/manavmehta.official/) account.
<br>
<br>
###### For more details on the project [Click here!](https://github.com/ManavMehta-Official/Knights-and-Knaves)



