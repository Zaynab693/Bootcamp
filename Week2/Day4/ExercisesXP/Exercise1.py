#Exercise 1: Random Sentence Generatorimport random

# Step 1: Read words from a file
import random
def get_words_from_file(file_path="C:\\Users\\asus\\Desktop\\GenAI\\Week2\\Day4\\ExercisesXP\\words.txt"):
    """
    Reads a file and returns a list of words.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()         
            words = content.split()        
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Step 2: Generate a random sentence
def get_random_sentence(length, file_path="words.txt"):
    """
    Generates a random sentence of a given length from words in the file.
    """
    words_list = get_words_from_file(file_path)
    
    if not words_list:
        return "No words available to generate a sentence."
    
    # Select random words
    random_words = [random.choice(words_list) for _ in range(length)]
    
    # Join words into a sentence and convert to lowercase
    sentence = " ".join(random_words).lower()
    
    # Capitalize the first letter and add a period
    sentence = sentence.capitalize() + "."
    return sentence

# Step 3: Main program function
def main():
    print("Welcome to the Random Sentence Generator!")
    print("You can generate a random sentence of 2 to 20 words.\n")
    
    try:
        length = int(input("Enter desired sentence length (2-20): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    # Validate sentence length
    if length < 2 or length > 20:
        print("Invalid input. Length must be between 2 and 20.")
        return
    
    # Generate and print random sentence
    sentence = get_random_sentence(length)
    print("\nGenerated sentence:")
    print(sentence)

# Run the program
if __name__ == "__main__":
    main()
