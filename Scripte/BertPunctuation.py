import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM


# --------- STATIC FUNCTIONS -----------
def format_text(text_list):
    """
    make a readable text (string) from the list
    """
    text = " ".join(text_list)
    text = text.replace(" . ", ". ")
    text += "."
    return text


# --------------- CLASS -----------------
class BertPunctuation:
    """
    add punctuation to a text using BERT
    https://stackoverflow.com/questions/54978443/predicting-missing-words-in-a-sentence-natural-language-processing-model
    """

    def __init__(self):
        # Load pre-trained model tokenizer (vocabulary)
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

        # Load pre-trained model (weights)
        self.model = BertForMaskedLM.from_pretrained('bert-base-uncased')
        self.model.eval()

    def punctuate_text(self, string):
        """
        add punctuation to string using the pre-trained BERT
        """
        tokenized_text = self.tokenize(string)

        # Tokenizer splits auf things words like "can't" to "can", "##t" so for putting it back together
        # in a human-readable way we need to use the text split by whitespaces
        text_list = string.split(" ")

        predictions = self.predict_tokens(tokenized_text)
        prediction_index = 0

        # replace [MASK]s with predicted tokens
        for word in text_list:
            if '[MASK]' in word:
                text_list[text_list.index(word)] = predictions[prediction_index]
                prediction_index += 1

        return format_text(text_list)

    def tokenize(self, string):
        """
        use BERT tokenizer to tokenize the string
        """
        return self.tokenizer.tokenize(string)

    def predict_tokens(self, tokenized_text):
        """
        Predict the tokens at [MASK]
        """

        # Create the segments tensors.
        tensors = self.create_tensors(tokenized_text)
        tokens_tensor = tensors[0]
        segments_tensors = tensors[1]

        # Predict all tokens
        with torch.no_grad():
            predictions = self.model(tokens_tensor, segments_tensors)

        predicted_tokens = []
        for word in tokenized_text:
            if '[MASK]' in word:
                masked_index = tokenized_text.index(word)
                predicted_index = torch.argmax(predictions[0, masked_index]).item()
                predicted_token = self.tokenizer.convert_ids_to_tokens([predicted_index])[0]
                predicted_tokens.append(predicted_token)

        return predicted_tokens

    def create_tensors(self, tokenized_text):
        """
        Create the segments tensors.
        """
        # Converts a token string (or a sequence of tokens) in a single integer id (or a sequence of ids),
        indexed_tokens = self.tokenizer.convert_tokens_to_ids(tokenized_text)

        # creates a list of zeros of the length of the tokenized text
        segments_ids = [0] * len(tokenized_text)

        # Convert inputs to PyTorch tensors
        tokens_tensor = torch.tensor([indexed_tokens])
        segments_tensors = torch.tensor([segments_ids])

        return [tokens_tensor, segments_tensors]
