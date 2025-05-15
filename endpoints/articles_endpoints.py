from config.supabase_config import supabase
from config.cache import cache
from schemas.articles import Articles, InsertArticles, UpdateArticles, DeleteArticles
from typing import List
from fastapi import APIRouter, HTTPException
from endpoints.multimedia_endpoints import get_multimedia
import json

# Instancia del router
router = APIRouter(prefix='/articles', tags=['Articles'])

# Get the 3 latest articles
@router.get('/latest/{id_river}', response_model=List[Articles])
async def get_latest_articles(id_river: int) -> List[Articles]:
    try:

        response = (
            supabase.table('Articles')
            .select("*")
            .eq('id_river', id_river)
            .order('id_article', desc=True)
            .limit(3)
            .execute()
        )

        data = response.data

        for article in data:
            multimedia_id = article.get('id_multimedia')
            multimedia = await get_multimedia(multimedia_id)
            article.update(multimedia)

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all the articles
@router.get('/{id_river}')
async def get_articles(id_river: int):
    key = f'articles_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        response = (
            supabase.table('Articles')
            .select("*")
            .eq('id_river', id_river)
            .execute()
        )

        data = response.data

        for article in data:
            multimedia_id = article.get('id_multimedia')
            multimedia = await get_multimedia(multimedia_id)
            article.update(multimedia)

        articles = {}

        article_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Articles/articles_hero%')
            .execute()
        )

        articles.update({
            "articles_hero": article_hero.data[0],
            "articles": data
        })

        cache.setex(key, 1, json.dumps(articles))

        return articles

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert Article
@router.post('/add', response_model=Articles)
async def add_article(article: InsertArticles) -> Articles:
    try:

        article_data = article.model_dump()

        response = (
            supabase.table('Articles')
            .insert(article_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update Article
@router.put('/update', response_model=Articles)
async def update_article(article: UpdateArticles) -> Articles:
    try:

        article_data = article.model_dump(exclude_none=True)

        response = (
            supabase.table('Articles')
            .update(article_data)
            .eq('id_article', article_data['id_article'])
            .eq('id_river', article_data['id_river'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete Article
@router.delete('/delete', response_model=Articles)
async def delete_article(article: DeleteArticles) -> Articles:
    try:

        article_data = article.model_dump()

        response = (
            supabase.table('Articles')
            .delete()
            .eq('id_article', article_data['id_article'])
            .eq('id_river', article_data['id_river'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
articles_router = router
