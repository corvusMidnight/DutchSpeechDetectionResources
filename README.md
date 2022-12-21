![image](https://d2k0ddhflgrk1i.cloudfront.net/_processed_/1/0/csm_banner_fb58e3c35a.png)


# Dutch Speech Detection Resources

This repository functions as a collection of resources for the development and testing of speech detection/recognition/analysis tools for the Dutch/Flemish language. These include:

- ![](https://img.shields.io/badge/model-blue)
- ![](https://img.shields.io/badge/dataset-lightgreen)
- ![](https://img.shields.io/badge/corpus-orange)
- ![](https://img.shields.io/badge/website-red)

# Table of contents
* [Models](#models)
* [Data](#data)

```diff
! text in orange

```

# Models

| **Title** | **Type** | **Description** | **Size** | **Link** |
|-----------|----------|-----------------|----------|----------|
|```diff ! Wav2Vec2 ```|```diff ! Wav2Vec2 ```|```diff ! Wav2Vec2 ```|```diff ! Wav2Vec2 ```|```diff ! Wav2Vec2 ```|
| XLSR Wav2Vec2 Dutch by Jonatas Grosman | ![](https://img.shields.io/badge/model-blue) | "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the train and validation splits of Common Voice 6.1 and CSS10." |      -    |     [HuggingFace](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-dutch) |
| Dutch XLSR Wav2Vec2 Large 53 by Wietse de Vries   |    ![](https://img.shields.io/badge/model-blue)     |      "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice dataset. When using this model, make sure that your speech input is sampled at 16kHz."           |     -     |    [HuggingFace](https://huggingface.co/wietsedv/wav2vec2-large-xlsr-53-dutch)      |
| wav2vec2-large-xls-r-300m-nl   |    ![](https://img.shields.io/badge/model-blue)      |      "This model is a fine-tuned version of facebook/wav2vec2-xls-r-300m on the common_voice dataset." | - | [HuggingFace](https://huggingface.co/RuudVelo/wav2vec2-large-xls-r-300m-nl)         |
| Wav2Vec2-Large-XLSR-53-Dutch   |    ![](https://img.shields.io/badge/model-blue)      |      "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."           |     -     |     [HuggingFace](https://huggingface.co/nithinholla/wav2vec2-large-xlsr-53-dutch)     |
| wav2vec2-large-xlsr-53-Dutch by Mehdi Hosseini Moghadam   |     ![](https://img.shields.io/badge/model-blue)     | "Fine-tuned facebook/wav2vec2-large-xlsr-53 in Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."        |     -     | [HuggingFace](https://huggingface.co/MehdiHosseiniMoghadam/wav2vec2-large-xlsr-53-Dutch)     |
| simonsr wav2vec2-large-xlsr-dutch |     ![](https://img.shields.io/badge/model-blue)     |        "Fine-tuned facebook/wav2vec2-large-xlsr-53 on Dutch using the Common Voice. When using this model, make sure that your speech input is sampled at 16kHz."         |     -     |    [HuggingFace](https://huggingface.co/simonsr/wav2vec2-large-xlsr-dutch)      |
| facebook wav2vec2 large xlsr-53-dutch model   |     ![](https://img.shields.io/badge/model-blue)     |        "The model facebook wav2vec2 large xlsr-53-dutch is a Natural Language Processing (NLP) Model implemented in Transformer library, generally using the Python programming language."         |     -     |  [HuggingFace](https://huggingface.co/facebook/wav2vec2-large-xlsr-53-dutch)     |
|```diff !speechbrain```|```diff !speechbrain```|```diff !speechbrain```|```diff !speechbrain```|```diff !speechbrain```|
| speechbrain/lang-id-commonlanguage_ecapa Copied   |     ![](https://img.shields.io/badge/model-blue)     |        "This repository provides all the necessary tools to perform language identification from speech recordings with SpeechBrain. The system uses a model pretrained on the CommonLanguage dataset (45 languages)."         |     -     |     [HuggingFace](https://huggingface.co/speechbrain/lang-id-commonlanguage_ecapa)     |
|```diff !openai```|```diffopenai```|```diffopenai```|```diffopenai```|```diffopenai```|
| openai/whisper-large   |     ![](https://img.shields.io/badge/model-blue)     |       "The Whisper model was proposed in Robust Speech Recognition via Large-Scale Weak Supervision by Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever."          |     -     |     [HuggingFace](https://huggingface.co/openai/whisper-large)     |
| GroNLP/wav2vec2-dutch-large-ft-cgn   |     ![](https://img.shields.io/badge/model-blue)     |        "A Dutch Wav2Vec2 model. This model is created by further pre-training the original English facebook/wav2vec2-large model on Dutch speech from Het Corpus Gesproken Nederlands. Subsequently, the model is fine-tuned on the same Dutch speech using CTC."        |      -    |     [HuggingFce](https://huggingface.co/GroNLP/wav2vec2-dutch-large-ft-cgn)     |
|  Wav2Vec2-Large-XLSR-53-ft-CGN  |     ![](https://img.shields.io/badge/model-blue)     |         "This model is created by fine-tuning the facebook/wav2vec2-large-xlsr-53 model on Dutch speech from Het Corpus Gesproken Nederlands using CTC."        |     -     |     [HuggingFace](https://huggingface.co/GroNLP/wav2vec2-large-xlsr-53-ft-cgn)     |
| Coming soon...   |     ![](https://img.shields.io/badge/model-blue)     |                 |          |          |



# Data

| **Title** | **Type** | **Description** | **Size** | **Link** |
|-----------|----------|-----------------|----------|----------|
| Common Voice NL   |     ![](https://img.shields.io/badge/dataset-lightgreen)     | "The Common Voice dataset consists of a unique MP3 and corresponding text file. Many of the 9,283 recorded hours in the dataset also include demographic metadata like age, sex, and accent that can help train the accuracy of speech recognition engines. The dataset currently consists of 7,335 validated hours in 60 languages"         | 63 hours |   [HuggingFace](https://huggingface.co/datasets/common_voice/viewer/nl/train) |
| LibriVox   |    ![](https://img.shields.io/badge/website-red)    |       "Free public domain audiobooks"          |     295 books     |      [LibriVox](https://librivox.org/search?primary_key=19&search_category=language&search_page=1&search_form=get_results)    |
| MUST-C   |    ![](https://img.shields.io/badge/dataset-lightgreen)      | "Created by Di Gangi et al. at 2019, the MuST-C Dataset is a speech translation corpus containing 385 hours from Ted talks for speech translation from English into several languages: Dutch, French, German, Italian, Portuguese, Romanian, Russian, & Spanish. Requires filling request form., in Multi-Lingual language."         |    385 hours      |     [Fondazione Bruno Kessler](https://ict.fbk.eu/must-c/)     |
| dutch-vl-tts   |     ![](https://img.shields.io/badge/corpus-orange)     |        "This dataset contains 15.000 audio fragments of a male Dutch Flemish voice, the sentences read are extracted from the Mozilla Common Voice project."         |      15.000 audio recordings   |     [GitHub](https://github.com/r-dh/dutch-vl-tts)     |
| Corpus Gesproken Nederlands   |     ![](https://img.shields.io/badge/corpus-orange)     |        "In de periode 1998-2004 is in het kader van het project Corpus Gesproken Nederlandse (CGN) gewerkt aan de aanleg van een databank voor het hedendaags Nederlands zoals dat door volwassen sprekers in Nederland en Vlaanderen wordt gesproken. De resultaten van dit project zijn in maart 2004 beschikbaar gekomen."         |    -      |    [CGN](https://lands.let.ru.nl/cgn/)     |
| IFA Spoken Language Corpus   |     ![](https://img.shields.io/badge/corpus-orange)     | "The IFA Spoken Language corpus is a free (GPL) database of hand-segmented Dutch speech. It was constructed with off-the-shelf software using speech from 8 speakers in a variety of speaking styles. For a total of 50,000 words (41 minutes/speaker), speech acquisition and preparation took around 3 person-weeks per speaker."         |     4 hours     |     [IFA](https://www.fon.hum.uva.nl/IFA-SpokenLanguageCorpora/IFAcorpus/)     |
| CSS10    |     ![](https://img.shields.io/badge/dataset-lightgreen)     |        "CSS10 is a collection of single speaker speech datasets for 10 languages. Each of them consists of audio files recorded by a single volunteer and their aligned text sourced from LibriVox."         |     -     |     [kaggle](https://www.kaggle.com/datasets/bryanpark/dutch-single-speaker-speech-dataset)     |
| Spoken Wikipedia Corpus (Dutch)   |     ![](https://img.shields.io/badge/corpus-orange)     |       "The Spoken Wikipedia project unites volunteer readers of Wikipedia articles. Hundreds of spoken articles in multiple languages are available to users who are – for one reason or another – unable or unwilling to consume the written version of the article." | -  |    [kaggle](https://www.kaggle.com/datasets/rtatman/spoken-wikipedia-corpus-dutch)      |
| Corpus Gesproken Nederlands (CGN) |     ![](https://img.shields.io/badge/corpus-orange)     |       "Het Corpus Gesproken Nederlands (CGN) is een verzameling van 900 uur (bijna 9 miljoen woorden) hedendaagse Nederlandse spraak, afkomstig van Vlamingen en Nederlanders."          |     900 hours     |     [Instituut voor de Nederlandse taal](https://taalmaterialen.ivdnt.org/download/tstc-corpus-gesproken-nederlands/)     |
| Coming soon...   |          |                 |          |          |
