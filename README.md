# Auto Send Chat

Automatically send a message in a chat at a given date and time.

## Installation

### Install Pipenv

```bash
pip install pipenv
```

### Install Dependencies

```bash
pipenv install
```

## Usage

### Activate pipenv

```bash
pipenv shell
```

### Get mouse position

Run the following in the project directory and move the mouse to the text area of chat (within 5 s).

```bash
python mouse_pos.py
```

### Run auto-send.py

Change the date and time at which the message needs to be sent.
Note the mouse coordinates after running the previous command and change the 'x_pos' and 'y_pos' variables in auto-send.py and run the following.

```bash
python auto-send.py
```
