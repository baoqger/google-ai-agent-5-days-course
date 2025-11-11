def merge_and_label_dialogue(input_file, output_file):
    merged_lines = []
    current_sentence = ""
    speaker_turn = 0  # 0 for Person A, 1 for Person B

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">>"):
                # Save previous sentence if exists
                if current_sentence:
                    prefix = "Person A:" if speaker_turn == 0 else "Person B:"
                    merged_lines.append(f"{prefix} {current_sentence.strip()}")
                    speaker_turn = 1 - speaker_turn  # Alternate speaker

                # Start new sentence, remove ">>"
                current_sentence = line[2:].strip()
            else:
                # Continuation of current sentence
                current_sentence += " " + line

        # Append last sentence
        if current_sentence:
            prefix = "Person A:" if speaker_turn == 0 else "Person B:"
            merged_lines.append(f"{prefix} {current_sentence.strip()}")

    with open(output_file, 'w', encoding='utf-8') as f_out:
        for sentence in merged_lines:
            f_out.write(sentence + "\n")

    print(f"Merged {len(merged_lines)} dialogue turns saved to {output_file}")


# Example usage:
input_path = "original-subtitles.txt"    # Replace with your input file path
output_path = "output.txt"  # Replace with your desired output file path
merge_and_label_dialogue(input_path, output_path)