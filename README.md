# Dutch Speech Detection Resources

This repository functions as a collection of resources for the development and testing of speech detection/recognition/analysis tools
for the Dutch/Flemish language.

# Table of contents
* [Models](#models)
* [Data](#data)

# Models

| **Title** | **Type** | **Description** | **Size** | **Link** |
|-----------|----------|-----------------|----------|----------|
| XLSR Wav2Vec2 Dutch by Jonatas Grosman | model | "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the train and validation splits of Common Voice 6.1 and CSS10." |      -    |     [HuggingFace](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-dutch) |
| Dutch XLSR Wav2Vec2 Large 53 by Wietse de Vries   |    model      |      "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice dataset. When using this model, make sure that your speech input is sampled at 16kHz."           |     -     |    [HuggingFace](https://huggingface.co/wietsedv/wav2vec2-large-xlsr-53-dutch)      |
| wav2vec2-large-xls-r-300m-nl   |    model      |      "This model is a fine-tuned version of facebook/wav2vec2-xls-r-300m on the common_voice dataset." | - | [HuggingFace](https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-300m-nl)         |
| Wav2Vec2-Large-XLSR-53-Dutch   |    model      |      "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."           |     -     |     [HuggingFace](https://huggingface.co/nithinholla/wav2vec2-large-xlsr-53-dutch)     |
| wav2vec2-large-xlsr-53-Dutch by Mehdi Hosseini Moghadam   |     model     | "Fine-tuned facebook/wav2vec2-large-xlsr-53 in Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."        |     -     | [HuggingFace](https://huggingface.co/MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-Dutch)     |
| simonsr wav2vec2-large-xlsr-dutch |     model     |        "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."         |     -     |    [HuggingFace](https://huggingface.co/simonsr/wav2vec2-large-xlsr-dutch)      |
| facebook wav2vec2 large xlsr-53-dutch model   |     model     |        "The model facebook wav2vec2 large xlsr-53-dutch is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language."         |     -     |  [HuggingFace](https://huggingface.co/facebook/wav2vec2-large-xlsr-53-dutch)     |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |

# Data

| **Title** | **Type** | **Description** | **Size** | **Link** |
|-----------|----------|-----------------|----------|----------|
| Common Voice NL   |     dataset     | "The Common Voice dataset consists of a unique MP3 and corresponding text file. Many of the 9,283 recorded hours in the dataset also include demographic metadata like age, sex, and accent that can help train the accuracy of speech recognition engines. The dataset currently consists of 7,335 validated hours in 60 languages"         | 63 hours |   [HuggingFace](https://huggingface.co/datasets/common_voice/viewer/nl/train) |
| LibriVox   |    Audio Books (MP3)      |       "Free public domain audiobooks"          |     295 books     |      [LibriVox](https://librivox.org/search?primary_key=19&search_category=language&search_page=1&search_form=get_results)    |
| MUST-C   |    dataset      | "Created by Di Gangi et al. at 2019, the MuST-C Dataset is a speech translation corpus containing 385 hours from Ted talks for speech translation from English into several languages: Dutch, French, German, Italian, Portuguese, Romanian, Russian, & Spanish. Requires filling request form., in Multi-Lingual language."         |    385 hours      |     [Fondazione Bruno Kessler](https://ict.fbk.eu/must-c/)     |
| dutch-vl-tts   |     dataset     |        "This dataset contains 15.000 audio fragments of a male Dutch Flemish voice, the sentences read are extracted from the Mozilla Common Voice project."         |      15.000 audio recordings   |     [GitHub](https://github.com/r-dh/dutch-vl-tts)     |
| Corpus Gesproken Nederlands   |     dataset     |        "In de periode 1998-2004 is in het kader van het project Corpus Gesproken Nederlandse (CGN) gewerkt aan de aanleg van een databank voor het hedendaags Nederlands zoals dat door volwassen sprekers in Nederland en Vlaanderen wordt gesproken. De resultaten van dit project zijn in maart 2004 beschikbaar gekomen."         |    -      |    [CGN](https://lands.let.ru.nl/cgn/)     |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
