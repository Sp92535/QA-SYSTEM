from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.embeddings.gemini import GeminiEmbedding


def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
        
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20       

        index = VectorStoreIndex.from_documents(document)
        index.storage_context.persist()
        
        query_engine = index.as_query_engine()
        return query_engine
    
    except Exception as e:
        print(e)