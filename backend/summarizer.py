import nltk
from nltk.data import find
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

try:
    find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
    nltk.download("punkt_tab")


def summarize_terms(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary_sentences = summarizer(parser.document, 5)

    summary = " ".join(str(sentence) for sentence in summary_sentences)
    return summary

