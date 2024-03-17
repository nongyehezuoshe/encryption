# encryption

I use it to encrypt the mnemonic phrases of various cryptocurrencies.

## Usage
```bash
encryption <encrypt/decrypt> <file_path> <password>
```
To use this script, run it from the command line with three arguments: 

1. `encrypt` or `decrypt` to specify the desired action.
2. The path to the file you want to encrypt/decrypt.
3. The password to use for encryption/decryption.

## Example

Linux/Mac:
```bash
./encryption encrypt my-mnemonic-seed mypasswd
```
```bash
./encryption decrypt my-mnemonic-seed.encrypted mypasswd
```

Windows:
```bash
.\encryption.exe encrypt my-mnemonic-seed mypasswd
```
```bash
.\encryption.exe decrypt my-mnemonic-seed.encrypted mypasswd
```
