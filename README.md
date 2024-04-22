# eml-to-html

Tiny CLI tool that converts `.eml` email files to `.html` files.

## Installation
```
pip install eml-to-html
```

## Usage
```
eml-to-html [EML FILE]...
```

Feel free to pass a _glob_. For example:

```
eml-to-html some_email_file_1.eml some_email_file_2.eml
```

and

```
eml-to-html *.eml
```

are both valid calls to the command. Cheers!

Additionally, you can use -r to recurse directories.
```
eml-to-html -r [DIRNAME] or *
```
Will run recursivly.  
This option also skips creating a file if it already exists to allow for incremental conversions.

## db-to-html
db-to-html is a companion to eml-to-html as some email backups, such as GYB will create a msg-db.sqlite database.
```
db-to-html [DB FILE]
```
or 
```
db-to-html [DB FILE] [OUTPUT FILE]
```
Both work fine.

## Example

Running `eml-to-html` on the [`test_emails`](https://github.com/dunnkers/eml-to-html/tree/master/test_emails) folder:

```
$ eml-to-html test_emails/*.eml
🟢 Written `test_email_1.html`
🟢 Written `test_email_2.html`
```

File tree is now:

```
$ tree test_emails 
test_emails
├── test_email_1.eml
├── test_email_1.html
├── test_email_2.eml
└── test_email_2.html

0 directories, 4 files
```

## About
The original eml-to-html micro module was written by [Jeroen Overschie](https://jeroenoverschie.nl/) in 2022.

This version of eml-to-html contains enhancements and features not present in the original micro module, and 
aims to be a more feature-complee utility.  This version is currently maintained by Jordan Haisley
