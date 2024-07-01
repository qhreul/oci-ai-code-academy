from unittest import TestCase, main
from parameterized import parameterized

from llama_index.llms.oci_genai import OCIGenAI
from llama_index.embeddings.oci_genai import OCIGenAIEmbeddings

from oci_ai_code_academy.llms.config_model import ModelConfig, LLMParameters, EmbeddingParameters
from oci_ai_code_academy.llms.adapters.oci_gen_ai_adapter import OCIGenerativeAIAdapter


class TestOCIGenerativeAIAdapter(TestCase):

    @parameterized.expand([
        ('generation', LLMParameters(), OCIGenAI),
        ('embedding', EmbeddingParameters(), OCIGenAIEmbeddings)
    ])
    def test_load_oci_gen_ai(self, task_type: str, parameters, expected_cls):
        """
        :param task_type: the type of tasks to be performed
        :param parameters: the list of parameters to be taken into account
        :param expected_cls: the expected class
        """
        config = ModelConfig(task_type=task_type, task_model_name='cohere.command')
        adapter = OCIGenerativeAIAdapter(config)
        configured_model = adapter.load_oci_gen_ai(parameters)

        self.assertTrue(type(configured_model), expected_cls)

    def test_load_oci_gen_ai_not_implemented_error(self):
        config = ModelConfig(task_type='invalid', task_model_name='invalid')
        adapter = OCIGenerativeAIAdapter(config)
        with self.assertRaises(NotImplementedError):
            adapter.load_oci_gen_ai(None)


if __name__ == '__main__':
    main()
