# Parameter Errors in Gemini API

This document catalogs common parameter-related errors you might encounter when using the Google Gemini API, organized by error type and API version.

## TypeError: Part.from_text() takes 1 positional argument but 2 were given

### Error Message

```
TypeError: Part.from_text() takes 1 positional argument but 2 were given
```

### Affected Versions

- ✅ google-genai 0.2.0+

### Not Affected

- ❌ Earlier versions might have had different behavior

### Cause

This error occurs when using the `Part.from_text()` method without named parameters. In newer versions of the `google-genai` library, the method signature requires using a named parameter `text=` instead of a positional parameter.

### Code That Triggers The Error

```python
from google import genai
from google.genai import types as genai_types

# ❌ INCORRECT: Using positional parameter
content = genai_types.Content(
    role="user",
    parts=[genai_types.Part.from_text("Hello, how are you?")]
)
```

### Solution

Use the named parameter `text=` when calling `Part.from_text()`:

```python
from google import genai
from google.genai import types as genai_types

# ✅ CORRECT: Using named parameter
content = genai_types.Content(
    role="user",
    parts=[genai_types.Part.from_text(text="Hello, how are you?")]
)
```

### Common Contexts

This error frequently appears in:

1. Chat applications where you're building a conversation history
2. Interactive applications that maintain conversation state
3. Applications migrated from older versions of the Gemini API
4. Code examples copied from outdated tutorials

### Related Documentation

- [Google GenAI Python SDK Reference](https://googleapis.github.io/python-genai/)
- [Content Creation Guide](https://ai.google.dev/gemini-api/docs/prompting-with-multimedia)

---

## ValueError: Content must contain at least one part

### Error Message

```
ValueError: Content must contain at least one part
```

### Affected Versions

- ✅ google-genai 0.1.0+

### Cause

This error occurs when creating a `Content` object with an empty `parts` list. The Google Gemini API requires that each Content object contains at least one Part.

### Code That Triggers The Error

```python
from google import genai
from google.genai import types as genai_types

# ❌ INCORRECT: Empty parts list
content = genai_types.Content(
    role="user",
    parts=[]
)
```

### Solution

Ensure that the `parts` list contains at least one item:

```python
from google import genai
from google.genai import types as genai_types

# ✅ CORRECT: Parts list with at least one item
content = genai_types.Content(
    role="user",
    parts=[genai_types.Part.from_text(text="Hello")]
)
```

### Common Contexts

This error typically appears when:

1. Dynamically generating content where the source might be empty
2. Building chat interfaces where user input could be empty
3. Error handling code that doesn't check for empty responses

---

## Additional Parameter Errors

> This section will be expanded with more parameter-related errors as they are encountered and documented by contributors.

- TypeError: generate_content() got an unexpected keyword argument
- ValueError: Model parameter missing
- TypeError: Expected string, got dict
- ValueError: Invalid role (must be one of 'user', 'model', 'system')