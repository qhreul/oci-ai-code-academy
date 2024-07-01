import os
from dotenv import load_dotenv

from llama_index.llms.oci_genai import OCIGenAI
from llama_index.embeddings.oci_genai import OCIGenAIEmbeddings

from oci_ai_code_academy.llms.config_model import ModelConfig, LLMParameters, EmbeddingParameters

load_dotenv()


class OCIGenerativeAIAdapter:

    def __init__(self, config: ModelConfig):
        """
        :param config: the configuration for the OCI Generative AI model
        """
        self.config = config

    def _load_oci_gen_ai_llm(self, parameters: LLMParameters):
        """
        :param parameters: parameters to configure the LLM
        :return: a configured large language model
        """
        llm = OCIGenAI(
            model=self.config.task_model_name,
            service_endpoint=os.getenv('OCI_GENAI_ENDPOINT'),
            compartment_id=os.getenv('OCI_COMPARTMENT_ID'),
            max_tokens=parameters.max_tokens,
            temperature=parameters.temperature,
        )
        return llm

    def _load_oci_gen_ai_embedding_model(self, parameters: EmbeddingParameters):
        """
        :param parameters: parameters to configure the embedding model
        :return: a configured embedding model
        """
        embedding_model = OCIGenAIEmbeddings(
            model_name=self.config.task_model_name,
            service_endpoint=os.getenv('OCI_GENAI_ENDPOINT'),
            compartment_id=os.getenv('OCI_COMPARTMENT_ID'),
            truncate=parameters.truncate,
            embed_batch_size=parameters.embed_batch_size
        )
        return embedding_model

    def load_oci_gen_ai(self, parameters):
        """
        :param parameters: parameters to configure the OCI models
        :return:
        """
        if self.config.task_type == 'generation':
            return self._load_oci_gen_ai_llm(parameters)
        elif self.config.task_type == 'embedding':
            return self._load_oci_gen_ai_embedding_model(parameters)
        else:
            raise NotImplementedError(f'Task {self.config.task_type} is not supported by current implementation')
