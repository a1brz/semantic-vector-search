
# Semantic Vector Search

### Prerequisites
- **Python 3.7+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: To clone the repository. Download from [git-scm.com](https://git-scm.com/downloads).
- **Ollama**: Required for embeddings. Download from [Ollama](https://ollama.com/download).

### Setup Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/a1brz/semantic-vector-search.git
    cd semantic-vector-search
    ```

2. **Set Up Python Virtual Environment**
    - **Unix/macOS:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    - **Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3. **Install Required Modules**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4. **Install and Configure Ollama**
    - **Download Ollama:** Visit the [Ollama Download Page](https://ollama.com/download) and follow the installation instructions for your operating system.
    - **Start Ollama Server:**
        ```bash
        ollama serve
        ```
        > **Note:** Ensure that Ollama is running before proceeding to the next step.

5. **Download Embeddings Model**
    ```bash
    ollama pull mxbai-embed-large
    ```
    > **Note:** This command downloads the `mxbai-embed-large` model. Ensure you have a stable internet connection.

6. **Run the Semantic Search Script**
    ```bash
    python semantic_search.py
    ```

### Additional Tips

- **Deactivate Virtual Environment:**
    When you're done, you can deactivate the virtual environment by running:
    ```bash
    deactivate
    ```

- **Troubleshooting:**
    - If you encounter issues with `ollama serve`, ensure that no other services are conflicting on the required ports.
    - Verify that all dependencies are correctly installed. You can list installed packages using:
        ```bash
        pip list
        ```

- **Customization:**
    Feel free to modify `semantic_search.py` to better suit your specific use case or to experiment with different embedding models.

### Repository Structure

```
semantic-vector-search/
├── venv/                  # Python virtual environment
├── requirements.txt       # Python dependencies
├── semantic_search.py     # Main script for semantic search
├── README.md              # This readme file
├── .gitignore             # Git ignore file
└── ...                    # Additional files and folders
```
