# Import all required module
from tkinter import Tk, PhotoImage, Entry, Label, Button, messagebox, IntVar, END
import random


# Create a function to run the game
def run():
    # Create the window
    window = Tk()
    # Add window title
    window.title("Hangman")
    # Add window size
    window.geometry('800x500')

    # Create a list of name and picture of animals
    data = [
        ['cat', PhotoImage(file='./images/cat.png').zoom(5).subsample(26)],
        ['sheep', PhotoImage(file='./images/sheep.png').zoom(5).subsample(40)],
        ['elephant', PhotoImage(file='./images/elephant.png').zoom(5).subsample(22)]
    ]

    # Run a new game on the window
    new_game(window, data)
    # Update the screen
    window.mainloop()


# Create a function to run the new game on the window
def new_game(window, data):
    # Select an item from the data list
    question = random.choice(data)
    # Get the word from the list
    word = question[0]
    # Get the image from the list
    image = question[1]

    # Create a variable for guesses and set it to 3
    n_guess = IntVar()
    n_guess.set(3)

    # Generate the display
    generate_display(window, data, word, image, n_guess)


# Create a function to generate the display
def generate_display(window, data, word, image, n_guess):
    # Add animal image to the screen
    image_label = Label(window)
    image_label.config(image=image)
    image_label.place(x=10, y=10)

    # Create a button to start new game
    new_word = Button(window, text="New Word", command=lambda: new_game(window, data), width=17)
    new_word.place(x=300, y=80)

    # Take the input from the user
    user_word = Entry(window)
    user_word.insert(0, "Enter the animal name")
    user_word.place(x=300, y=110)

    # Create a submit button and check if player input is correct or not
    submit_button = Button(window, text="Submit", 
                           command=lambda: check(window, data, word, image, n_guess, user_word), 
                           width=17)
    submit_button.place(x=300, y=140)

    # Create a label to show the number of guesses left
    guess_label = Label(window, text=f"Number of guess left: {n_guess.get()}")
    guess_label.place(x=600, y=20)

    # Display the keyboard on the window
    keyboard(window, user_word)


# Create a function to check the player input
def check(window, data, word, image, n_guess, user_word):
    # If number of guesses if than 1, let the game mover future
    # Else end the game
    if n_guess.get() > 1:
        # Check if word matches or not
        if user_word.get().lower() == word:
            # Show the player wining message and end the game
            messagebox.showinfo("Hangman", "You guessed it!")
            window.destroy()
        else:
            # Reduce the number of guesses and regenerate the display
            n_guess.set(n_guess.get() - 1)
            generate_display(window, data, word, image, n_guess)
    else:
        # Show the player losing message and end the game
        messagebox.showwarning("Hangman", "Game Over")
        window.destroy()


# Create a function to generate the keyboard
def keyboard(window, user_word):
    # Create a list of letters
    keys = [["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            ["J", "K", "L", "M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X", "Y", "Z"]]

    # Create a loop for each key and show them on display
    for i in range(len(keys)):
        for j, key in enumerate(keys[i]):
            # Create the button and if player clicks on it update the value of input
            alpha = Button(window, text=key, command=lambda key=key: update_word(user_word, key), 
                           width=4)
            alpha.place(x=80 * j + 40, y=50 * (i + 6))


# Create a function to update the word entered by the player 
def update_word(user_word, letter):
    # If user is entering the first letter, clear the placeholder
    # and insert new letter
    # Else add the letter at the end of word
    if user_word.get() == "Enter the animal name":
        user_word.delete(0, END)
        user_word.insert(END, letter)
    else:
        user_word.insert(END, letter)


# Run the game
run()
