import os

def main():
    # Attempt to retrieve the secret from the environment
    api_secret = os.getenv('MY_SUPER_SECRET_KEY')

    if api_secret:
        print("✅ Success: Secret retrieved from the environment!")
        # In a real app, you'd use the secret here
        print(f"The first two characters of your secret are: {api_secret[:2]}***")
    else:
        print("❌ Error: No secret found. Did you forget to set the environment variable?")

if __name__ == "__main__":
    main()
