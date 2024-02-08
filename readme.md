# Python Pinball Game
Two year old (as of February 2024) pinball game written in Python
## References
* [Original GitHub Repo](https://github.com/Dungjax/Pinball)
* [YouTube Video](https://www.youtube.com/watch?v=hp8VBkwkNOw)
* [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
## Major Design Issues To Be Resolved (February 2024)
* With the introduction of PyAutoGui and settings.py, there is a need to comb through
all of the code to find where hard-coded x,y values are used and make them
dynamically adjust based on the screen_width and screen_height values that
are calculated during game start up and stored in settings.py.