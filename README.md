# Pong-Game

This is a classic Pong game implemented using the Turtle graphics library and Pygame for sound effects. The game supports two players, where each player controls a paddle, and the goal is to prevent the ball from passing by your paddle while trying to score against your opponent.

1. Features:
* Two-player Pong game.
* Paddle and ball movement.
* Score tracking.
* Sound effects when the ball hits a paddle or a wall.
* Keyboard controls for moving the paddles and resetting the ball.

2. Prerequisites
* You need to have Python installed on your system. You can download it from here.
* Additionally, the following libraries are required:
  * Turtle (included in Python's standard library)
  * Pygame – for handling sound effects.

* You can install Pygame using the following pip command:
* pip install pygame

3. Game Setup
* Clone the Repository: First, clone this repository to your local machine:

git clone https://github.com/your-repo/pong-game.git

cd pong-game

* Prepare the Sound File: This game uses a sound file (bounce1.mp3) for the bounce effect. Make sure the file is located in the same directory as the Python script.
  * If you don’t have the sound file, either find a bounce1.mp3 sound effect or modify the code to use a different sound.
* Run the Game: To start the game, simply run the Python script using the following command (if in terminal):
python pong_game.py

4. Game Controls
* Player 1 (Left Paddle):
  * Move up: Press W
  * Move down: Press S

* Player 2 (Right Paddle):
  * Move up: Press the Up Arrow
  * Move down: Press the Down Arrow

* Reset the Ball: Press R
* Resume the Ball: Press G

5. **How to Play**
The game follows the classic Pong rules:
* The ball moves across the screen, bouncing off the top and bottom edges.
* Each player controls a paddle and tries to hit the ball to prevent it from passing by.
* If the ball passes the paddle, the opponent scores a point.
* The game continues indefinitely, and you can reset the ball by pressing R.

Known Issues
* Sound File Dependency: Ensure that the bounce1.mp3 file is available in the same directory as the game script to avoid errors when playing sounds.

**Thank you and enjoy the game!**
