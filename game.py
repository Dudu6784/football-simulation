import random
import time
import turtle
from collections import Counter

screen = turtle.Screen()

# Set the window to full screen
screen.setup(width=screen.window_width(), height=screen.window_height())
screen.screensize(1920, 1080)

# Enable full screen mode
screen._root.attributes("-fullscreen", True)

weights1 = [0.01, 0.09, 0.90]
weights2 = [0.01, 0.09, 0.90]
scorers = []
Goals1 = []
Goals2 = []
goals = []
teams = []
turtle.bgcolor('black')
team1players = ['br', 'cb', 'n']
team2players = ['br', 'cb', 'n']

def calculate_strength(rank, exponent=5):
    if not (1 <= rank <= 100):
        raise ValueError("Ranking must be in the range 1–100")
    return (101 - rank) ** exponent

def simulate_match_with_events(team1, team2, rank1, rank2, chance_of_goal1, chance_of_goal2):
    strength1 = calculate_strength(rank1)
    strength2 = calculate_strength(rank2)

    total_strength = strength1 + strength2
    prob1 = strength1 / total_strength
    prob2 = strength2 / total_strength

    goals1 = 0
    goals2 = 0

    print(f"--- Match: {team1} vs {team2} ---")
    t = turtle.Turtle()
    t3 = turtle.Turtle()
    t3.color('white')
    t.color('white')
    t2 = turtle.Turtle()
    t2.color('white')
    t.hideturtle()
    t.penup()
    t.goto(-150, 200)
    t3.hideturtle()
    t3.penup()
    t3.goto(-200, 200)
    t2.hideturtle()
    t2.penup()

    y = 150  # starting position for goal display

    t.write(f'{team1} {goals1} : {goals2} {team2}', font=("Arial", 24, 'bold'))
    time.sleep(10)  # short pause before start

    for minute in range(1, 91):

        time.sleep(1)
        t3.clear()
        event = random.random()
        t3.write(minute, font=('Arial', 40, 'bold'))
        if event < prob1 * chance_of_goal1:
            goals1 += 1
            t.clear()
            t.write(f'{team1} {goals1} : {goals2} {team2}', font=("Arial", 24, 'bold'))
            goals.append(minute)
            teams.append(team1)
            player = random.choices(team1players, weights=weights1, k=1)[0]
            scorers.append(player)
            t2.penup()
            t2.goto(-150, y)
            t2.write(f'{minute} min – Goal for {team1}! Scored by {player}', font=('Arial', 10, 'bold'))
            y -= 25

            print(f"{minute}' - GOAL! {team1} scores! (Score: {goals1}:{goals2})")

        elif event < (prob1 + prob2) * chance_of_goal2:
            goals2 += 1
            t.clear()
            t.write(f'{team1} {goals1} : {goals2} {team2}', font=("Arial", 24, 'bold'))
            goals.append(minute)
            teams.append(team2)
            player2 = random.choices(team2players, weights=weights2, k=1)[0]
            scorers.append(player2)
            t2.penup()
            t2.goto(-150, y)
            t2.write(f'{minute} min – Goal for {team2}! Scored by {player2}', font=('Arial', 10, 'bold'))
            y -= 25

            print(f"{minute}' - GOAL! {team2} scores! (Score: {goals1}:{goals2})")
        else:
            print(f"{minute}' - No events.")

    print("\n--- END OF REGULAR TIME ---")
    print(f"Final Score: {team1} {goals1} : {goals2} {team2}")
    Goals1.append(goals1)
    Goals2.append(goals2)
    top_scorer_counter = Counter(scorers)
    top_scorer, count = top_scorer_counter.most_common(1)[0]
    t2.goto(-150, y - 25)
    t2.write(f'Top scorer: {top_scorer} with {count} goals!', font=('Arial', 10, 'bold'))
    time.sleep(10)
    scorers.clear()
    t.clear()
    t2.clear()
    if goals1 > goals2:
        print(f"Winner: {team1}")
    elif goals2 > goals1:
        print(f"Winner: {team2}")
    else:
        print("Draw")

# Example usage
team1 = input("Enter the name of the first team: ")
team2 = input("Enter the name of the second team: ")
rank1 = int(input('Enter the ranking of the first team (1-100): '))
rank2 = int(input('Enter the ranking of the second team (1-100): '))
chance_of_goal1 = float(input('Enter the goal chance for the first team (e.g., 0.03): '))
chance_of_goal2 = float(input('Enter the goal chance for the second team (e.g., 0.03): '))

simulate_match_with_events(team1, team2, rank1, rank2, chance_of_goal1, chance_of_goal2)
screen.onkey(simulate_match_with_events(team1, team2, rank1, rank2, chance_of_goal1, chance_of_goal2), 'space')
screen.listen()
turtle.exitonclick()
