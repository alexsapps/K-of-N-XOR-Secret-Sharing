# K-of-N XOR Secret Sharing

`K`-of-`N` secret sharing optimized for easy auditability of code.

`K`-of-`N` secret sharing is commonly implemented as [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) which "is an efficient secret sharing algorithm for distributing private information (the "secret") among a group. The secret cannot be revealed unless a quorum of the group acts together to pool their knowledge. To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient number of shares are combined."

However, as of this writing, [trustworthy implementations of Shamir's are lacking](https://www.reddit.com/r/cryptography/comments/1et5hy0/shamirs_secret_sharing_for_common_people/).

Here, instead of using Shamir's, we use XOR for secret sharing because it is much easier for any programmer to audit the code and trust it for their own purposes.

Since XOR requires all shareholders to be present, and we want to account for some being unavailable, this implementation's splitting function generates a *set* of XOR shares for every combination of `K` out of `N` total shareholders (`K<N`). So, for example, any 3 out of 5 shares can recover the secret. (A shareholder is typically a trusted friend or location responsible for maintaining a copy of their share, or in this case, their shares.)

The drawback to this approach is you have to give each shareholder multiple shares to keep track of instead of just one. This should be fine for many use cases because the values are small (assuming the secret is small) and not too numerous (assuming small `N`). For example, with `N=7` shareholders, the worst possible choices of `K` (3 and 4) result in 35 shares per shareholder. For `N=5` and `K` of 2 or 3, we need just 10 shares per shareholder.

Shares are printed out grouped by the intended shareholder for convenient dissemination, and labelled with the set for future reconstruction of the secret. The shareholders are numbered and the sets are labelled by letters of the alphabet.

Thanks [sandassure](https://www.reddit.com/user/sandassure/) (and [Cryptizard](https://www.reddit.com/user/Cryptizard/)) for [the idea](https://www.reddit.com/r/cryptography/comments/1et5hy0/comment/lm3sz9j/), and thanks ChatGPT for the implementation (but not for suggesting a deterministic random function...lol) !

Currently there is support for `K`=3; `N`=5 only.

## Usage

Be sure to [install Python](https://www.google.com/search?q=install+python) if you don't already have it, then download the Python files in this repo and follow the below example.

### Splitting

First, identify `N` stakeholders (e.g. trusted friends or places) and then run the splitting code to obtain codes for each of them:

```
$ python3 ./3of5-XOR-Split.py
Enter the secret to be split: 🔥Secret🔥
Stakeholder 1:
  Set A: 565625aa68fb4c5d293ef46b6982
  Set B: 760c39261e21ba92bd8da198191d
  Set C: f7bd089ab72d68ad5162fefd1a75
  Set D: c975f340d1d38aa6fed82f35e37e
  Set E: 89491092e5bbe2fcf14f18cd28d8
  Set F: 51508f6b3bed424c289d154d12a8

Stakeholder 2:
  Set A: 238dfe8478365cad4e9f54f0fd79
  Set B: 9e5f2002bf221f850fef22214a5e
  Set C: 286d51711870a5128c629e271743
  Set G: 150d54cbfc9c1a61713f41adf900
  Set H: 60c04a94d4e2fbfebbe5135346d4
  Set I: 9a1384ba0d2ebbb1e694a26006f4

Stakeholder 3:
  Set A: 85444f8b43a8738202d55004005e
  Set D: d8554e969b4e75d80b445b3259a9
  Set E: 254db616166434752e03cd513486
  Set G: 72aee438ee4db86ea63870661c77
  Set H: 707d73a6cd77c127f6994bf5c37c
  Set J: 05fc2df450836f1e4a1997bfa212

Stakeholder 4:
  Set B: 18cc8d81f266c665d7167326c7e6
  Set D: e1bf297319f89c0c90e884982e72
  Set F: 17f096c5fa229416b03e48100793
  Set G: 973c245641b4c17db273c15471d2
  Set I: 2df13a4c3e0aeb3050e5038739e3
  Set J: 7d62d0581baf4702f669fbce0652

Stakeholder 5:
  Set C: 2f4fcd4efc38aecdb87490459993
  Set E: 5c9b3221a0bab5fbba38250388fb
  Set F: b63f8d0b92aab528fdd7adc2819e
  Set H: e022ad974af059ab2808a839110d
  Set I: 477d2a53604133f3d3055178abb2
  Set J: 8801690918494b6ed9049cee30e5

$
```

Then disseminate the codes. For example, Stakeholder 1 might be your lockbox at the bank, so you print out the shares and deposit them there. Stakeholder 2 might be your friend, and you might message them using a [privacy focused messaging app](https://www.google.com/search?q=privacy+focused+messaging+app) and tell them "Hey friend, please keep these codes safe in your password manager. I might ask you to give them back to me later, but please make sure it's really me before doing so." 

### Combining

Enter any 3 shares from the same set. To do this, you might obtain the full list of shares from each of 3 shareholders, and then identify the letter that occurs in each of them and use the shares for that set. For example, stakeholders #2, #3 and #5 all have shares for set "H".

```
$ python3 ./3ofN-XOR-combine.py 
Enter 3 shares (hex format) to reconstruct the secret:
Share 1: 60c04a94d4e2fbfebbe5135346d4
Share 2: 707d73a6cd77c127f6994bf5c37c
Share 3: e022ad974af059ab2808a839110d

Reconstructed Secret: 🔥Secret🔥
$
```

## Prompt for Chat GPT to generate this code

Write a python script that prompts the user for a unicode secret and creates 3 shares of it that recreate it when XOR'ed together. Say each share will be for a different trusted person to keep track of called a "shareholder". These shares are related, so let's say they make up one set.

Do this for every combination of 3 out of 5 known shareholders, #1-#5. there are 10 such combinations, so there should be 10 sets. Let's identify sets by A-J.

At the end, print all shares across sets organized by stakeholder:

Stakeholder 1:
Set A:  a048d...
Set B: ...
Set C: ...
...

Stakeholder 2:
...

Please be sure to use a secure random function.

Please also write a separate script file to reconstruct the secret, prompting for any 3 shares generated by the splitting code.

## Privacy and security considerations

It is recommended to download these python files onto your computer and verify their contents yourself before running. You'll have to trust the Python CLI and Python Standard Library of course, but this project contains no 3rd party dependencies and does not require running any build scripts. If concerned about trojan source attacks, consider asking Chat GPT to regenerate the code from the same prompts used here (see ChatGPT link above).

Consider saving a backup of the code so you won't lose the ability to combine your secret in case this code is altered in a backward-incompatible way or removed or made unavailable from its publicly hosted location.

Of course you should run the code only on a device that you trust.

Consider how you will keep the shares secret. Human shareholders are susceptible to social engineering and phishing.

Note that even individual shares reveal the length of your secret.
