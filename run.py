from fugashi import GenericTagger
import unidic

tagger = GenericTagger(f"-d '{unidic.DICDIR}' -p")

text = "今日はいい天気"

# parse can be used as normal
print(tagger.parse(text))

# features from the dictionary can be accessed by field numbers
for word in tagger(text):
    print(word.surface, word.feature[0])
