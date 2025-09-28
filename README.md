# Number to Words Converter

This project provides Python scripts to convert any given positive integer into its word representation in both French and English.

## Description

The repository contains two main scripts:
- `Nel.py`: Converts numbers to French words.
- `Enl.py`: Converts numbers to English words.

Both scripts define a function (`NeL(n)` for French, `EnL(n)` for English) that takes a positive integer as input and returns its equivalent in words. The scripts are designed to handle numbers of any length by breaking them down into three-digit chunks and applying the appropriate grammatical rules for each language.

## Features

- **Multi-Language Support**: Provides number-to-word conversion for both English and French.
- **Handles Numbers of Any Length**: The scripts can convert very large numbers, including those with thousands, millions, billions, and beyond.
- **Input Validation**: Each script checks if the input is a positive integer and provides user-friendly error messages for invalid inputs (e.g., strings, floats, negative numbers).
- **Correct Grammar**: The scripts apply correct grammatical rules for both languages, including special cases.
- **Interactive Command-Line Interface**: Both scripts include a simple interactive prompt that allows users to enter numbers and see the output in real-time.

## How to Run the Scripts

To run the scripts, you need to have Python installed.

### English Version (`Enl.py`)

1.  **Open a terminal or command prompt**.
2.  **Run the script**:
    ```bash
    python Enl.py
    ```
3.  **Enter a number**: The script will prompt you to enter a positive integer.
4.  **Continue or exit**: You will be asked if you want to enter another number (`y`/`n`).

### French Version (`Nel.py`)

1.  **Open a terminal or command prompt**.
2.  **Run the script**:
    ```bash
    python Nel.py
    ```
3.  **Enter a number**: The script will prompt you to enter a positive integer.
4.  **Continue or exit**: You will be asked if you want to enter another number (`o`/`n`).

## Examples

### English (`Enl.py`)
-   Input: `21` -> Output: `twenty-one`
-   Input: `101` -> Output: `one hundred and one`
-   Input: `12345` -> Output: `twelve thousand three hundred and forty-five`
-   Input: `1999999` -> Output: `one million nine hundred and ninety-nine thousand nine hundred and ninety-nine`

### French (`Nel.py`)
-   Input: `21` -> Output: `vingt-et-un`
-   Input: `75` -> Output: `soixante-quinze`
-   Input: `123` -> Output: `cent vingt-trois`
-   Input: `12345` -> Output: `douze mille trois cent quarante-cinq`

## Limitations

-   **Positive Integers Only**: The scripts are designed to work only with positive integers. They do not support negative numbers or decimals.
-   **No External Libraries**: The scripts are self-contained and do not require any external libraries.