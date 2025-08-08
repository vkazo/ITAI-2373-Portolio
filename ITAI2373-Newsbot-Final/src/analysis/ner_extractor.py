# Named Entity Recognition module
# 🕸️ Entity Relationship Mapping# TODO: Implement advanced entity recognition and relationship mappingclass EntityRelationshipMapper:    """    Advanced NER with relationship extraction and network analysis    TODO: Build sophisticated entity understanding    """        def __init__(self):        # TODO: Initialize NER and relationship extraction components        # Hint: Consider:        # - Multiple NER models (spaCy, transformers, custom)        # - Relationship extraction techniques        # - Entity linking and disambiguation        # - Knowledge graph construction        pass        def extract_entities(self, article_text):        """        TODO: Extract and classify entities                Should identify:        - People (with roles/titles)        - Organizations (with types)        - Locations (with hierarchies)        - Events (with dates/contexts)        - Products, technologies, etc.        """        pass        def extract_relationships(self, article_text):        """        TODO: Extract relationships between entities                Examples:        - "CEO of" (person -> organization)        - "located in" (organization -> location)        - "acquired by" (organization -> organization)        - "attended" (person -> event)        """        pass        def build_knowledge_graph(self, articles):        """        TODO: Build knowledge graph from multiple articles                This creates a network of entities and relationships        that can reveal:        - Key players in different domains        - Hidden connections between entities        - Influence networks        - Trending relationships        """        pass        def find_entity_connections(self, entity1, entity2):        """        TODO: Find connections between two entities                This could help answer questions like:        - "How are Apple and Tesla connected?"        - "What's the relationship between Biden and climate change?"        """        pass# TODO: Test your entity mapper# entity_mapper = EntityRelationshipMapper()print("🕸️ Entity relationship mapper ready for implementation!")# 🕸️ Entity Relationship Mapping

# 🕸️ Entity Relationship Mapping
import spacy
import networkx as nx
from collections import defaultdict

class EntityRelationshipMapper:
    """
    Advanced NER with relationship extraction and network analysis.
    Extracts named entities, builds a relationship graph, and finds entity-level connections.
    """
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.graph = nx.Graph()

    def extract_entities(self, article_text):
        """
        Extract and classify entities using spaCy.
        Identifies:
        - People (with roles/titles)
        - Organizations (with types)
        - Locations (with hierarchies)
        - Events (with dates/contexts)
        - Products, technologies, etc.
        """
        doc = self.nlp(article_text)
        entities = defaultdict(set)

        for ent in doc.ents:
            entities[ent.label_].add(ent.text)

        return {label: list(values) for label, values in entities.items()}

    def extract_relationships(self, article_text):
        """
        Extract relationships between entities using rule-based heuristics.
        Examples include:
        - "CEO of" (person -> organization)
        - "located in" (organization -> location)
        - "acquired by" (organization -> organization)
        - "attended" (person -> event)
        """
        doc = self.nlp(article_text)
        relationships = []

        for sent in doc.sents:
            ents = list(sent.ents)
            for i, ent1 in enumerate(ents):
                for j, ent2 in enumerate(ents):
                    if i != j:
                        if "CEO" in sent.text and ent1.label_ == "PERSON" and ent2.label_ == "ORG":
                            relationships.append((ent1.text, "CEO of", ent2.text))
                        elif "acquired" in sent.text and ent1.label_ == "ORG" and ent2.label_ == "ORG":
                            relationships.append((ent1.text, "acquired", ent2.text))
                        elif "located in" in sent.text and ent1.label_ == "ORG" and ent2.label_ == "GPE":
                            relationships.append((ent1.text, "located in", ent2.text))
                        elif "attended" in sent.text and ent1.label_ == "PERSON" and ent2.label_ == "EVENT":
                            relationships.append((ent1.text, "attended", ent2.text))

        return relationships

    def build_knowledge_graph(self, articles):
        """
        Build a knowledge graph from multiple articles.
        Constructs a network of entities and relationships for analysis.
        """
        for article in articles:
            relationships = self.extract_relationships(article)
            for ent1, relation, ent2 in relationships:
                self.graph.add_node(ent1)
                self.graph.add_node(ent2)
                self.graph.add_edge(ent1, ent2, label=relation)

    def find_entity_connections(self, entity1, entity2):
        """
        Find and return the shortest relationship path between two entities.
        Useful for questions like:
        - "How are Apple and Tesla connected?"
        - "What's the relationship between Biden and climate change?"
        """
        if nx.has_path(self.graph, entity1, entity2):
            path = nx.shortest_path(self.graph, entity1, entity2)
            connections = []
            for i in range(len(path) - 1):
                edge_data = self.graph.get_edge_data(path[i], path[i + 1])
                label = edge_data.get("label", "related to")
                connections.append((path[i], label, path[i + 1]))
            return connections
        return []

print("🕸️ Entity relationship mapper ready for implementation!")
