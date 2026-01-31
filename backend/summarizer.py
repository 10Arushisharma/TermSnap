import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

nltk.download("punkt")

def summarize_terms(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary_sentences = summarizer(parser.document, 5)

    summary = " ".join(str(sentence) for sentence in summary_sentences)
    return summary

