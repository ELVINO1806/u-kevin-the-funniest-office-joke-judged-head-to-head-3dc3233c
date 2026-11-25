import os

ENTRY = "IT reset my password to 'Password123'. I changed it to 'Password123!' and now I am the company's entire security policy."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
