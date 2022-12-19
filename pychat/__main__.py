import openai
import os
from argparse import ArgumentParser

OPEN_API_KEY = "OPENAI_API_KEY"


def main():

    # Parameterizing arguments from the command line
    parser = ArgumentParser(description="Pychat v0.1")
    # max-tokens is the flag
    parser.add_argument(
        "--max-tokens", help="Maximum size of tokes used", type=int, default=4000
    )
    # flag for engine
    parser.add_argument(
        "--engine",
        help="The openai engine to use",
        type=str,
        default="text-davinci-003",
    )

    # flag for query from user
    parser.add_argument(
        "--query", help="A string input from the user", type=str, required=True
    )

    # parsing the arguments

    args = parser.parse_args()

    max_tokens = args.max_tokens
    engine = args.engine
    query = args.query

    print("Options:")
    print(f"Max tokens: {max_tokens}")
    print(f"Engine: {engine}")

    open_ai_api_key = os.getenv(OPEN_API_KEY)

    if open_ai_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    query = query.strip()

    while True:
        if query.lower() == "quit":
            print("\nGoodbye! Come again anytime.")
            break
        elif query == "":
            print("You did not ask me anything.")
            query = input("You (type 'quit' to exit): \n")
        else:
            completion = openai.Completion.create(
                engine=engine, prompt=query, max_tokens=max_tokens
            )

            if len(completion.choices) == 0:
                print("No output")
            else:
                output = completion.choices[0].text
                print(f"AI: {output.strip()}")

            query = input("\nYou (type 'quit' to exit): \n")
            query = query.strip()


if __name__ == "__main__":
    main()
