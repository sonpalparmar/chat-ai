from app.api.routes.chat.models import ChatQuery
from app.services.ingestion.embedding import CustomCacheEmbedding
from app.services.ingestion.indexing import search_chunks
from app.services.chat.llms import get_result_from_llms
from fastapi import HTTPException


def query_handling(chat_query: ChatQuery):
    user_query = chat_query.query
    try:

        model = CustomCacheEmbedding()

        query_embedding = model.embed_documents(user_query)
        search_results = search_chunks(query_embeddings=query_embedding, limit=3)
        context = "\n".join(
            [result.payload.get("content", "") for result in search_results]
        )
        print("after search result")
        res = get_result_from_llms(
            model_name=chat_query.model, user_query=user_query, context=context
        )
        
        
        print(res)
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
