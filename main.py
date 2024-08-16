from animeflv import AnimeFLV
with AnimeFLV() as api:
    elements = api.search(input("serie: "))
    for i, elements in enumerate(elements):
        print(f"{i}, {elements.title}")
        try:
            pass
        except Exception as e:
            print(e)
