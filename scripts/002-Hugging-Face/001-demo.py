
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# These classes are used for working with GPT-2 models and tokenizing text.


# initialize a GPT-2 model and tokenizer
model_name = "gpt2-medium"  # You can also use, "gpt2-large", or "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt = "Hello linkedin! I am a data scientist and I am excited to share my latest project with you."
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate( input_ids, 
                        max_length=50, 
                        num_return_sequences=3, 
                        temperature=0.7, 
                        pad_token_id=tokenizer.eos_token_id, 
                        do_sample=True
                        )

# Decode generated text
generated_text = [tokenizer.decode(ids, skip_special_tokens=True) for ids in output]
for text in generated_text:
    print(text)


