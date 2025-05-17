# Tokenization

This is the process of breaking down large texts into chunks or subwords or the process of breaking down large text strings into smaller units.

## Byte-Pair Encoding

### Algorithm - Encoding

1. Identify frequent pairs
   - In each iteration, scan the text to find the most common occuring pair of bytes (or characters)
2. Replace and record
   - Replace that pair with a new placeholder ID (one not already in use - say for instace we start with 0 to 255 then the next ID will be 256)
   - Record this mapping in a lookup table
   - The size of the lookup table is a hyperparameter, also called "vocabulary size"
3. Repeat until no gains
   - Keep reperating steps 1 and 2, continually merging the most frequent pairs
   - Stop when no further compression is possible

### Decoding

- To restore teh original text, reverse the process by substituting each ID with its corresponding pair using the lookup table
