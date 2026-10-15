from maps.GakushokuSample import GakushokuSample
from maps.k25102_osusume import k25102_osusume

data = [
    k25102_osusume(),
    GakushokuSample(),
]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()