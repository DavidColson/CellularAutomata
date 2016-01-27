A Elementary Cellular Automata Simulator made in Python and PyGame
------------------------------------------------------------------

**What is it?**

This is a simple little python program demonstrating an elementary cellular automata functioning. Essentially a cellular automaton is a grid of cells that can have certain states. As each timestep progresses a new state is calculated based on the cells current state, and the state of it's neighbours. 

My little implementation uses PyGame to draw the state of the cells, and basic python to calculate each time generation, represented on the y-axis of the output image.

**What happens if I run it?**

A new ruleset will be picked randomly and it will draw out all the generations filling the screen. Occasionally amazing things will happen like this:

![Automata sample 1](/images/Automata1.png)
![Automata sample 2](/images/Automata2.png)
![Automata sample 3](/images/Automata3.png)

**How do I test the code?**

You need to have PyGame installed with python, otherwise the code should just run without any issue. A window will popup and show you the output. In the first few lines of the code you can set some settings such as the rule code and cell size and such. Also experiment with different initial conditions for the cells. You can do this on lines 24-25.

**How it works**

The rules function (found on line 28) does most of the hard work in the simulation. It combines the cell state with it's two neighbours into a 3 bit binary number such as 110. That is the cells state is on and one of it's neighbours is also on. This is converted into an integer so it can be used as an index from 0 to 7.

The rulecode is then converted into a list of 8 binary bits. We use the 3 bit number as an index to access an element from this array. The result is the state of the new cell. It looks something like this:

3 bit                   New Cell
neighbourhood           State
000             --->    0
001             --->    1
010             --->    0
011             --->    1
100             --->    1
101             --->    0
110             --->    1
111             --->    0

In the above example the rulecode is 90, which in binary is 01011010, as is seen above in the states of the new cells.

This process is done for each cell in a row and the new row of cells is displayed below, and the process repeats.


