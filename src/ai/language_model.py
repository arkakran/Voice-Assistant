from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class SimpleLanguageModel:
    def __init__(self, model_name="distilgpt2", logger=None, cache_dir=None):
        self.logger = logger
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)

    def generate_response(self, prompt, max_new_tokens=60):
        """
        Generate a response from the language model using safe parameters.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"], 
            max_new_tokens=max_new_tokens,           
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,                         
            top_p=0.9,
            temperature=0.7
        )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        response = response.strip().split("\n")[0]
        if len(response) > 300:
            response = response[:300] + "..."

        if self.logger:
            self.logger.log_speech(response)

        return response
