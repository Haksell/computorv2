from enum import Enum, auto


class Token(Enum):
    EQUALS = auto()


class TokenizeState(Enum):
    NOTHING = auto()
    VARIABLE = auto()


def tokenize(s):
    tokens = []
    state = TokenizeState.NOTHING
    token = []
    for c in " ".join(s.lower().strip().split()):
        match state:
            case TokenizeState.NOTHING:
                pass
            case TokenizeState.VARIABLE:
                pass
    return tokens
