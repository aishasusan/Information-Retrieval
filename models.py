# Contains all retrieval models.

from abc import ABC, abstractmethod

from document import Document


class RetrievalModel(ABC):
    @abstractmethod
    def document_to_representation(self, document: Document, stopword_filtering=False, stemming=False):
        """
        Converts a document into its model-specific representation.
        This is an abstract method and not meant to be edited. Implement it in the subclasses!
        :param document: Document object to be represented
        :param stopword_filtering: Controls, whether the document should first be freed of stopwords
        :param stemming: Controls, whether stemming is used on the document's terms
        :return: A representation of the document. Data type and content depend on the implemented model.
        """

    @abstractmethod
    def query_to_representation(self, query: str):
        """
        Determines the representation of a query according to the model's concept.
        :param query: Search query of the user
        :return: Query representation in whatever data type or format is required by the model.
        """

    @abstractmethod
    def match(self, document_representation, query_representation) -> float:
        """
        Matches the query and document presentation according to the model's concept.
        :param document_representation: Data that describes one document
        :param query_representation:  Data that describes a query
        :return: Numerical approximation of the similarity between the query and document representation. Higher is
        "more relevant", lower is "less relevant".
        """

class LinearBooleanModel(RetrievalModel):

    # TODO: Implement all abstract methods and __init__() in this class. (PR02)
    def __init__(self):
        def __init__(self):
            pass
         
    def linear_search(self, search_term, document_collection):
        result = []
        for document in document_collection:
            terms = self.document_to_representation(document)
            if search_term in terms:
                result.append(document)
        return result   

    #abstract method implementation to process queries
    def query_to_representation(self, query: str):
        return [word for word in query.split()]
   
    #abstract method implementation to process document
    def document_to_representation(self, document, stopword_filtering=False, stemming=False):
        processed_document = document.terms  # Use document.terms instead of filtered_terms
        if stopword_filtering:
            processed_document = [word for word in processed_document if word not in self.stopwords]
        if stemming:
            processed_document = [self.stemmer.stem(word) for word in processed_document]
        return processed_document
    
    #abstract method implementation to match document
    def match(self, document_representation, query_representation) -> float:
        intersection = len(frozenset(document_representation).intersection(set(query_representation)))
        union = len(frozenset(document_representation).union(set(query_representation)))
        return intersection / union

    def __str__(self):
        return 'Boolean Model (Linear)'



class InvertedListBooleanModel(RetrievalModel):
    # TODO: Implement all abstract methods and __init__() in this class. (PR03)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function. (PR3, Task 2)

    def __str__(self):
        return 'Boolean Model (Inverted List)'


class SignatureBasedBooleanModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Boolean Model (Signatures)'


class VectorSpaceModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Vector Space Model'


class FuzzySetModel(RetrievalModel):
    # TODO: Implement all abstract methods. (PR04)
    def __init__(self):
        raise NotImplementedError()  # TODO: Remove this line and implement the function.

    def __str__(self):
        return 'Fuzzy Set Model'
