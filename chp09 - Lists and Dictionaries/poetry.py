import random

def makePoem():
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    three_nouns = set()
    while len(three_nouns) < 3:
        three_nouns.add(random.choice(nouns))
    three_verbs = set()
    while len(three_verbs) < 3:
        three_verbs.add(random.choice(verbs))
    three_adjectives = set()
    while len(three_adjectives) < 3:
        three_adjectives.add(random.choice(adjectives))
    two_prepositions = set()
    while len(two_prepositions) < 2:
        two_prepositions.add(random.choice(prepositions))

    noun1 = three_nouns.pop()
    noun2 = three_nouns.pop()
    noun3 = three_nouns.pop()

    adj1 = three_adjectives.pop()
    if adj1[0] in 'aeiouy':
        result = f'An {adj1} {noun1}'
    else:
        result = f'A {adj1} {noun1}'
    result = result + '\n\n' + result + f' {three_verbs.pop()} {two_prepositions.pop()} the {three_adjectives.pop()} {noun2}\n' + \
             f'{random.choice(adverbs)}, the {noun1} {three_verbs.pop()}\n' + \
             f'the {noun2} {three_verbs.pop()} {two_prepositions.pop()} a {three_adjectives.pop()} {noun3}'
    return result

print(makePoem())