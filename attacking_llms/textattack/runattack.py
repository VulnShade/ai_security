# 1. Takes our AI model that understands positive/negative text
# 2. Tries to change words in the text to confuse the AI
#    For example: changing “great movie” to “okay movie”
# 3. Keeps track of:
#   - Which attacks worked (AI was fooled)
#   - Which attacks failed (AI wasn’t fooled)
#   - How many words were changed
# 4. Saves all results to files we can look at later

from textattack.attack_recipes import TextFoolerJin2019
from textattack import Attacker, AttackArgs
from textattack.datasets import Dataset
from transformers import pipeline
from textattack.models.wrappers import ModelWrapper
import torch
from textattack.attack_results import SuccessfulAttackResult, FailedAttackResult

class SentimentWrapper(ModelWrapper):
    def __init__(self):
        self.model = pipeline('sentiment-analysis')

    def __call__(self, text_inputs):
        outputs = []
        for text in text_inputs:
            result = self.model(text)[0]
            if result['label'] == 'POSITIVE':
                probs = [0.0, float(result['score'])]
            else:
                probs = [float(result['score']), 0.0]
            outputs.append(probs)
        return torch.tensor(outputs)

def analyze_result(result):
    """Analyze a single attack result"""
    if isinstance(result, SuccessfulAttackResult):
        # Get the text strings
        original = str(result.original_result.attacked_text)
        perturbed = str(result.perturbed_result.attacked_text)

        # Calculate word changes
        orig_words = set(original.split())
        pert_words = set(perturbed.split())
        words_changed = len(orig_words.symmetric_difference(pert_words))

        return {
            'success': True,
            'original_text': original,
            'perturbed_text': perturbed,
            'words_changed': words_changed
        }
    else:
        return {
            'success': False,
            'original_text': str(result.original_result.attacked_text)
        }

def main():
    print("Initializing model wrapper...")
    model_wrapper = SentimentWrapper()

    # Create dataset
    examples = [
        ("This movie is great and amazing!", 1),
        ("This was a terrible waste of time.", 0),
        ("I really enjoyed watching this film.", 1),
        ("The worst movie I've ever seen.", 0)
    ]

    dataset = Dataset(examples)

    print("Creating attack...")
    attack = TextFoolerJin2019.build(model_wrapper)

    print("Setting up attack arguments...")
    attack_args = AttackArgs(
        num_examples=4,
        log_to_csv="attack_results.csv",
        checkpoint_interval=2,
        disable_stdout=False)

    print("Starting attack...")
    attacker = Attacker(attack, dataset, attack_args)
    results = attacker.attack_dataset()

    # Analyze results
    analyzed_results = [analyze_result(r) for r in results]

    # Count successes and failures
    successful = sum(1 for r in analyzed_results if r['success'])
    failed = sum(1 for r in analyzed_results if not r['success'])

    print("\nCustom Attack Results Summary:")
    print("-" * 50)
    print(f"Number of successful attacks: {successful}")
    print(f"Number of failed attacks: {failed}")
    print(f"Success rate: {(successful/len(results)):.2%}")

    print("\nDetailed Results:")
    print("-" * 50)
    for i, result in enumerate(analyzed_results, 1):
        print(f"\nExample {i}:")
        print(f"Original text: {result['original_text']}")
        if result['success']:
            print(f"Perturbed text: {result['perturbed_text']}")
            print(f"Words changed: {result['words_changed']}")
            print(f"Modification rate: {result['words_changed']/len(result['original_text'].split()):.2%}")
        else:
            print("Attack failed")
        print("-" * 30)

    # Save results to file
    with open("detailed_results.txt", "w") as f:
        f.write("Attack Results Summary\n")
        f.write("-" * 50 + "\n")
        f.write(f"Number of successful attacks: {successful}\n")
        f.write(f"Number of failed attacks: {failed}\n")
        f.write(f"Success rate: {(successful/len(results)):.2%}\n\n")

        f.write("Detailed Results\n")
        f.write("-" * 50 + "\n")
        for i, result in enumerate(analyzed_results, 1):
            f.write(f"\nExample {i}:\n")
            f.write(f"Original text: {result['original_text']}\n")
            if result['success']:
                f.write(f"Perturbed text: {result['perturbed_text']}\n")
                f.write(f"Words changed: {result['words_changed']}\n")
                f.write(f"Modification rate: {result['words_changed']/len(result['original_text'].split()):.2%}\n")
            else:
                f.write("Attack failed\n")
            f.write("-" * 30 + "\n")

if __name__ == "__main__":
    main()
