class AiModel(object):
    """
    This is a base class for all ai models.
    """
    model_pipeline = None
    model_tokenizer = None
    model_config = None

    def submit_data(self):
        pass

    def process_config(self):
        pass



