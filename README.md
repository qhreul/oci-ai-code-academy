<div align="center">
    <h1>
        <br/>
        <img src="img/repo_logo.png" alt="oci-ai-code-academy-logo" width="60"/>
        <br/>
        Oracle Cloud Infrastructure AI Code Academy
    </h1>
    <hr/>
</div>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3119/">
    <img src="https://img.shields.io/badge/python-3.11.9-blue.svg"/>
  </a>
  <a href="https://python-poetry.org/">
    <img src="https://img.shields.io/badge/dependency-poetry-%B2EA00"/>
  </a>
</p>

- [Description](#description)
- [Development](#development)
  - [Requirements](#requirements)
  - [Environment Variables](#environment-variables)
  - [How to prepare the environment](#how-to-prepare-the-environment) 

## Description <a name="description"></a>
Oracle University offers several courses to become familiar with the Oracle Cloud Infrastructure (OCI) services. One of 
these learning paths relates to [OCI Generative AI offering](https://mylearn.oracle.com/ou/learning-path/become-an-oci-generative-ai-professional/).
OCI Generative AI is a fully managed service that provides a set of state-of-the-art, customizable large language models 
(LLMs) that cover a wide range of use cases for text generation, summarization, and text embeddings.

Upon the completion of the OCI Generative AI Professional certification, the student will have learned:
* **Fundamentals of Large Language Models (LLMs)**: LLM basics, LLM architectures, Prompt Engineering, Fine-tuning techniques, fundamentals of code models, Multi-modal LLMs and Language Agents 
* **OCI Generative AI Deep-Dive**: Pretrained Foundational Models (Generation, Summarization, Embedding), Flexible Fine-tuning including T-Few techniques, Model Inference, Dedicated AI Clusters, Generative AI Security architecture  
* **Build a Conversational Chatbot with OCI Generative AI**: Understand RAG, Vector Databases, Semantic Search, build chatbot using LangChain Framework (Prompts, Models, Memory, Chains), Trace and Evaluate chatbot and deploy on OCI

## Development <a name="development"></a>

### Requirements <a name="requirements"></a>
* Git
* Python >= 3.11
* Poetry >= 1.7.0

### Environment Variables <a name="environment-variables"></a>
| **Name**      | **Description**                                 | **Default**  |
|---------------|-------------------------------------------------|--------------|
| `LOG_DIR`     | Location of the logging files                   | logs/        |
| `LOG_LEVEL`   | Logging level to be applied during execution    | INFO         |

_Populating `.env` file_

| **Name**             | **Description**                                                                            |
|----------------------|--------------------------------------------------------------------------------------------|
| `OCI_COMPARTMENT_ID` | Identifier of the compartment grouping Oracle Cloud Infrastructure (OCI) resources.        |
| `OCI_CONFIG_PROFILE` | Oracle Cloud Infrastructure CLI profile containing credentials to access the user account. |
| `OCI_ENDPOINT`       | Oracle Cloud Infrastructure endpoint to access Generative AI inference models.             |

**Note**: As prerequisite to setting the OCI CLI profile, the following steps are required:
1. Install the [OCI Command Line Interface (CLI)](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm) on your machine
2. Set up the configuration file (see [instructions](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#configfile))

### How to prepare the environment <a name="how-to-prepare-the-environment"></a>
* Install dependencies
  ```
  poetry update
  ```
