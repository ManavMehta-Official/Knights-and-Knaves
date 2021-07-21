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

##### Here is the code for the `logic.py` module:

```markdown
import itertools


class Sentence():

    def evaluate(self, model):
        """Evaluates the logical sentence."""
        raise Exception("nothing to evaluate")

    def formula(self):
        """Returns string formula representing logical sentence."""
        return ""

    def symbols(self):
        """Returns a set of all symbols in the logical sentence."""
        return set()

    @classmethod
    def validate(cls, sentence):
        if not isinstance(sentence, Sentence):
            raise TypeError("must be a logical sentence")

    @classmethod
    def parenthesize(cls, s):
        """Parenthesizes an expression if not already parenthesized."""
        def balanced(s):
            """Checks if a string has balanced parentheses."""
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
        if not len(s) or s.isalpha() or (
            s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])
        ):
            return s
        else:
            return f"({s})"


class Symbol(Sentence):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise Exception(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(
            ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
        )

    def __repr__(self):
        conjunctions = ", ".join(
            [str(conjunct) for conjunct in self.conjuncts]
        )
        return f"And({conjunctions})"

    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([Sentence.parenthesize(conjunct.formula())
                           for conjunct in self.conjuncts])

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or(Sentence):
    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(
            ("or", tuple(hash(disjunct) for disjunct in self.disjuncts))
        )

    def __repr__(self):
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjuncts})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨  ".join([Sentence.parenthesize(disjunct.formula())
                            for disjunct in self.disjuncts])

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])


class Implication(Sentence):
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (isinstance(other, Implication)
                and self.antecedent == other.antecedent
                and self.consequent == other.consequent)

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"

    def evaluate(self, model):
        return ((not self.antecedent.evaluate(model))
                or self.consequent.evaluate(model))

    def formula(self):
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} => {consequent}"

    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())


class Biconditional(Sentence):
    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, Biconditional)
                and self.left == other.left
                and self.right == other.right)

    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"

    def evaluate(self, model):
        return ((self.left.evaluate(model)
                 and self.right.evaluate(model))
                or (not self.left.evaluate(model)
                    and not self.right.evaluate(model)))

    def formula(self):
        left = Sentence.parenthesize(str(self.left))
        right = Sentence.parenthesize(str(self.right))
        return f"{left} <=> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


def model_check(knowledge, query):
    """Checks if knowledge base entails query."""

    def check_all(knowledge, query, symbols, model):
        """Checks if knowledge base entails query, given a particular model."""

        # If model has an assignment for each symbol
        if not symbols:

            # If knowledge base is true in model, then query must also be true
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:

            # Choose one of the remaining unused symbols
            remaining = symbols.copy()
            p = remaining.pop()

            # Create a model where the symbol is true
            model_true = model.copy()
            model_true[p] = True

            # Create a model where the symbol is false
            model_false = model.copy()
            model_false[p] = False

            # Ensure entailment holds in both models
            return (check_all(knowledge, query, remaining, model_true) and
                    check_all(knowledge, query, remaining, model_false))

    # Get all symbols in both knowledge and query
    symbols = set.union(knowledge.symbols(), query.symbols())

    # Check that knowledge entails query
    return check_all(knowledge, query, symbols, dict())

```

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



