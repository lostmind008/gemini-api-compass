"""
Example demonstrating the "TypeError: Part.from_text() takes 1 positional argument but 2 were given" error.

This code shows:
1. The common error and its cause
2. The correct way to fix it
3. A version-compatible approach

Usage:
    python part_from_text_error.py
"""

from google import genai
from google.genai import types as genai_types

# Replace with your actual API key
API_KEY = "YOUR_API_KEY"

def demonstrate_error():
    """
    This function attempts to use Part.from_text() incorrectly,
    which will trigger the TypeError in v1beta+ of the API.
    
    You can uncomment to see the error.
    """
    client = genai.Client(api_key=API_KEY)
    
    try:
        # ❌ INCORRECT: Using positional parameter
        # Will raise: TypeError: Part.from_text() takes 1 positional argument but 2 were given
        content = genai_types.Content(
            role="user",
            parts=[genai_types.Part.from_text("Hello, how are you?")]
        )
        
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=[content]
        )
        
        print("Response:", response.text)
        
    except TypeError as e:
        print(f"ERROR: {e}")
        print("This error occurs when using Part.from_text() with a positional parameter.")
        print("See the correct usage below.")
        print("-" * 50)


def correct_usage():
    """
    This function shows the correct way to use Part.from_text()
    with the named parameter 'text='
    """
    client = genai.Client(api_key=API_KEY)
    
    # ✅ CORRECT: Using named parameter
    content = genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text="Hello, how are you?")]
    )
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=[content]
        )
        
        print("CORRECT USAGE:")
        print("content = genai_types.Content(")
        print("    role=\"user\",")
        print("    parts=[genai_types.Part.from_text(text=\"Hello, how are you?\")]")
        print(")")
        print("\nResponse would be processed successfully.")
        
    except Exception as e:
        # This should not happen with correct usage, but handling just in case
        print(f"Unexpected error: {e}")


def version_compatible_approach():
    """
    This function demonstrates a version-compatible approach that works
    regardless of the API version.
    """
    print("\nVERSION-COMPATIBLE APPROACH:")
    print("This approach will work with all versions of the API:")
    print("""
# Define a helper function for creating content
def create_user_content(text):
    return genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text=text)]
    )

# Then use it in your code
content = create_user_content("Hello, how are you?")
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[content]
)
    """)


if __name__ == "__main__":
    print("=== GEMINI API PART.FROM_TEXT() ERROR DEMONSTRATION ===\n")
    
    # Comment this out if you don't want to see the error
    demonstrate_error()
    
    correct_usage()
    version_compatible_approach()
    
    print("\n=== END OF DEMONSTRATION ===")