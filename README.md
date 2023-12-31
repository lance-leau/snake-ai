# Snake Game AI using Hamiltonian Cylces
![Snake Game AI](https://imgur.com/Vddzpr9.png)


- [Presentation](#presentation)
- [Hamiltonian Cycles and Shortcuts](#hamiltonian-cycles-and-shortcuts)
- [Shortcuts Implementation](#shortcuts-implementation)
- [How to Run the Code](#how-to-run-the-code)

### Presentation
This project presents a classic Snake game integrated with an AI system. The game employs a Hamiltonian cycle algorithm, accompanied by optimization techniques that introduce shortcuts for efficient gameplay. The implementation offers an engaging and challenging experience for players.
It seemed fitting to make this snake AI algorithm in python.

### Hamiltonian Cycles and Shortcuts
In graph theory, a Hamiltonian path or cycle is a traversal of a graph that visits each vertex exactly once. The Snake game's AI employs the Hamiltonian cycle concept to navigate the game board effectively, ensuring that no cell is revisited during gameplay. Furthermore, the AI algorithm utilizes shortcuts to optimize the Snake's movement.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/60/Hamiltonian_path.svg" alt="Example of a 20 vertices graph with a Hamiltonian cycle shown in red." width="300" height="300">
  <br>
  <i>Example of a 20 vertices graph with a Hamiltonian cycle shown in red.</i>
</p>

### Shortcuts Implementation
The AI system optimizes the Snake's movement by considering the following steps:


* Calculating the position of the target (apple) in the cycle.
* Calculating the position of the current position (snake's head) in the cycle.
* For each of the possible directions, if the difference between the head of the target is smaller then the size of the snake, add the direction to a list
* Return the direction of the list corresponding to the cell the bigger value on the cycle

### How to run the code
Navigate to the ```snake-ai``` folder and open a terminal to run the command ```py main.py```
Follow the instructions in the terminal to choose between playing and letting the AI play.

***note: I am aware that this algorithm is sub-optimal, but I made it myself and [I am proud of it](https://imgflip.com/i/854knr)***
