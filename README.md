# ebook_analysis

Word Frequency Analysis of Printed Books on Wikibooks

Overview:

This project focuses on deriving word frequencies from printed books available on Wikibooks. The user inputs the book's name, and the system provides a word frequency analysis. Users can either analyze a single book's word frequency or compare the word frequency between two books.

Features:


Obtain word frequency for a given book.


Compare word similarities and differences between two books.


Flexibility for users to determine the number of words displayed.


Technical Details:


Web Scraping: Utilizes requests and BeautifulSoup libraries to extract the content of books. Error handling is implemented for potential incorrect inputs by the user.

Data Processing: After web scraping, the data is stored in a .txt file, post which it is read, cleaned (removal of punctuation, conversion to lowercase), and tokenized.

Word Analysis: After tokenization, stopwords are filtered out. The frequencies of the words are then counted, sorted, and presented to the user based on their preferences.


Challenges and Resolutions:


File Reading/Writing: Encountered encoding issues during file operations, which was resolved using the utf-8 encoding.

Word Processing: Initial approach using the replace() function led to undesired word truncations. Resolved by iterating through each word.

Handling Sets: Due to the unordered nature of sets, converting them back to lists was necessary to maintain consistency across outputs.


Experiments:

Comparison experiments conducted on books like 'Non-Programmer's Tutorial for Python 2.6' and 'Non-Programmer's Tutorial for Python 3' indicated a difference from the results of Online Word Counter, attributed to varying stopword lists.

