# Contains all functions that deal with stop word removal.

import os
import string
from document import Document

DATA_PATH = 'data'
STOPWORD_FILE_PATH = os.path.join(DATA_PATH, 'stopwords.json')

def remove_symbols(text_string: str) -> str:
    """
    Removes all punctuation marks and similar symbols from a given string.
    Occurrences of "'s" are removed as well.
    :param text:
    :return:
    """
 
    # traverse the given string and if any punctuation
    # mark occur replace it with null
    translator = str.maketrans('', '', string.punctuation)
    #string without punctuation
    text_remove_punct = text_string.translate(translator)
    # traverse the given string and if any possessive
    # mark occur replace it with null
    text_remove_possessive = text_remove_punct.replace("'s", "")
    return text_remove_possessive
    # TODO: Implement this function. (PR02)
    #raise NotImplementedError('Not implemented yet!')

def is_stop_word(term: str, stop_word_list: list[str]) -> bool:
    """
    Checks if a given term is a stop word.
    :param stop_word_list: List of all considered stop words.
    :param term: The term to be checked.
    :return: True if the term is a stop word.
    """
    #split the given term to meaningful words
    words = term.split()
    #convert to lower and check if it is a stopword 
    if any(word.lower() not in stop_word_list for word in words):
        return False
    else: 
        return True
    # TODO: Implement this function  (PR02)
    #raise NotImplementedError('Not implemented yet!')


def remove_stop_words_from_term_list(term_list: list[str]) -> list[str]:
    """
    Takes a list of terms and removes all terms that are stop words.
    :param term_list: List that contains the terms
    :return: List of terms without stop words
    """
    # Hint:  Implement the functions remove_symbols() and is_stop_word() first and use them here.
    # TODO: Implement this function. (PR02)
    #raise NotImplementedError('Not implemented yet!')
   
    #to open and save the stopword file and save it into a list
    with open(STOPWORD_FILE_PATH, 'r') as f:
             stop_word_list = [line.strip() for line in f.readlines()]
    filtered_term_list = []
    #Iterate the termlist and remove unwanted symbols and return filtered list
    for term in term_list:
        filtered_term = remove_symbols(term)
        if not is_stop_word(filtered_term, stop_word_list):
            filtered_term_list.append(filtered_term)
    return filtered_term_list  


def filter_collection(collection: list[Document]):
    """
    For each document in the given collection, this method takes the term list and filters out the stop words.
    Warning: The result is NOT saved in the documents term list, but in an extra field called filtered_terms.
    :param collection: Document collection to process
    """ 
    # Hint:  Implement remove_stop_words_from_term_list first and use it here.

    #Copy the output to document collection after performing all stopword functions
    for document in collection:
        document.filtered_terms = remove_stop_words_from_term_list(document.terms)
    
    # TODO: Implement this function. (PR02)
    # raise NotImplementedError('To be implemented in PR02')


def load_stop_word_list(raw_file_path: str) -> list[str]:
    """
    Loads a text file that contains stop words and saves it as a list. The text file is expected to be formatted so that
    each stop word is in a new line, e. g. like englishST.txt
    :param raw_file_path: Path to the text file that contains the stop words
    :return: List of stop words
    """
    #to open and save the stopword file and save it into a list
    with open(raw_file_path, 'r') as file:
        stop_word_list = [line.strip() for line in file.readlines()]
    return stop_word_list
    # TODO: Implement this function. (PR02)
    #raise NotImplementedError('To be implemented in PR02')

def create_stop_word_list_by_frequency(collection: list[Document]) -> list[str]:
    """
    Uses the method of J. C. Crouch (1990) to generate a stop word list by finding high and low frequency terms in the
    provided collection.
    :param collection: Collection to process
    :return: List of stop words
    """
    word_freq = {}
    #Iterate the collection and extract the frequency of word occurance
    for document in collection:
        for word in document.terms:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1]) 
    num_stop_words = len(sorted_words) // 2
    
    #appending values to stopword
    stop_words = [word for word, _ in sorted_words[:num_stop_words]]
    
    return stop_words

