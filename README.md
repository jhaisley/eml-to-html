# Enhanced EML to HTML Converter

A comprehensive CLI tool that transforms `.eml` email files into readable `.html` files, now featuring recursive directory processing and database conversion for complete email account preservation.

## Features
- **EML to HTML Conversion**: Quickly convert single or multiple `.eml` files to `.html`.
- **Recursive Directory Processing**: Use the `-r` flag to process all `.eml` files within a directory, including nested directories.
- **DB to HTML Conversion**: Specifically catered for email backups (e.g., from GYB) stored in a `msg-db.sqlite` database, allowing direct conversion to `.html`.

## Usage
Basic usage:
```
eml-to-html [EML FILE]...
```

For multiple files or using a _glob_:
```
eml-to-html example1.eml example2.eml
eml-to-html *.eml
```

To recursively process directories:
```
eml-to-html -r [DIRECTORY]
```
This option intelligently skips existing files, facilitating incremental conversions.

### DB to HTML Conversion
For converting email databases:
```
db-to-html [DB FILE]
```
Optionally, specify an output file:
```
db-to-html [DB FILE] [OUTPUT FILE]
```

## Example

### EML to HTML
```
$ eml-to-html test_emails/*.eml
 Written: `test_email_1.html`
 Written: `test_email_2.html`
```

### DB to HTML
```
$ db-to-html msg-db.sqlite
 Processed: `msg-db.sqlite` into HTML files.
```

## About
The Enhanced EML to HTML Converter is developed by Jordan Haisley, building upon the original micro module crafted by [Jeroen Overschie](https://jeroenoverschie.nl/) in 2022. This version introduces advanced functionalities—recursive directory processing and database conversion—to meet the evolving needs for comprehensive email data processing and preservation.

For more information, updates, or to contribute, please visit the [GitHub repository](https://github.com/jhaisley/eml-to-html).

Your feedback and contributions are always welcomed as we aim to make email data management easier and more accessible for everyone.
