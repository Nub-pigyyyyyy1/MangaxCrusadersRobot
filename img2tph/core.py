from typing import List

from telegraph.aio import Telegraph

from plugins import MangaChapter


async def img2tph(manga_chapter: MangaChapter, name: str):
    lines = []
    for img in manga_chapter.pictures:
        a_tag = f'<img src="{img}"/>'
        lines.append(a_tag)
    content = '\n'.join(lines)

    client = Telegraph()
    await client.create_account('Manga Bot')
    page = await client.create_page(name, author_name='Manga Bot', author_url='https://t.me/mangaxCrusadersRobot', html_content=content)
    return page['url']
