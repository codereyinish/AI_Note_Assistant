<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="99">
  <img src="https://img.icons8.com/?size=512&id=kTuxVYRKeKEY&format=png" width="99">
</p>
<p align="center">
    <h1 align="center">AI_NOTE_ASSISTANT</h1>
</p>
<p align="center">
    <em>Empower Your Notes with Intelligent Assistance!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/last-commit/codereyinish/AI_Note_Assistant?style=flat&logo=git&logoColor=white&color=c125ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/codereyinish/AI_Note_Assistant?style=flat&color=c125ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/codereyinish/AI_Note_Assistant?style=flat&color=c125ff" alt="repo-language-count">
	<a href="https://opensource.org/license/mit/">
		<img src="https://img.shields.io/github/license/codereyinish/AI_Note_Assistant?style=flat&logo=opensourceinitiative&logoColor=white&color=c125ff" alt="license">
	</a>
</p>
<p align="center">
    <em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/conda-44A833.svg?style=flat&logo=conda&logoColor=white" alt="Conda">
	<img src="https://img.shields.io/badge/pip-3775A9.svg?style=flat&logo=pypa&logoColor=white" alt="pip">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU Bash">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/OpenAI-1.35.3-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
	

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>
	
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Install](#-install)
  - [ 🤖 Usage ](#-usage)
- [🚧 Limitations and Future Plans of Project](#-limitations-and-future-plans-of-project)
  -[Limitations 🛑](#-limitations)
  -[ Future Plans 🌱](#-future-plans)
- [🤝 Contributing](#-contributing)	 
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>


## 📍 Overview

***Motivation***

Frustrated with generic AI responses, I created AI Note Assistant. It lets you upload notes directly into the system, where the model reads and analyzes them to provide accurate, context-specific answers. This approach saves time and boosts productivity by delivering tailored responses based on your documents.


***Objective***


AI Note Assistant enhances user interactions by utilizing the OpenAI Assistant API to read through uploaded files and provide tailored responses instead of generic ones. It offers a tutor-like experience, ensuring efficient information retrieval and response generation.



---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with a focus on document processing and interaction with the OpenAI assistant. It utilizes vector stores, file search, message threads, and conversational capabilities for responsive AI interactions. |
| 🔩 | **Code Quality**  | The codebase maintains a good level of quality with consistent style and adherence to best practices for Python development. It emphasizes readability, maintainability, and separation of concerns. |
| 📄 | **Documentation** | The project offers extensive documentation covering setup, usage, and inner workings of the AI Note Assistant. It provides clear explanations and examples, aiding developers in understanding and extending the functionality. |
| 🔌 | **Integrations**  | Key integrations include Python, JupyterLab, and OpenAI for enabling seamless execution and interaction with AI models. External dependencies are managed efficiently for enhanced functionality. |
| ⚡️  | **Performance**   | The project focuses on efficiency in interactions with the OpenAI assistant, aiming for fast responses and minimal resource usage. Performance optimizations are crucial for enhancing user experience and scalability. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include `py`, `ipynb`, `yml`, `jupyternotebook`, `python`, and `yaml` for various functionalities and integrations within the project. Dependency management is vital for smooth operation and compatibility. |

---

## 🗂️ Repository Structure

```sh
└── AI_Note_Assistant/
    ├── Note_Assistant.ipynb
    ├── Note_Assistant.py
    ├── Note_Environment.yml
    ├── README.md
    └── docs
        └── rag.docx
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                                                           | Summary                                                                                                                                                                                                                                                                                                                                     |
| ---                                                                                                            | ---                                                                                                                                                                                                                                                                                                                                         |
| [Note_Environment.yml](https://github.com/codereyinish/AI_Note_Assistant.git/blob/master/Note_Environment.yml) | Defines environment dependencies with Python, JupyterLab, and OpenAI for the AI Note Assistant project, ensuring seamless execution and interaction with AI models within a controlled environment.                                                                                                                                         |
| [Note_Assistant.py](https://github.com/codereyinish/AI_Note_Assistant.git/blob/master/Note_Assistant.py)       | Implements a document reader and responder tool within the OpenAI assistant. Configures vector stores, uploads files, sets up assistants with file search capability, initiates message threads, runs conversations, and retrieves responses tailored to provided document content for user queries.                                        |
| [Note_Assistant.ipynb](https://github.com/codereyinish/AI_Note_Assistant.git/blob/master/Note_Assistant.ipynb) | Improves OpenAI assistant by tailoring responses to provided document content. Implements knowledge retrieval with file search capability, generating contextually appropriate responses. Integrates document chunking, vector databases, semantic search, and blends retrieved information with original content for tutor-like responses. |

</details>

---

## 🚀 Getting Started

**System Requirements:**

* **Python**: 3.8+
* **JupyterNotebook**
* **Package manager/Container**: `conda`(Recommended), `pip`
* **LLM service**: `OpenAI` (Recommended), `Google Gemini`

### ⚙️ Installation

>1. **Clone the repository**:
>```bash
>git clone https://github.com/codereyinish/AI_Note_Assistant.git
> cd Ai-Note-Assistant
>```

>2. **Create the Conda environment**:

> ![conda](https://img.shields.io/badge/Anaconda-44A833.svg?style=flat&logo=Anaconda&logoColor=white)
>
>```bash
>conda env create -f Note_Environment.yml
> ```


>3. **Activate the environment**:
> ```bash
> conda activate noteAssistant_env
>    ```

>4. **Set up the OpenAI key**:
>Obtain your OpenAI API key from [OpenAI](https://www.openai.com/). Create a file named `.env` in the project root directory and add:
><a href="https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety" target ="_blank" style = "text-decoration: none">Refer this</a>
>```env
>OPENAI_API_KEY=your_openai_api_key
>```






### 🤖 Usage

<h4>From <code>source</code></h4>

> Run AI_Note_Assistant using the Jupyter Notebook:
> ```console
> $ jupyter nbconvert --execute Note_Assistant.ipynb
> ```

> Run AI_Note_Assistant as Python Script:
> ```console
> $ python Note_Assistant.py
> ```



---

### 🚧 Limitations and Future Plans of Project 

####  Limitations 🛑
1. **💸Cost of OpenAI API**: Utilizing the OpenAI Assistant API can become expensive, particularly if scaling the application. This cost consideration is important for long-term sustainability.
   
2. **📈Scalability Issues**: Integrating the AI Note Assistant into a website or scaling it for broader use may pose challenges due to resource demands and performance considerations.

3. **🤖 Potential for Generic Responses**: While ChatGPT effectively references notebook content for responses, the answers might sometimes appear too similar or copy-pasted, lacking personalized engagement.

#### Future Plans 🌱

To address these limitations and enhance the AI Note Assistant, future improvements include:

- **Fine-tuning Open Source LLMs**: Developing and integrating Open Source Language Model (LLM) solutions, which can offer cost-effective alternatives to proprietary APIs like OpenAI.
  
- **Enhanced Response Design**: Designing responses with a mix of components to avoid generic outputs:
  - **ChatGPT Writing Fillip**: Injecting creative and engaging writing style cues into responses.
  - **Notebook Content Retrieval**: Extracting specific and relevant information directly from uploaded documents.
  - **Scraping Linked Resources**: Scraping supplementary information from linked resources to enrich responses.
  - **Few-shot Learning Examples**: Incorporating few-shot learning examples to diversify writing styles and enhance context-specific responses.

These improvements aim to not only reduce operational costs but also enrich user interactions by providing more dynamic and contextually relevant AI responses.


---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/codereyinish/AI_Note_Assistant.git/issues)**: Submit bugs found or log feature requests for the `AI_Note_Assistant` project.
- **[Submit Pull Requests](https://github.com/codereyinish/AI_Note_Assistant.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/codereyinish/AI_Note_Assistant.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/codereyinish/AI_Note_Assistant.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/codereyinish/AI_Note_Assistant.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/AI_Note_Assistant.git">
   </a>
</p>
</details>

---

## 🎗 License

[MIT-License](LICENSE)

---

## 👏 Acknowledgments

- <a href="https://github.com/ShawhinT"  style="text-decoration: none;"> ShawinT </a>

<br>
<p align="right">
  <a href="#-overview"><b>Return</b></a>
</p>

---
