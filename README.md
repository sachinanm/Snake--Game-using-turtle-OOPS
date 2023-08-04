# Snake Game 🐍

The Snake Game is a classic arcade game in which the player controls a snake that moves around the screen, eating food to grow longer. The objective is to avoid running into the walls or the snake's own body while trying to eat as much food as possible. As the snake eats, it becomes longer, making the game more challenging.

## How to Play 🎮

1. **Controls:** Use the arrow keys (Up, Down, Left, Right) to control the direction of the snake.
2. **Objective:** Guide the snake to eat the food (displayed as fruits) to grow longer.
3. **Avoid Collisions:** Be careful not to run into the walls or the snake's own body, as this will end the game.

## Project Features 🚀

- Simple and intuitive controls using arrow keys.
- Randomly generated food (fruits) for the snake to eat.
- Snake grows longer as it eats food, increasing the challenge.
- Game over if the snake hits the walls or its own body.
- Display of the player's score (number of fruits eaten).

## How It Works 🔄

The Snake Game is built using the Turtle graphics library in Python, which allows us to create graphical elements on the screen. The game is designed using **classes and objects**, making it easier to manage and organize the various components of the game.

The snake itself is represented as a series of square segments. Each segment is an object of the Turtle class, and these segments are stored in a list. The snake's movement is achieved by updating the position of each segment based on the direction provided by the player.

List slicing is used to manage the snake's body. As the snake moves, its tail is constantly growing. When the snake eats food, a new segment is added to the list, effectively increasing the length of the snake.

Inheritance is utilized to create the food objects (fruits) in the game. The food **inherits properties and methods** from the Turtle class, which makes it easier to create and manage multiple instances of food.

## Installation 🛠️

To play the Snake Game, you need to have Python installed on your computer. You can run the game by executing the Python script provided.

1. Clone the repository or download the Python script.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the directory containing the Python script.
4. Run the script using the command: `python snake_game.py`

## Future Enhancements 🔮

The Snake Game can be further improved by adding the following features:

- High score tracking to challenge players to beat their best score. (Updated)
- Levels with increasing difficulty as the snake grows longer. (Updated)


## Have Fun! 🎉

Enjoy playing the Snake Game and challenge your friends to beat your high score. Feel free to modify and customize the game to add your own unique features and ideas. Happy coding! 🚀
