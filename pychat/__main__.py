import openai
import os

OPENAI_API_KEY = "OPENAI_API_KEY"


def main():
    print("PyChat v0.1")

    openai_api_key = os.getenv(OPENAI_API_KEY)

    if openai_api_key == None:
        print("OPENAI_API_KEY required")
        exit(-1)

    query = input("Input: ")

    test_input = query.strip()

    if test_input == '':
        print("You did not enter any prompt.")
    else:
        completion = openai.Completion.create(
            engine="text-davinci-003", prompt=query, max_tokens=4000
        )

        if len(completion.choices) == 0:

            print("No output")
        
        else:

            output = completion.choices[0].text

            print("Output: {}".format(output))


if __name__ == "__main__":
    main()
