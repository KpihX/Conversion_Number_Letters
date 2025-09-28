# Number to French Words Converter

This project provides a Python script that converts any given positive integer into its French word representation.

## Description

The script, `Nel.py`, defines a function `NeL(n)` that takes a positive integer as input and returns its equivalent in French words. The script is designed to handle numbers of any length, breaking them down into three-digit chunks and applying the appropriate grammatical rules for French number words.

## Features

- **Handles Numbers of Any Length**: The script can convert very large numbers, including those with thousands, millions, billions, and beyond.
- **Input Validation**: The script checks if the input is a positive integer and provides user-friendly error messages for invalid inputs, such as strings, floats, or negative numbers.
- **Correct French Grammar**: The script correctly applies French grammatical rules, including "et-un" for numbers like 21, 31, etc., and handles special cases like "quatre-vingts."
- **Interactive Command-Line Interface**: The script includes a simple interactive prompt that allows users to enter numbers and see the output in real-time.

## How to Run the Script

To run the script, you need to have Python installed.

1.  **Save the code**: Make sure the `Nel.py` file is saved on your local machine.
2.  **Open a terminal or command prompt**: Navigate to the directory where you saved the file.
3.  **Run the script**: Execute the following command:

    ```bash
    python Nel.py
    ```

4.  **Enter a number**: The script will prompt you to enter a positive integer. Type the number and press `Enter`.
5.  **View the output**: The script will display the number written in French words.
6.  **Continue or exit**: You will be asked if you want to enter another number. Type `o` to continue or `n` to exit.

## Examples

Here are a few examples of the script's output:

-   Input: `1` -> Output: `un`
-   Input: `21` -> Output: `vingt-et-un`
-   Input: `75` -> Output: `soixante-quinze`
-   Input: `100` -> Output: `cent`
-   Input: `123` -> Output: `cent vingt-trois`
-   Input: `1000` -> Output: `mille`
-   Input: `12345` -> Output: `douze mille trois cent quarante-cinq`
-   Input: `1999999` -> Output: `un million neuf cent quatre-vingt-dix-neuf mille neuf cent quatre-vingt-dix-neuf`

## Limitations

-   **Positive Integers Only**: The script is designed to work only with positive integers. It does not support negative numbers or decimals.
-   **French Language Only**: The output is exclusively in French.
-   **No External Libraries**: The script is self-contained and does not require any external libraries.