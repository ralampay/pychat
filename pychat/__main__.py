# TODO:
# 1. Handle detection of OPENAI_API_KEY availability
# 2. max_tokens can be set as a parameter outside with a default value of 4000
# 3. Empty input from user. Suggested to use try except
# 4. engine can be set as a paremter with a default of 'text-davinci-003'
# 5. choices should be checked if we actually have values

# Additional Features:
# 1. Put code in while loop so you won't have to rerun the program

import openai

def main():
    print("PyChat v0.1")
    query = input('Input: ')

    completion = openai.Completion.create(engine='text-davinci-003', prompt=query, max_tokens=4000)

    output = completion.choices[0].text

    print("Output: {}".format(output))

if __name__ == '__main__':
    main()
