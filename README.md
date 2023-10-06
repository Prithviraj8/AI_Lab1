# Minimax
# Pre-requisites ?
1. Install python version 3 and above. Preferably 3.9.18
2. Use `pip install -r requirements.txt` to install the python version from the requirements file.
3. Add a .txt file under minimax/parse_data similar to the one that already exists: <b>input_file.txt and input_file2.txt </b>.
    This input file contains the input data on which the minimax algorithm executes
    <br>The file from which the input data has to be parsed must have a '.txt' extension in the filename as well.
4. And, that's it. You're set to use this minimax algorithm. Enjoy!

# How do I run the code ?
1. Once you follow the steps mentioned in the Pre-requisites, open your terminal.
2. cd into the folder Lab1(Minimax). This folder should have a minimax directory, .gitignore, requirements.txt and this README.md file that you're reading from.
3. Now, run any of the below commands based on your requirements to get the result and scores of various players based on the data given in the input file.

### Commands to run:
1. `python minimax/minimax.py min input_file.txt`
2. `python minimax/minimax.py max input_file.txt`
3. `python minimax/minimax.py -v min input_file.txt`
4. `python minimax/minimax.py -v max input_file.txt`
5. `python minimax/minimax.py -v -ab min input_file.txt`
6. `python minimax/minimax.py -v -ab max input_file.txt`
7. `python minimax/minimax.py -v -ab -range 10 min input_file.txt`
8. `python minimax/minimax.py -v -ab -range 10 max input_file.txt`
    

### Note:
Discussed possible techniques with Varun Tirthani.
All the code work is entirely my own.

