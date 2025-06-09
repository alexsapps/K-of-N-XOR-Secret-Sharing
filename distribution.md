Here are some template messages you may use to facilitate coordination with shareholders.

## Invitation

Hi <b>&lt;shareholder&gt;</b>, could I give you a password of sorts that you can give back to me later, in case I forget it?
I'm asking this to people I trust because data is client-encrypted, so there's no way to recover my data if I
forget the password.

This would require a password manager that has a multi-line text field such as a "notes" field--not just username and
password fields--in order to securely store several lines of secret data I would provide you and instructions for
handling it when needed.

Rather than giving you my actual password, I would give you a "share" of it--just one of many pieces of information
needed to reconstruct my actual password using something called a "secret sharing algorithm". You would be one of
multiple people who I'm asking to do the same thing as you. With the help of enough of those people, I can get my
password back later on if I forget it.

If you ever got a message from me in the future saying I forgot my password or otherwise requesting this piece of
information in your password manager, I would be trusting you to insist on a video call to make sure it's not someone
trying to impersonate me (such as a scammer or undercover police), and then I'd rely on you to give me the secret data
back. If I make up some excuse why I can't video call, then I'd trust you to refuse to give me anything, as it might not
be me asking at all. Also, it's highly unlikely, but if authorities demanded this piece of information, I'd need you to
insist on speaking with a lawyer first.

Please let me know if you'd be willing to help. Then, once I confirm everyone, I'll send out the secret shares.

## Distribution

Hi <b>&lt;shareholder&gt;</b>, please store the text below as an entry in your password manager, including the warning
message, secret data, and instructions for reconstructing.

The entry may be called:

> <b>&lt;secret owner&gt;</b>'s secret sharing for <b>&lt;description of secret&gt;</b>

Here is the text to store:

> Warning: Do not disclose this information to anyone but the secret owner, <b>&lt;name&gt;</b>. You must verify the
secret owner's identity in person or on a video call. Do not disclose to law enforcement or government agencies;
contact <b>&lt;legal or organizational resource&gt;</b> for assistance. Even if the secret owner is claimed to be
incapacitated or unavailable, do not disclose to others.
>
> Secret data:
> <b>&lt;secret&gt;</b>
>
> Description: <b>&lt;description of secret&gt;</b>
>
> Date: <b>&lt;today's date&gt;</b>
>
> Instructions for the secret owner to reconstruct the secret: collect <b>&lt;K&gt;</b> shares with matching labels;
decode the hexadecimal-encoded strings into byte sequences, compute the bitwise XOR of corresponding bytes, and decode
the resulting byte sequence as a UTF-8 string. Example code:
https://github.com/alexsapps/K-of-N-XOR-Secret-Sharing/blob/f2df5d257e8bf25c72dac9cd90d993ae76baac29/3ofN-XOR-combine.py
