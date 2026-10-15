from maps.GakushokuSample import GakushokuSample
from maps.k25102_osusume import k25102_osusume

from maps.NimuraOsusume import NimuraOsusume
from maps.OkiOsusumeGakusyoku import GakushokuSample

data = [k25102_osusume(),
        NimuraOsusume(),
        GakushokuSample(),
        ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()