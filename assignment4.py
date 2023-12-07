import random

def guess_animal():
    animals = ["monkey", "buffalo", "whale", "aardvark", "lion", "elephant", "giraffe", "horse", "dog", "kitten"]
    random_animal = random.choice(animals)
    guessed_animal = ""

    while guessed_animal != random_animal:
        guessed_animal = input(f'what is the animal: ').lower()

        if guessed_animal not in animals:
            print('oops, invalid animal. Try again with a different animal.')
        elif len(guessed_animal) < len(random_animal):
            print('oops, take a second guess. The animals name is longer.')
        elif len(guessed_animal) > len(random_animal):
            print('oops, take a second guess. The animals ame is shorter.')

    print(f'Congratulations! You guessed the right animal: {random_animal}')


guess_animal()

