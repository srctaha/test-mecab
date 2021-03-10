from fugashi import GenericTagger
import unidic

tagger = GenericTagger(f"-d '{unidic.DICDIR}' -p")

print(tagger("今日はいい天気"))
