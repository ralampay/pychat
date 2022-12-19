import openai
import os
import argparse

OPENAI_API_KEY = "OPENAI_API_KEY"

def main():
    global query
    global max_tokens

    parser = argparse.ArgumentParser(description="PyChat v0.1")
    
    parser.add_argument("--max-tokens", help="Maximum size of tokens to be used", type=int, default=4000)
    parser.add_argument("--engine", help="The openai engine to use", type=str, default="text-davinci-003")
    parser.add_argument("--query", help="Checking for user input", type=str, default="write a conversational greetings and then ask how you can help")

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

    # put line34 in comment as there's already an assigned default 'query' value
    # query = query.strip()

    o_quit = False
    # while True:
    while not o_quit:

        open_ai(query)
        query = input("User Input: [or type 'quit' to exit]: ")
        query = query.strip()

        if query.lower() == 'quit':
            query = "give a closing statement to a user"
            open_ai(query)
            o_quit = True
            break

        elif query == '':
            query = "write a reply that an input was not found or maybe the customer did not provide one and ask to re-enter how can I help"


def open_ai(query):
        completion = openai.Completion.create(
            engine="text-davinci-003", prompt=query, max_tokens=max_tokens
        )

        if len(completion.choices) == 0:
            print("No output")
        else:
            output = completion.choices[0].text
            print("ai response: ", format(output))

if __name__ == "__main__":
    main()
