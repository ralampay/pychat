import openai
import os
import argparse

OPENAI_API_KEY = "OPENAI_API_KEY"


def main():
    parser = argparse.ArgumentParser(description="PyChat v0.1")
    
    parser.add_argument("--max-tokens", help="Maximum size of tokens to be used", type=int, default=4000)
    parser.add_argument("--engine", help="The openai engine to use", type=str, default="text-davinci-003")
    parser.add_argument("--query", help="Checking for user input", type=str, default="Greet me")

    args = parser.parse_args()

    max_tokens  = args.max_tokens
    engine      = args.engine
    query       = args.query

    print("\nOptions: ")
    print(f"max_tokens: {max_tokens}")
    print(f"engine: {engine}")

    openai_api_key = os.getenv(OPENAI_API_KEY)

    if openai_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    query = query.strip()

    while True:
        if query.lower() == 'quit':
            print("Thank you for using PyChat!")
            break
        elif query == '':
            print("You did not enter any prompt.")
            query = input("Please enter a prompt: ")
        else:
            completion = openai.Completion.create(
                engine="text-davinci-003", prompt=query, max_tokens=max_tokens
            )

            if len(completion.choices) == 0:
                print("No output")
            else:
                output = completion.choices[0].text
                print(format(output))

            query = input("Prompt [or type 'quit' to exit]: ")
            query = query.strip()

if __name__ == "__main__":
    main()
