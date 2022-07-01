# String Searching Algorithm

[Wikipedia](https://en.wikipedia.org/wiki/String_search_algorithm)

String-searching algorithms are used to find where patterns are found within a larger string.


## Single-pattern algorithms

- m: length of the pattern
- n: length of the text
- k: size of the alphabet

| Algorithm | Preprocessing time | Matching time | Space |
| :---: | :---: | :---: | :---: |
| [Naive string search](naive_string_search) | none | $θ(mn)$ | none |
| [Rabin-Karp](rabin_karp) | $θ(m)$ | $θ(n)$ <br> $O(mn)$ | $O(1)$ |
| [KMP](KMP) | $θ(m)$ | $θ(n)$ | $θ(m)$ |
| [Boyer-Moore](boyer_moore) | $θ(m+k)$ | $Ω(n/m)$ <br> $O(mn)$ | $θ(k)$ |
| [Two-way algorithm](two_way) | $θ(m)$ | $O(n)$ | $O(1)$ |
| [Backwrad Non-Deterministic DAWG Matching (BNDM)](BNDM) | $O(m)$ | $O(n)$ | |
| [Backward Oracle Matching (BOM)](BOM) | $O(m)$ | $O(mn)$ | |

## Algorithms using a fiite set of patterns

- M: length of the longest pattern
- m: total length
- n: length of the text
- o: the number of occurrences

| Algorithm | Extension of | Preprocessing time | Matching time | Space |
| :---: | :---: | :---: | :---: | :---: |
| [Aho-Corasick](aho_corasick) | KMP | θ(m) | $θ(n + o)$ | θ(m) |
| [Commentz-Walter](commentz_walter) | Boyer-Moore | θ(m) | $θ(Mn)$ at worst<br>sublinear in average | θ(m) |
| [Set-BOM](set_BOM) | BOM |  |  |  |
