import os

import chromadb
from llama_index.core import StorageContext
from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from oci_ai_code_academy import settings

import logging
from logging.config import dictConfig
dictConfig(settings.LOG_CONFIG)
logger = logging.getLogger(__name__)


class ChromaDBUtil:

    def __init__(self, storage_path: str = './chroma_db', collection_name: str = 'default'):
        """
        :param storage_path: local path where data is persisted
        :param collection_name:
        """
        self.db_client = chromadb.PersistentClient(path=storage_path)
        self.collection = self.db_client.get_or_create_collection(collection_name)
        self.vector_store = ChromaVectorStore(chroma_collection=self.collection)
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)

    def load_data(self, content_path: str, embedding_model: BaseEmbedding,
                  chunk_size: int = 2500, chunk_overlap: int = 100):
        """
        :param content_path: path to the content to be loaded in the vector store
        :param embedding_model: embedding model used to vectorize the documents
        :param chunk_size: size of chunks when splitting documents
        :param chunk_overlap: number of characters overlapping across chunks
        TODO add support for multiple doc types
        """

    def _load_pdf_data(self, content_path: str, chunk_size: int, chunk_overlap: int):
        """
        :param content_path: path to the PDF documents to be loaded
        :param chunk_size: size of chunks when splitting documents
        :param chunk_overlap: number of characters overlapping across chunks
        :return: a set of processed chunks extracted from PDF documents
        """
