from celery import shared_task
import PyPDF2
from textblob import TextBlob
import time


@shared_task
def analyze_document_task(doc_id):
    from .models import Analysis, Documents
    import PyPDF2
    from textblob import TextBlob
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lex_rank import LexRankSummarizer

    try:
        doc = Documents.objects.get(id=doc_id)
        # 1. Update status immediately
        doc.status = "processing"
        doc.save()

        # 2. Extract Text
        reader = PyPDF2.PdfReader(doc.pdf.path)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text += text

        # 3. Sentiment Analysis (Fix typo: polarity, not porality)
        blob = TextBlob(full_text)
        score = blob.sentiment.polarity  # FIXED TYPO

        # Your custom sentiment logic (Great touch!)
        sentiment_label = "Neutral"
        if score < 0:
            sentiment_label = "Tragic" if score <= -0.5 else "Shallow"
        elif score > 0:
            sentiment_label = "Excellent" if score >= 0.6 else "Energetic"

        # 4. Summarization (Fix syntax errors)
        # We use full_text (string), not blob (object)
        parser = PlaintextParser.from_string(full_text, Tokenizer("english"))
        summarizer = LexRankSummarizer()

        # summarizer returns a TUPLE of sentences. We must join them.
        summary_sentences = summarizer(
            parser.document, 3)  # Let's get 3 sentences
        # FIXED: Use a string join on the list of sentences
        final_summary = " ".join([str(s) for s in summary_sentences])

        # 5. Save Analysis
        Analysis.objects.create(
            document=doc,
            summary=final_summary,
            sentiment=sentiment_label,
        )

        doc.status = 'completed'
        doc.save()
        return f"Document {doc_id} analyzed successfully"

    except Documents.DoesNotExist:
        return "Document Not Found"
    except Exception as e:
        if 'doc' in locals():
            doc.status = 'failed'
            doc.save()
        return f"Task failed: {str(e)}"
