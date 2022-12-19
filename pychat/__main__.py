import openai
import os
import argparse

OPENAI_API_KEY = "OPENAI_API_KEY"


def main():
    parser = argparse.ArgumentParser(description="PyChat v0.1")

    parser.add_argument("--max-tokens", help="Maximum size of tokens to be used", type=int, default=4000)
    parser.add_argument("--engine", help="The openai engine to use", type=str, default='text-davinci-003')
    parser.add_argument("--query", help="Provide user input", type=str, required=True)

    args = parser.parse_args()

    max_tokens  = args.max_tokens
    engine      = args.engine
    query       = args.query

    print("Options:")
    print("max_tokens: {}".format(max_tokens))
    print("engine: {}".format(engine))
    #print("query: {}".format(query))

    openai_api_key = os.getenv(OPENAI_API_KEY)

    if openai_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    #query = input("Input: ")

    while(query != 'quit'):
        test_input = query.strip()

        if test_input == '':
            print("You did not enter any prompt.")
        else:
            completion = openai.Completion.create(
                engine=engine, prompt=query, max_tokens=max_tokens
            )

            if len(completion.choices) == 0:

                print("No output")
            
            else:

                output = completion.choices[0].text

                print("Output: {}".format(output))
        
        print('-'*70)
        query = input('\nInput: ')


if __name__ == "__main__":
    main()
