# Gemini API Version Comparison

This document provides a comprehensive comparison of different Gemini API versions, highlighting key differences, breaking changes, and compatibility concerns.

## Version Overview

| Version | Release | Status | Key Features |
|---------|---------|--------|--------------|
| v1      | Current | Stable | All core functionality, stable interfaces |
| v1beta  | Legacy  | Maintained | Experimental features, some parameter differences |
| v1alpha | Experimental | Changing | Preview features, unstable interfaces |

## Breaking Changes Between Versions

### v1beta → v1

| Feature | v1beta Behavior | v1 Behavior | Migration Notes |
|---------|----------------|-------------|----------------|
| Content creation | Requires structured Content objects | Accepts simple strings | v1 is more permissive, but structured Content still works |
| `Part.from_text()` | Requires named param `text=` | Requires named param `text=` | Consistent between versions |
| Response handling | Complex response structure | Simplified access via `.text` | Both approaches work in v1 |
| Error handling | More specific errors | More general errors | May need to adjust error handling |
| Streaming | Different interface | Simplified interface | See streaming examples for migration |

### Key API Differences

#### Content Creation 

**v1beta (Strict Format)**:
```python
# v1beta approach (VERBOSE)
contents = [
    genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text="What is machine learning?")]
    )
]
```

**v1 (Flexible Format)**:
```python
# v1 approach (SIMPLE)
contents = "What is machine learning?"

# v1 also supports the v1beta approach
contents = [
    genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text="What is machine learning?")]
    )
]
```

#### Response Handling

**v1beta (Complex Navigation)**:
```python
# v1beta approach
response = client.models.generate_content(
    model="gemini-1.5-pro", 
    contents=contents
)
text = response.candidates[0].content.parts[0].text
```

**v1 (Simplified Access)**:
```python
# v1 approach
response = client.models.generate_content(
    model="gemini-1.5-pro", 
    contents=contents
)
text = response.text  # Helper property
```

#### Configuration Objects

**v1beta (Limited Options)**:
```python
# v1beta approach
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=contents,
    generation_config={
        "temperature": 0.7,
        "max_output_tokens": 1024
    }
)
```

**v1 (Enhanced Options)**:
```python
# v1 approach
config = genai_types.GenerateContentConfig(
    temperature=0.7,
    max_output_tokens=1024,
    top_p=0.95,
    top_k=40
)

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=contents,
    config=config
)
```

## Feature Availability by Version

| Feature | v1alpha | v1beta | v1 | Notes |
|---------|---------|--------|-----|-------|
| Text generation | ✅ | ✅ | ✅ | Core feature |
| Image input | ✅ | ✅ | ✅ | All versions |
| Video input | ✅ | ❌ | ✅ | Not in v1beta |
| Function calling | ✅ | ❌ | ✅ | Not in v1beta |
| Streaming responses | ✅ | ✅ | ✅ | Interface differences |
| Multi-turn chat | ✅ | ✅ | ✅ | All versions |
| System instructions | ✅ | ❌ | ✅ | Not in v1beta |
| Token counting | ❌ | ❌ | ✅ | Only in v1 |

## Common Compatibility Issues

### Parameter Name Changes

| v1beta Parameter | v1 Parameter | Notes |
|-----------------|--------------|-------|
| `safety_settings` | `safety_settings` | Unchanged but structure differs |
| `generation_config` | `config` | Different object type |
| N/A | `stream` | New in v1 |

### Method Signature Changes

| Method | v1beta Signature | v1 Signature | Notes |
|--------|-----------------|--------------|-------|
| `generate_content` | `(model, contents, generation_config)` | `(model, contents, config, stream)` | Parameter renaming |
| `count_tokens` | N/A | `(model, contents)` | New in v1 |

## Version Detection

You can detect which version of the API you're using to implement version-specific code:

```python
from google import genai
import inspect

def detect_genai_version():
    """Detect the version of google-genai library."""
    # Check if count_tokens method exists (v1 feature)
    if hasattr(genai.Client.models, 'count_tokens'):
        return "v1"
    
    # Check parameter names in generate_content
    params = inspect.signature(genai.Client.models.generate_content).parameters
    if 'config' in params:
        return "v1"
    elif 'generation_config' in params:
        return "v1beta"
    
    return "unknown"

# Usage
version = detect_genai_version()
print(f"Using google-genai {version}")
```

## Recommended Approach for Version Compatibility

To write code that works across versions:

1. **Use v1beta style Content creation** - The more explicit approach works in both versions
2. **Use named parameters everywhere** - Avoid positional arguments when possible
3. **Implement version detection** - Use conditional code for version-specific features
4. **Handle both response styles** - Check for `.text` first, then fall back to navigating the response object

Example of version-compatible code:

```python
from google import genai
from google.genai import types as genai_types

# Initialize client
client = genai.Client(api_key="YOUR_API_KEY")

# Create content in v1beta style (works in both v1beta and v1)
contents = [
    genai_types.Content(
        role="user",
        parts=[genai_types.Part.from_text(text="Tell me a joke about programming")]
    )
]

# Detect if we're using v1 or v1beta for config
if hasattr(genai_types, 'GenerateContentConfig'):
    # v1 approach
    config = genai_types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1024
    )
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=contents,
        config=config
    )
else:
    # v1beta approach
    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=contents,
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 1024
        }
    )

# Extract text in a version-compatible way
if hasattr(response, 'text'):
    # v1 approach
    text = response.text
else:
    # v1beta approach
    text = response.candidates[0].content.parts[0].text if response.candidates else ""

print(text)
```

## Further Reading

- [Official API Version Documentation](https://ai.google.dev/gemini-api/docs/api-versions)
- [Migration Guide: v1beta to v1](../migration_guides/beta_to_v1.md)
- [Error Catalog](../error_catalog/README.md)