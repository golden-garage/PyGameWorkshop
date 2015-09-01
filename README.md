# PyGameWorkhop

This repo contains lessons used in a PyGame after school program.

## Activities

*Lessons* are group into *Activities*.

Each *Activity* has a planned duration of 90 mins.

Most *Activities* are either complete games or complete game levels.

The *Activities* are ordered.

Each new *Activity* builds on the knowledge and reuses the code from older *Activities*.

### Wormy

In this *Activity*,  students build the classic arcade game, Snake (also known as Nibbles).

> The code used in this lesson was inspired by [Wormy (a Nibbles clone)](http://inventwithpython.com/pygame) from
> [Al Sweigart](http://inventwithpython.com):

When this *Lesson* is complete, the student will have developed a complete game.

#### Lesson 1 - hello wormy

* game initialization

    - specific to Raspberry Pi's in text mode

    - optimized for a 1280x1024 display (classroom default)

* basic game loop

```python
while true:
    display();
```
          
* display text


#### Lesson 2 - goodbye wormy

* basic event handling

```python
while GAME_IS_RUNNING:
    handle_events();
    display_game();
```

* key press to end game

#### Lesson 3 - spinning hello

* updating game objects

```python
while GAME_IS_RUNNING:
    handle_events();
    update_game_objects();
    display_game();
```

* text rotates with each game loop

* framerate (speed up, slowdown)

#### Lesson 4 - game scens

* each game scene has its own game loop

* switch scenes

* game board with grid and scoreboard

#### Lesson 5 - random apples

* basic drawing

* random drawing

* list of objects to draw each frame

* use + - keys to add remove random apples

#### Lesson 6 - wormy lives (and dies)

* use arrow keys to move, one square at a time

* use arrow keys to choose direction

* game ends, end game scene

#### Lesson 7 - wormy eats apples

* scoreboard is updated

* new apples replace eaten apples

* different kinds of apples

#### Lesson 7 - wormy grows

* wormy has an array of body parts

* each part follows the previous

* wormy shouldn't eat himself

#### Lesson 8 - endgame

* lives

* high scorelist

#### Lesson 9 - credits

* scrolling credit scene

* game optimization and feature requests



