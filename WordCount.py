#WordCount.py
#Name: Rinku Mahato
#Date: 02/28/2026
#Assignment: Word Count

def main():
    filename = input("Enter file name: ").strip()
    # gettysberg.txt
    # fish.txt

    try:
        with open(filename, 'r') as myfile:
            line_count = 0
            word_count = 0
            char_count = 0

            for line in myfile:
                # Count Lines: count of newline-terminated lines
                char_count += len(line)

                # Count words to each line using split()
                word_count += len(line.split())

                # Count total characters- including spaces/newlines
                if line.endswith("\n"):
                    line_count += 1

        # Output results
        print("Lines:", line_count)
        print("words:", word_count)
        print("characters:", char_count)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == '__main__':
  main()