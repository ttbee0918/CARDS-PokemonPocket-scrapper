from tcgPocket import TGCPocket
import json
import time


init_time = time.time()
filename = "pokemon_cards.json"


pocket = TGCPocket()


end_time = time.time()
print(
    f"Finished downloading cards to {filename}, total time: {
        end_time - init_time} segundos."
)


with open(filename, "w", encoding="utf-8") as file:
    json.dump(pocket.getCardData(), file, ensure_ascii=False, indent=4)
