from typing import Optional

from pydantic import BaseModel, Field


class LLMParameters(BaseModel):
    max_tokens: int = Field(description='Maximum number of tokens that the LLM can generate', default=3000)
    temperature: float = Field(description='Parameter to control whether the output is more creative or more '
                                           'predictable. Lower values are used in tasks with a “correct” answer such '
                                           'as question answering or summarizing. Higher values enable the model to '
                                           'generate more “creative” outputs but might generate hallucinations or '
                                           'factually incorrect information.',
                               default=0.0, range=[0.0, 1.0])
    top_p: Optional[float] = Field(description='Parameter to ensure that only the most likely tokens with the sum p of '
                                               'their probabilities are considered for generation at each step. '
                                               'A higher p introduces more randomness into the output.',
                                   default=0.75, range=[0.0, 1.0])
    presence_penalty: Optional[float] = Field(description='Parameter to assign an equal penalty to every token that '
                                                          'appears in the prompt or output to encourage generating '
                                                          'outputs with tokens that have not been used.',
                                              default=0.0, range=[0.0, 1.0])
    frequency_penalty: Optional[float] = Field(description='Parameter to assign a penalty when a token appears '
                                                           'frequently, proportional to how many times it has already '
                                                           'appeared in the prompt or output. A higher penalty applies '
                                                           'a stronger penalty and can produce less repetitive outputs.',
                                               default=0.0, range=[0.0, 1.0])


class EmbeddingParameters(BaseModel):
    embed_batch_size: int = Field(description='Size of batch being processed', default=10)
    truncate: Optional[str] = Field(description='Truncate embeddings that are too long from start or end',
                                    default='END', allowed_values=['NONE', 'START', 'END'])


class ModelConfig(BaseModel):
    task_type: str = Field(description='Type of tasks to be handled by the Large Language Model (LLM)',
                           default='generation', allowed_values=['generation', 'chat', 'embedding'])
    task_model_name: str = Field(description='Name of the Large Language Model for the task')
