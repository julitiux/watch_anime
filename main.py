from animeflv import AnimeFLV
with AnimeFLV() as api:
    elements = api.search(input("serie: "))
    for i, elements in enumerate(elements):
        print(f"{i}, {elements.title}")
        try:
            selection = int(input("select option"))
            info = api.get_anime_info(elements[selection].id)
            info.episodes.reverse()
            for j, episode in enumerate(info.episodes):
                print(f"{j} | Episode - {episode.id}")
            index_episode = int(input("select episode: "))
            serie = elements[selection].id

        except Exception as e:
            print(e)
