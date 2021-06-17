---
title: Pronoun notation
date: 2021-06-16 18:31:28 -0700
---
Pronoun sets: They're often notated with slashes, such as in `she/her` or `he/they`. Some time in the past I saw a meme which pointed out using exclusively slashes between pronouns has some ambiguity, and offered some symbols that could be used less ambiguously (and then humour; such is the nature of memes).  
But what if this notation were to be expanded and explicitly defined somewhere? I attempted to do that for some reason.

## The original meme
![multiple pronouns. she/they: ambiguous. she&they: use both, and switch it up often (bonus points for midsentence pronoun switch). she|they: choose any, they're all okay. she>they: she is best, but also cool with they. she\they: Windows file system. she☭they: our pronouns. she⊕they: I'm pretty sure these notes are for math class.](https://i.redd.it/qbvashrrsmm61.png)
## Pronoun-set notation specification (using <abbr title="augmented Backus-Naur form">ABNF</abbr>)
```
pronoun-set = precedence-set / "any" ("&"/"|") " except " exception-set

exception-set = declension-set *("," declension-set) ; one or more <declension-set>s separated by commas
precedence-set = equal-preference-set *(">" equal-preference-set) ; one or more <equal-preference-set>s separated by greater-than signs
equal-preference-set = mix-set *("|" mix-set) / OPWS "any|" OPWS ; one or more <mix-set>s separated by vertical bars, or "any|"
mix-set = declension-set *("&" declension-set) / OPWS "any&" OPWS ; one or more <declension-set>s separated by ampersands, or "any&"
declension-set = pronoun *("/" pronoun) ; one or more <pronoun>s separated by slashes
pronoun = OPWS (1*ALPHA / "ask pronoun") OPWS ; <pronoun> is one or more letters, or the string "ask pronoun"
OPWS = [WSP] ; optional whitespace
```
`ALPHA` here is not necessarily `ALPHA` from [the ABNF core rules](https://www.rfc-editor.org/rfc/rfc5234.html#appendix-B.1); here I am using `ALPHA` to mean letters in general. I will not attempt to specify what "letters in general" means here because there are a lot of writing systems.  
For backwards-compatibility purposes, if a pronoun set's only non-letter characters are the slash and optionally whitespace, it may be interpreted as multiple declension sets separated by slashes.  

Why did I use ABNF? There are an overwhelmingly large number of metasyntax notations; it is hard to choose one. In the end I chose ABNF because [ABNF has a public specification](https://www.rfc-editor.org/rfc/rfc5234.txt).
## Some example use cases
- `she&they`, `she|they`, `she>they` from the meme
- `she/they` is allowed too; here the reader needs to use context to determine this is multiple declension sets separated by slashes
- `any&`: any pronouns, switch it up often
- `any|`: any pronouns, switching it up often is not required
- `any& | xe/xir`: switch up any pronouns, or use `xe/xir` (this is an instance in which optional whitespace is useful because otherwise this'd end up containing the string `&|`)
- `any| except he,she`: any pronouns, except for `he` and `she`. Switching it up often is not required.
- `ask pronoun>she`: asking for pronoun is best, but also cool with `she`. (good for if you are not always able to reply to requests for pronouns in a timely manner)
- `ask pronoun/em/eir/eirs/ask pronoun > e/emself`: ask only for certain declensions (with unable-to-reply-to-requests-in-a-timely-manner in this case being Spivak). (also observe that declensions don't have a set order, though nominative/accusative/possessive determiner/possessive/reflexive seems to be common in English)
- `they&he|they&she`: either switch between `they` and `he` or switch between `they` and `she`
- `they>he|she`: `they` is best, but `he` or `she` are equally okay as well

Are there use cases which this spec doesn't cover? Quite possibly! In that case this spec could be superseded by another spec. In that case I would request that you follow the **Design goals** below, but I can't force you or anything
## Design goals
My design goals for this spec were:
1. Be able to represent many pronoun sets
2. Be backwards-compatible (with existing slash notation and the meme's first three items I guess)
3. Be somewhat human-readable

## neat now this thing is on the world wide web
hope this has been enjoyable to read i guess
