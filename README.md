# Gemini API Compass 🧭

[![GitHub stars](https://img.shields.io/github/stars/lostmind008/gemini-api-compass.svg?style=social&label=Star&maxAge=2592000)](https://github.com/lostmind008/gemini-api-compass) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> **Version-specific documentation, error resolution, and integration patterns for Google's Gemini API ecosystem**

## Why This Repository Exists

Using Google's Gemini API should be straightforward, but version changes, inconsistent documentation, and cryptic errors can make development challenging. **Gemini API Compass** provides:

- ✅ **Version-specific documentation** - Know exactly what works in which API version
- ✅ **Error resolution guides** - Clear solutions to common errors with version context
- ✅ **Integration patterns** - Real-world implementation examples beyond simple demos
- ✅ **Migration paths** - Step-by-step guides to upgrade between versions
- ✅ **Cross-API comparisons** - How to translate OpenAI/Anthropic patterns to Gemini

## Quick Start

### Common Error Resolution

```python
# ERROR: TypeError: Part.from_text() takes 1 positional argument but 2 were given

# ❌ INCORRECT (v1beta and later)
parts = [genai_types.Part.from_text(chat_context)]

# ✅ CORRECT (v1beta and later)
parts = [genai_types.Part.from_text(text=chat_context)]
```

### Version-Specific Examples

<details>
<summary>v1beta API Example</summary>

```python
from google import genai
from google.genai import types as genai_types

client = genai.Client(api_key="YOUR_API_KEY")

# v1beta usage for chat
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=[
        genai_types.Content(
            role="user",
            parts=[genai_types.Part.from_text(text="Hello, how are you?")]
        )
    ]
)
print(response.text)
```
</details>

<details>
<summary>v1 API Example</summary>

```python
from google import genai
from google.genai import types as genai_types

client = genai.Client(api_key="YOUR_API_KEY")

# v1 usage for chat
response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents="Hello, how are you?"  # Simple string works in v1
)
print(response.text)
```
</details>

## Repository Structure

```
gemini-api-compass/
├── docs/                      # Documentation organized by topic
│   ├── versions/              # Version-specific information
│   ├── error_catalog/         # Comprehensive error catalog
│   ├── migration_guides/      # Version migration guides
│   └── cross_api/             # Cross-API comparisons
├── examples/                  # Working code examples
│   ├── chat/                  # Chat implementation examples
│   ├── vision/                # Vision API examples
│   ├── function_calling/      # Function calling patterns
│   └── error_handling/        # Error handling strategies
├── anti_patterns/             # Common mistakes to avoid
└── tests/                     # Test helpers and validators
```

## Featured Content

- [Common Error Catalog](docs/error_catalog/README.md) - Solutions to frequent errors
- [Migration Guide: v1beta to v1](docs/migration_guides/beta_to_v1.md) - Upgrading to v1
- [OpenAI to Gemini Migration](docs/cross_api/openai_to_gemini.md) - Transitioning from OpenAI
- [API Version Comparison](docs/versions/version_comparison.md) - Feature & parameter differences
- [Error Handling Patterns](examples/error_handling/README.md) - Best practices

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Types of contributions needed:
- Error reports with solutions
- Version-specific examples
- Migration experiences
- Cross-API comparisons
- Documentation improvements

## License

MIT - See [LICENSE](LICENSE) for details.

## Acknowledgements

This project is not officially affiliated with Google. Gemini, and the Gemini API are trademarks of Google LLC.