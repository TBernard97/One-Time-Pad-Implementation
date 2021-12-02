# One Time Pad Implementation

![dank meme](/Screenshots/required_meme.jpg)

Implementation of the one-time-pad algorithm. 

Following constraints ensure requirements are satisified.

- Keys are randomly generated using the token_hex function from the [secrets](https://docs.python.org/3/library/secrets.html) library. 
- Keys are written to file to ensure key is not reused.
- Because token_hex is a length doubling PRG, half the message length is used to ensure key is the same length as message (makes encryption easy).

It is up to the user to decide how the key and message is transmitted.

# Requirements

- [python3](https://www.python.org/downloads/)
- pip3 (Usually comes with python3)

# Installation 

To install run the following command within the project directory.

```bash
pip3 install -r requirements.txt
```

# Usage

```
usage: otp.py [-h] [--encrypt ENCRYPT] [--decrypt DECRYPT] [--key KEY]

optional arguments:
  -h, --help         show this help message and exit
  --encrypt ENCRYPT  Encrypt a message. Key generated randomly.
  --decrypt DECRYPT  Decrypt a message. Requires key.
  --key KEY          Key used for decryption. Requires ciphertext.
```

## Encrypting a message

To encrypt a message simply use the `--encrypt` flag with the message. Program will output encrypted text and key.

```bash
python3 --encrypt [MESSAGE]
```

![encryption](/Screenshots/encryption.png)


## Decrypting a message

To encrypt a message simply use the `--decrypt` and `--key` flags with the ciphertext and key, respectively. Program will output decrypted message.


```bash
python3 --decrypt [CIPHERTEXT] --key [KEY]
```


![decryption](/Screenshots/decryption.png)
