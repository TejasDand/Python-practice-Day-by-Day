import random

def play_game(range_max):

    number_guess = random.randint(1, range_max) # Generates a random number

    players = ["Player 1", "Player 2"]
    winner = None

    # If player not win
    while not winner: 
        for player in players:
            print(f"\n🎮 {player}'s turn (3 attempts)")
            attempts = 3

            while attempts > 0:
                
                guess = int(input(f"{player}, guess a number between 1 and {range_max} ({attempts} attempts left): "))

                if guess == number_guess:
                    print(f"\n🎉 {player} guessed it right! The number was {number_guess}.")
                    winner = player
                    break
                elif guess < number_guess:
                    print("Too Low!")
                else:
                    print("Too High!")

                attempts -= 1

            # If player wins
            if winner:
                break

    print("\n🏁 Game Over.")

# Difficulty Levels
difficulty_levels = {
    "easy": 30,
    "medium": 50,
    "hard": 100
}

difficulty = input("Enter difficulty level - Easy / Medium / Hard: ").lower()

if difficulty in difficulty_levels:
    play_game(difficulty_levels[difficulty])
else:
    print("\nPlease choose a valid difficulty level from Easy / Medium / Hard!\n")
