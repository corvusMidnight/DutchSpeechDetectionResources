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
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |


# Data

| **Title** | **Type** | **Description** | **Size** | **Link** |
|-----------|----------|-----------------|----------|----------|
| Common Voice NL   |     dataset     | "The Common Voice dataset consists of a unique MP3 and corresponding text file. Many of the 9,283 recorded hours in the dataset also include demographic metadata like age, sex, and accent that can help train the accuracy of speech recognition engines. The dataset currently consists of 7,335 validated hours in 60 languages"         | 63 hours |   [HuggingFace](https://huggingface.co/datasets/common_voice/viewer/nl/train) |
| LibriVox   |    Audio Books (MP3)      |       "Free public domain audiobooks"          |     295 books     |      [LibriVox](https://librivox.org/search?primary_key=19&search_category=language&search_page=1&search_form=get_results)    |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
| Generic   |          |                 |          |          |
