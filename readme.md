# Python Pinball Game
Two year old (as of February 2024) pinball game written in Python

## Tools Used

| Tool    |  Version |
|:--------|---------:|
| Python  |   3.13.1 |
| PyCharm | 2024.3.1 |
| VSCode  |   1.96.2 |
| Pygame  |    2.6.1 |
| Pymunk  |   6.10.0 |

## Change History

| Date       | Description          |
|:-----------|:---------------------|
| 2024-02-08 | Initial creation     |
| 2025-01-10 | Refactor class names |


## References
* [Original GitHub Repo](https://github.com/Dungjax/Pinball)
* [YouTube Video](https://www.youtube.com/watch?v=hp8VBkwkNOw)
* [PyGame: A Primer on Game Programming in Python](https://realpython.com/pygame-a-primer/)
* [Python Pinball Game Project with Source Code](https://data-flair.training/blogs/python-pinball-game-code/)
* 
## Major Design Issues To Be Resolved (February 2024)
* With the introduction of PyAutoGui and settings.py, there is a need to comb through
all of the code to find where hard-coded x,y values are used and make them
dynamically adjust based on the screen_width and screen_height values that
are calculated during game start up and stored in settings.py.