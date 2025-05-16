# Contributing to Gemini API Compass

First off, thank you for considering contributing to Gemini API Compass! This project exists to help developers navigate the complexities of Google's Gemini API, and your experiences are invaluable to that mission.

## How Can I Contribute?

### Reporting Errors You've Encountered

Have you run into an error with the Gemini API? Share it to help others!

**Error Reports** should include:
- The complete error message and stack trace
- The version of `google-genai` and other relevant libraries
- Code that reproduces the error (minimum working example)
- Your solution or workaround
- Any relevant context (e.g., "This only happens with vision models")

Use the **Error Report Template** when creating an issue.

### Adding Version-Specific Documentation

Did you notice differences between API versions? Help document them!

**Version Documentation** should include:
- Clear indication of which API version(s) you're documenting
- Code examples showing version-specific behavior
- Any parameter differences or behavior changes
- Migration hints for developers upgrading versions

### Sharing Integration Patterns

Have you built something with Gemini API? Share your patterns!

**Integration Patterns** should include:
- Complete, working code examples
- Explanation of the integration approach
- Version compatibility information
- Alternative approaches or trade-offs
- Error handling considerations

### Improving Existing Documentation

Found an issue in our docs? Help us fix it!

**Documentation Improvements** could be:
- Clarity improvements
- Additional examples
- Correction of errors
- Better organization
- Addition of missing information

## Pull Request Process

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Create a new Pull Request

## Style Guide

### Documentation

- Use Markdown for all documentation
- Include version information prominently
- Organize content with clear headings
- Include working code examples when relevant
- Use syntax highlighting for code blocks

### Code Examples

- Include complete imports
- Use meaningful variable names
- Include comments for complex logic
- Demonstrate proper error handling
- Test examples before submitting

## Adding a New Error to the Catalog

1. Identify the appropriate category for the error (e.g., authentication, parameters, etc.)
2. Use the error template structure found in existing catalog entries
3. Include:
   - Full error message
   - Affected versions
   - Root cause explanation
   - Solution with code example
   - Context in which the error commonly occurs

## Issue Templates

### Error Report Template

```markdown
## Error Description

[Describe the error you encountered]

## Error Message

```
[Paste the full error message and stack trace here]
```

## Environment

- google-genai version: [version]
- Python version: [version]
- OS: [OS name and version]

## Reproduction Steps

```python
# Code to reproduce the error
```

## Solution

```python
# Your solution or workaround
```

## Additional Context

[Any additional information that might be helpful]
```

### Documentation Improvement Template

```markdown
## Current Documentation Problem

[Describe what's missing, unclear, or incorrect]

## Location

[Link to the file that needs improvement]

## Suggested Improvement

[Your suggested changes]

## Additional Context

[Any additional information that might be helpful]
```

## Community Guidelines

- Be respectful and inclusive
- Assume good intentions
- Focus on the improvement, not the person
- Give credit where credit is due
- Help others learn, don't just correct them

Thank you for your contributions to making Gemini API development easier for everyone!