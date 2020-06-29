from deepsegment import DeepSegment


class DeepSegmentPunctuation:
    """
    add punctuation to a text using the deepsegment module from
    https://github.com/notAI-tech/deepsegment
    """

    def __init__(self):
        self.segmenter = DeepSegment('en')

    def punctuate_text(self, string):
        sentences = self.segmenter.segment_long(string, n_window=len(string))
        text = ""
        for sentence in sentences:
            text += sentence
            text += ". "
        return text
