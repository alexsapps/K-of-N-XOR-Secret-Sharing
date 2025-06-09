# K-of-N XOR Secret Sharing

`K`-of-`N` secret sharing optimized for easy auditability of code.

`K`-of-`N` secret sharing is commonly implemented as [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing) which "is an efficient secret sharing algorithm for distributing private information (the "secret") among a group. The secret cannot be revealed unless a quorum of the group acts together to pool their knowledge. To achieve this, the secret is mathematically divided into parts (the "shares") from which the secret can be reassembled only when a sufficient number of shares are combined."

However, as of this writing, [trustworthy implementations of Shamir's are lacking](https://www.reddit.com/r/cryptography/comments/1et5hy0/shamirs_secret_sharing_for_common_people/).

Here, instead of using Shamir's, we use XOR for secret sharing because it is much easier for any programmer to audit the code and trust it for their own purposes.

Since XOR requires all shares to be present, and we want to account for some being unavailable, this implementation's splitting function generates a *set* of XOR shares for every combination of `K` out of `N` total shareholders (`K<N`). So, for example, any 3 out of 5 shares can recover the secret. (A shareholder is typically a trusted friend or location responsible for maintaining a copy of their share, or in this case, their shares.)

The drawback to this approach is you have to give each shareholder multiple shares to keep track of instead of just one. This should be fine for many use cases because the values are small (assuming the secret is small) and not too numerous (assuming small `N`). For example, with `N=7` shareholders, the worst possible choices of `K` (3 and 4) result in 35 shares per shareholder. For `N=5` and `K` of 2 or 3, we need just 10 shares per shareholder.

Shares are printed out grouped by the intended shareholder for convenient dissemination, and labelled with the set for future reconstruction of the secret. The shareholders are numbered and the sets are labelled by letters of the alphabet.

Thanks [sandassure](https://www.reddit.com/user/sandassure/) (and [Cryptizard](https://www.reddit.com/user/Cryptizard/)) for [the idea](https://www.reddit.com/r/cryptography/comments/1et5hy0/comment/lm3sz9j/), and thanks ChatGPT for the implementation (but not for suggesting a deterministic random function...lol) !

Currently there is support for `K`=3; `N`=5 only.

## Usage of this codebase

Be sure to [install Python](https://www.google.com/search?q=install+python) if you don't already have it, then download the Python files in this repo and follow the below example.

### Splitting

First, identify `N` shareholders (e.g. trusted friends or places) and then run the splitting code to obtain codes for each of them:

```
$ python3 ./3of5-XOR-Split.py
Enter the secret to be split: 🔥Secret🔥
Shareholder 1:
  Set A: 565625aa68fb4c5d293ef46b6982
  Set B: 760c39261e21ba92bd8da198191d
  Set C: f7bd089ab72d68ad5162fefd1a75
  Set D: c975f340d1d38aa6fed82f35e37e
  Set E: 89491092e5bbe2fcf14f18cd28d8
  Set F: 51508f6b3bed424c289d154d12a8

Shareholder 2:
  Set A: 238dfe8478365cad4e9f54f0fd79
  Set B: 9e5f2002bf221f850fef22214a5e
  Set C: 286d51711870a5128c629e271743
  Set G: 150d54cbfc9c1a61713f41adf900
  Set H: 60c04a94d4e2fbfebbe5135346d4
  Set I: 9a1384ba0d2ebbb1e694a26006f4

Shareholder 3:
  Set A: 85444f8b43a8738202d55004005e
  Set D: d8554e969b4e75d80b445b3259a9
  Set E: 254db616166434752e03cd513486
  Set G: 72aee438ee4db86ea63870661c77
  Set H: 707d73a6cd77c127f6994bf5c37c
  Set J: 05fc2df450836f1e4a1997bfa212

Shareholder 4:
  Set B: 18cc8d81f266c665d7167326c7e6
  Set D: e1bf297319f89c0c90e884982e72
  Set F: 17f096c5fa229416b03e48100793
  Set G: 973c245641b4c17db273c15471d2
  Set I: 2df13a4c3e0aeb3050e5038739e3
  Set J: 7d62d0581baf4702f669fbce0652

Shareholder 5:
  Set C: 2f4fcd4efc38aecdb87490459993
  Set E: 5c9b3221a0bab5fbba38250388fb
  Set F: b63f8d0b92aab528fdd7adc2819e
  Set H: e022ad974af059ab2808a839110d
  Set I: 477d2a53604133f3d3055178abb2
  Set J: 8801690918494b6ed9049cee30e5

$
```

Then distribute the codes to the shareholders. See the [Practical usage](#practical-usage) section of this document for
guidance.

### Combining

Enter any 3 shares from the same set. To do this, you might obtain the full list of shares from each of 3 shareholders, and then identify the letter that occurs in each of them and use the shares for that set. For example, shareholders #2, #3 and #5 all have shares for set "H".

```
$ python3 ./3ofN-XOR-combine.py 
Enter 3 shares (hex format) to reconstruct the secret:
Share 1: 60c04a94d4e2fbfebbe5135346d4
Share 2: 707d73a6cd77c127f6994bf5c37c
Share 3: e022ad974af059ab2808a839110d

Reconstructed Secret: 🔥Secret🔥
$
```

## Practical usage

Shareholders may be a mix of humans and physical locations. For example, one shareholder might be your lockbox at the
bank containing a printout its share(s). Another shareholder might be your friend whom you've asked (using a secure
channel) to keep their share(s) in an entry in their password manager.
Check out the [Privacy and security considerations](#privacy-and-security-considerations) section of this document for
some tips on choosing shareholders.

Introducing the concept of secret sharing to your trusted contacts and efficiently distributing shares to them can be
complicated.
Consider using the template messages in [Share Distribution Message Templates](docs/distribution-msg-templates.md) to
facilitate coordination with shareholders.
Having your 5 shareholders confirmed before entering your secret into any algorithm may make the process simpler and
more secure; you probably won't want to keep multiple shares floating around in insecure locations while you wait for
potential shareholders to confirm.

## Privacy and security considerations

* Human shareholders should have good "operational security"; they should be people you trust not to get hacked.
Examples of good practices of operational security include locking devices when not in use, keeping hardware and
software updated, using password managers properly, generally avoiding spyware, and being on the lookout for social
engineering attacks.
They should also be organized enough not to lose their share.
* Choose your human shareholders carefully so they will have a difficult time colluding to reconstruct your secret
without your permission.
* It is recommended to download these python files onto your computer and verify their contents yourself before running.
You'll have to trust the Python CLI / Standard Library of course, but this project contains no 3rd party
dependencies and does not require running any build scripts. If concerned about trojan source attacks, consider asking
Chat GPT to [regenerate this code from the same prompts](docs/chatgpt-prompt.md).
* Consider saving a backup of the code so you won't lose the ability to combine your secret in case this code is altered
in a backward-incompatible way or removed or made unavailable from its publicly hosted location.
* When distributing codes to trusted contacts, use a [privacy focused messaging app][priv-msg-app] with end-to-end
encryption.
* Only use this code and enter your secret on a device that you trust.
* Consider how you will keep the shares secret. Human shareholders are susceptible to social engineering and phishing.
* Note that even individual shares reveal the length of your secret.
* You may wish to keep the set of shareholders secret. Consider how you will guard this secret without foretting who the
shareholders are.

[priv-msg-app]: https://www.google.com/search?q=privacy+focused+messaging+app
