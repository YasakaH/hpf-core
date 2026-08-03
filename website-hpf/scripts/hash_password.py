import hashlib
import sys

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python hash_password.py <password>")
        sys.exit(1)
    print(hashlib.sha256(sys.argv[1].encode("utf-8")).hexdigest())

if __name__ == "__main__":
    main()
