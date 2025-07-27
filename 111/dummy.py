import os

OUTPUT_FILE = "merged_output.txt"

def is_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except Exception:
        return False

def collect_and_merge_files(base_dir='.'):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_file:
        for root, _, files in os.walk(base_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                rel_path = os.path.relpath(file_path, base_dir)

                if file_path == OUTPUT_FILE:
                    continue  # skip the output file itself

                if is_text_file(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception as e:
                        content = f"[Could not read file: {e}]"
                else:
                    content = "[Binary or unreadable file]"

                out_file.write(f"\n--- {rel_path} ---\n")
                out_file.write(content)
                out_file.write("\n\n")  # extra spacing between files

    return os.path.abspath(OUTPUT_FILE)

def main():
    merged_file_path = collect_and_merge_files()
    print(f"✅ All files merged into: {merged_file_path}")

if __name__ == "__main__":
    main()
