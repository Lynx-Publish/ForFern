import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import snapshot_download
import os

# Define the local directory for model storage
MODEL_REPO = "numind/NuExtract-tiny-v1.5"
MODEL_DIR = "./nuextract_model"

# Download the model if not already present
if not os.path.exists(MODEL_DIR):
    print("Downloading NuExtract-tiny model...")
    snapshot_download(repo_id=MODEL_REPO, local_dir=MODEL_DIR, local_dir_use_symlinks=False)
    print("Download complete.")

# Load model and tokenizer
print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForCausalLM.from_pretrained(MODEL_DIR)

# Simple command input loop
def extract_info(input_text):
    prompt = f"""
Extract the following information from the text:
Text: "{input_text}"
Return as JSON:
{{
  "Place the object is supposed to move to": "",
  "The object asked to be moved": ""
}}
"""

    # Tokenize and run generation
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=256, pad_token_id=tokenizer.eos_token_id)

    # Decode result
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("\nExtraction Result:")
    print(result.strip())

# Run loop
if __name__ == "__main__":
    print("NuExtract Assistant Ready. Type a command to extract structured info.")
    while True:
        text = input("\nEnter a command (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        extract_info(text)
