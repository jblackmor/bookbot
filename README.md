# BookBot: Novel Static Analysis Tool
 -BookBot was one of my first projects!

This repository contains a Python script that performs two types of static analysis on text files, specifically novels like *[Frankenstein](https://www.gutenberg.org/cache/epub/84/pg84.txt)*:

1. **Word Count**: It calculates the total number of words in the novel.
2. **Character Frequency**: It counts how many times each alphabetical character (A-Z) appears in the novel<br>Example: "The 'x' character was found 'y' times."

This project was created in collaboration with **[Boot.Dev](https://boot.dev)**.

## Features

- **Word Counting**: The script computes the total number of words in a text file.
- **Character Frequency**: It analyzes the frequency of each alphabetic character (ignoring case).

## How to Use

### Prerequisites
Make sure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

### Steps

1. **Download a Novel & Set the Path**:  
   - Ensure that you have the text file of the novel saved on your computer, and remember the book_path location (e.g. `path/to/your/frankenstein.txt`)
   - There are many eBooks to download for free on the [Project Gutenberg](https://www.gutenberg.org/) website.

2. **Run the Script**:  
   Once the path is known, run the main script:
   ```bash
   python3 main.py <path_to_book>
   ```
3. **View the Results**:  
   After running the script, you'll see:
    - The total number of words in the novel.
    - The frequency of each alphabetical character (a-z).

**Contributing**:
    Feel free to open issues or submit pull requests if you want to contribute or suggest new features. Contributions are always welcome!