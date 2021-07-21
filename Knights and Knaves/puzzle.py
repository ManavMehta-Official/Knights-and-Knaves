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
